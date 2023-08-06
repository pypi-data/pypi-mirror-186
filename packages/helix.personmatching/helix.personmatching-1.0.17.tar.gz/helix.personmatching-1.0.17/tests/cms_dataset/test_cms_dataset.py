from datetime import datetime, timedelta
from pathlib import Path
import csv
from typing import Dict, Optional, List

# noinspection PyPackageRequirements
import pytest

# noinspection PyPackageRequirements
from fhir.resources.address import Address

# noinspection PyPackageRequirements
from fhir.resources.bundle import Bundle, BundleEntry

# noinspection PyPackageRequirements
# noinspection PyPackageRequirements
from fhir.resources.contactpoint import ContactPoint

# noinspection PyPackageRequirements
from fhir.resources.humanname import HumanName

# noinspection PyPackageRequirements
from fhir.resources.identifier import Identifier

# noinspection PyPackageRequirements
from fhir.resources.patient import Patient

from helix_personmatching.logics.match_score import MatchScore
from helix_personmatching.matchers.matcher import Matcher


def create_patient_resource(row: Dict[str, str]) -> Patient:
    patient: Patient = Patient()
    patient.id = row["EnterpriseID"]
    patient.name = [
        HumanName(
            family=row["LAST"],
        )
    ]
    if row["FIRST"] or row["MIDDLE"]:
        patient.name[0].given = []

    if row["FIRST"]:
        first_: str = row["FIRST"]
        if first_:
            # noinspection PyUnresolvedReferences,PyTypeChecker
            patient.name[0].given.append(first_)

    if row["MIDDLE"]:
        middle: str = row["MIDDLE"]
        # noinspection PyUnresolvedReferences
        patient.name[0].given.append(middle)

    if row["SUFFIX"]:
        patient.name[0].suffix = [row["SUFFIX"]]

    if row["GENDER"]:
        if row["GENDER"] == "FEMALE" or row["GENDER"] == "F":
            patient.gender = "female"
        elif row["GENDER"] == "MALE" or row["GENDER"] == "M":
            patient.gender = "male"
        elif row["GENDER"] == "U":
            patient.gender = "unknown"
        else:
            raise NotImplementedError(f"Unknown gender: {row['GENDER']}")

    if row["DOB"]:
        # DOB is in number of days from 1/1/1900
        initial_date = datetime.strptime("1-1-1900", "%m-%d-%Y")
        dob_ = initial_date + timedelta(days=int(row["DOB"]) - 2)
        patient.birthDate = dob_
    if row["SSN"]:
        patient.identifier = [
            Identifier(system="http://hl7.org/fhir/sid/us-ssn", value=row["SSN"])
        ]
    if row["ADDRESS1"] or row["ADDRESS2"] or row["ZIP"] or row["CITY"] or row["STATE"]:
        patient.address = [Address(use="home")]

    if row["ADDRESS1"]:
        patient.address[0].line = [row["ADDRESS1"]]
    if row["ADDRESS2"]:
        address_2 = row["ADDRESS2"]
        if not patient.address[0].line:
            patient.address[0].line = []
        if address_2:
            # noinspection PyTypeChecker
            patient.address[0].line.append(address_2)

    if row["CITY"]:
        patient.address[0].city = row["CITY"]

    if row["STATE"]:
        patient.address[0].state = row["STATE"]

    if row["ZIP"]:
        # noinspection PyPep8Naming
        patient.address[0].postalCode = row["ZIP"]

    if row["PHONE"] or row["EMAIL"]:
        patient.telecom = []
    if row["PHONE"]:
        patient.telecom.append(ContactPoint(system="phone", value=row["PHONE"]))
    if row["EMAIL"]:
        patient.telecom.append(ContactPoint(system="email", value=row["EMAIL"]))
    return patient


