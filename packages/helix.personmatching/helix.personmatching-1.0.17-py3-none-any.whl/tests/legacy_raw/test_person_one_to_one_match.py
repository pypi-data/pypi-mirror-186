from typing import Any, Dict, List, Optional

from nicknames import NickNamer

from helix_personmatching.logics.rule_score import RuleScore
from helix_personmatching.logics.rules_generator import RulesGenerator
from helix_personmatching.logics.score_calculator import ScoreCalculator
from helix_personmatching.logics.scoring_input import ScoringInput
from helix_personmatching.models.constants import Attribute
from helix_personmatching.models.rule import Rule
from helix_personmatching.models.rule_option import RuleOption


def test_person_one_to_one_match() -> None:
    person_1_dict: Dict[str, Any] = {
        Attribute.ID.name: "unitypoint-b3a42xc8",
        Attribute.NAME_FAMILY.name: "bourne",
        Attribute.NAME_GIVEN.name: "James ",
        Attribute.NAME_MIDDLE.name: "Iqbal ",
        Attribute.NAME_MIDDLE_INITIAL.name: "I ",
        Attribute.GENDER.name: "MALE",
        Attribute.BIRTH_DATE.name: "1980-09-17",
        Attribute.BIRTH_DATE_YEAR.name: "1980",  # parsed from birth date
        Attribute.BIRTH_DATE_MONTH.name: "09",  # parsed from birth date
        Attribute.BIRTH_DATE_DAY.name: "17",  # parsed from birth date
        Attribute.ADDRESS_LINE_1.name: "363 Mackerline St",
        Attribute.ADDRESS_LINE_1_ST_NUM.name: "363",  # parsed from address
        Attribute.ADDRESS_POSTAL_CODE.name: "34239",
        Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE.name: "34239",
        Attribute.EMAIL.name: "jbourne@gmail.com",
        Attribute.EMAIL_USERNAME.name: "jborune",  # parsed from the email
        Attribute.PHONE.name: "7770003333",
        Attribute.PHONE_AREA.name: "777",  # parsed from phone
        Attribute.PHONE_LOCAL.name: "000",  # parsed from phone
        Attribute.PHONE_LINE.name: "3333",  # parsed from phone
        Attribute.IS_ADULT_TODAY.name: "true",  # calculated by today's date - birth date >= 18 yrs old
        Attribute.SSN.name: "",  # parsed from identifier.value
        Attribute.SSN_LAST4.name: "",  # parsed from identifier.value
        Attribute.META_SECURITY_CLIENT_SLUG.name: "unitypoint",  # parsed from meta.security access
    }

    person_2_dict: Dict[str, Any] = {
        Attribute.ID.name: "unitypoint-73bvy14ka0",
        Attribute.NAME_FAMILY.name: "BORNE",
        Attribute.NAME_GIVEN.name: " JAMES ",
        Attribute.NAME_MIDDLE.name: "Iqbal ",
        Attribute.NAME_MIDDLE_INITIAL.name: "I ",
        Attribute.GENDER.name: "male",
        Attribute.BIRTH_DATE.name: "1980-09-17",
        Attribute.BIRTH_DATE_YEAR.name: "1980",  # parsed from birth date
        Attribute.BIRTH_DATE_MONTH.name: "09",  # parsed from birth date
        Attribute.BIRTH_DATE_DAY.name: "17",  # parsed from birth date
        Attribute.ADDRESS_LINE_1.name: "363 mackerline st.",
        Attribute.ADDRESS_LINE_1_ST_NUM.name: "363",  # parsed from address
        Attribute.ADDRESS_POSTAL_CODE.name: "34239",
        Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE.name: "34239",
        Attribute.EMAIL.name: "jbourne@hotmail.com",
        Attribute.EMAIL_USERNAME.name: "jborune",  # parsed from the email
        Attribute.PHONE.name: "7770003355",
        Attribute.PHONE_AREA.name: "777",  # parsed from phone
        Attribute.PHONE_LOCAL.name: "000",  # parsed from phone
        Attribute.PHONE_LINE.name: "3355",  # parsed from phone
        Attribute.IS_ADULT_TODAY.name: "true",  # calculated by today's date - birth date >= 18 yrs old
        Attribute.SSN.name: "555992222",
        Attribute.SSN_LAST4.name: "2222",
        Attribute.META_SECURITY_CLIENT_SLUG.name: "unitypoint",
    }

    rules: List[Rule] = RulesGenerator.generate_rules(options=None)

    person1: ScoringInput = ScoringInput(**person_1_dict)
    person2: ScoringInput = ScoringInput(**person_2_dict)

    # match on first rule
    rule_score_result: Optional[RuleScore] = ScoreCalculator.calculate_score_for_rule(
        rule=rules[0],
        source=person1,
        target=person2,
        rule_option=RuleOption(nick_namer=NickNamer()),
    )
    assert (
        rule_score_result is not None
        and rule_score_result.id_source is not None
        and rule_score_result.id_target is not None
        and rule_score_result.rule_score is not None
    )
    print(rule_score_result)

    # match on all rules
    rules_score_results: List[RuleScore] = ScoreCalculator.calculate_score(
        rules, person1, person2
    )

    rules_score_results = sorted(
        rules_score_results, key=lambda x: x.rule_score, reverse=True
    )

    assert len(rules_score_results) == len(rules)
    print(f"================ Rule Scores ==================")
    for result in rules_score_results:
        print(f"{result.rule_name} = {result.rule_score} ({result.rule_description})")
        print(result.to_json())

    # calculate the final score
    final_score: float = 0.0
    for result in rules_score_results:
        # the score is uniqueness probability
        # pick the highest probability
        if result.rule_score > final_score:
            final_score = result.rule_score

    # number_of_rules_with_present_attributes: int = (
    #     ScoreCalculator.get_number_of_rules_with_present_attributes(rules_score_results)
    # )
    #
    # final_score /= number_of_rules_with_present_attributes

    print(f"FINAL SCORE: {final_score}")

    # SUGGESTION
    # based on the calculated final score, in 0-100 scale,
    #  the caller categorize and assign the FHIR AssuranceLevel when creating data linkage,
    #  https://www.hl7.org/fhir/valueset-identity-assuranceLevel.html#expansion
    #  "level1" (the lowest): 0.0 - 20.0 for little or no confidence in the asserted identity's accuracy
    #  "level2"             : 20.0 - 60.0 for some confidence
    #  "level3"             : 60.0 - 80.0 for high confidence
    #  "level4" (the highest): 80.0 - 100.0 for very high confidence