@pytest.mark.integration
def test_cms_dataset() -> None:
    print("")
    data_dir: Path = Path(__file__).parent.joinpath("./")

    limit: Optional[int] = 1000
    limit_to_id: Optional[str] = None  # "12871231"
    # limit_to_id: Optional[List[str]] = ["15391849", "15992723"]

    file_name = "ONC Patient Matching Algorithm Challenge Test Dataset.A-C.csv"

    print(f"==== Testing {file_name} ========")
    with open(data_dir.joinpath("files/onc").joinpath(file_name)) as file:
        csv_reader = csv.DictReader(file)
        patients = list()
        i: int = 0
        for row in csv_reader:
            i = i + 1
            if limit and i > limit:
                break
            if limit_to_id is not None:
                if row["EnterpriseID"] not in limit_to_id:
                    continue
            patients.append(create_patient_resource(row=row))
        print(f"Count of rows={len(patients)}")

        bundle = Bundle(
            type="searchset",
            total=len(patients),
            entry=[BundleEntry(resource=resource) for resource in patients],
        )
        with open(
            data_dir.joinpath("files/bundles").joinpath(
                file_name.replace(".csv", ".json")
            ),
            "w",
        ) as json_file:
            json_file.write(bundle.json())

        passed_records: Dict[str, List[MatchScore]] = {}
        failed_records: Dict[str, List[MatchScore]] = {}
        not_matched_records: Dict[str, List[MatchScore]] = {}
        matcher: Matcher = Matcher()
        match_scores: List[MatchScore] = matcher.match_resources(
            source=bundle,
            target=bundle,
            verbose=True,
            only_matches=True if not limit_to_id else False,
        )
        # noinspection PyUnresolvedReferences
        for source in [e.resource for e in bundle.entry]:
            sorted_match_scores = [
                score for score in match_scores if source.id == score.id_source
            ]
            sorted_match_scores = sorted(
                sorted_match_scores, key=lambda x: x.total_score, reverse=True
            )
            matched_records = [s for s in sorted_match_scores if s.matched is True]

            if len(matched_records) == 0:
                match_scores_for_id = [
                    s for s in sorted_match_scores if s.id_target == source.id
                ]
                not_matched_records[source.id] = match_scores_for_id
            else:
                if matched_records[0].id_target != source.id:
                    failed_records[source.id] = matched_records
                else:
                    passed_records[source.id] = [matched_records[0]]

        print(
            f"\n====== MATCHES PASSED ({len(passed_records)}/{len(patients)}) ======="
        )
        for id_, scores in passed_records.items():
            print(scores[0].to_json())

        print(
            f"\n==== NO MATCHES FOUND ({len(not_matched_records)}/{len(patients)}) ========"
        )
        for id_, scores in not_matched_records.items():
            print(f"--------- {id_} -------")
            if len(scores) > 0:
                first_rule_score = scores[0].rule_scores[0]
                print(
                    f"{first_rule_score.rule_name} = {first_rule_score.rule_score} "
                    + f"({first_rule_score.rule_description})"
                )
                for score in scores:
                    print(score.to_json())

        failed_records_with_higher_probabilities: List[MatchScore] = []
        print(
            f"\n====== MATCHES TO WRONG RECORD ({len(failed_records)}/{len(patients)}) ========="
        )
        for id_, scores in failed_records.items():
            print(f"--------- {id_} -------")
            score_of_source_record = [
                score for score in scores if score.id_source == score.id_target
            ][0]
            for score in scores:
                if score.total_score > score_of_source_record.total_score:
                    failed_records_with_higher_probabilities.append(score)
                print(
                    f"Total score: {score.total_score}, "
                    + f"Total score unscaled: {score.total_score_unscaled} "
                    + f"Avg score: {score.average_score}, "
                    + f"Avg boost: {score.average_boost}"
                )
                print(score.to_json())
                for rule_score in score.rule_scores:
                    print(f"{rule_score.rule_name}: {rule_score.rule_score}")

        assert (
            len(not_matched_records) / len(patients) < 1.0
        ), f"Found {len(not_matched_records)} records that had no match"
        assert (
            len(failed_records) / len(patients) < 1.0
        ), f"Found {len(failed_records)} records that had wrong match"

        assert len(failed_records_with_higher_probabilities) == 0, (
            f"Found {len(failed_records_with_higher_probabilities)} records "
            + f"{[s.id_source for s in failed_records_with_higher_probabilities]} "
            + f"that had wrong match with higher probability"
        )
