from typing import List, Optional

from helix_personmatching.models.rules.RuleWeight import RuleWeight
from helix_personmatching.models.rules.attribute_rule import AttributeRule
from helix_personmatching.models.constants import Attribute
from helix_personmatching.models.rules.booster_rule import BoosterRule
from helix_personmatching.models.rule import Rule
from helix_personmatching.models.scoring_option import ScoringOption


class RulesGenerator:
    @staticmethod
    def generate_rules(*, options: Optional[List[ScoringOption]] = None) -> List[Rule]:
        """
        generate default match rules
        :return: generated rules for matching
        """

        standard_weight = RuleWeight.get_standard_weight()

        # https://sequoiaproject.org/wp-content/uploads/2015/11/The-Sequoia-Project-Framework-for-Patient-Identity-Management.pdf
        # Sequence  Traits                      Completeness    Uniqueness
        # 1         FN+LN+DoB                   98.2%           95.7%
        # 2         FN+LN+DoB+Sex               98.2%           95.9%
        # 3*        FN+LN+DoB+Sex+ZIP(first 5)  91.1%           99.2%
        # 4*        FN+LN+DoB+Sex+Phone         76.2%           99.5%
        # 5         FN+LN+DoB+Sex+MN            59.9%           98.9%
        # 6         FN+LN+DoB+Sex+MN(initial)   60.0%           97.7%
        # 7*        FN+LN+DoB+Sex+SSN(last 4)   61.9%           99.7%

        rules: List[Rule] = [
            AttributeRule(
                # This is a very high uniqueness rule:
                # https://sequoiaproject.org/wp-content/uploads/2015/11/The-Sequoia-Project-Framework-for-Patient-Identity-Management.pdf
                name="Rule-001",
                description="given name, family name, gender, dob, zip",
                number=1,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.GENDER,
                    Attribute.BIRTH_DATE,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                ],
                # Sequence  Traits                      Completeness Uniqueness
                # 3         FN+LN+DoB+Sex+ZIP(first 5)  91.1%         99.2%
                weight=RuleWeight(exact_match=0.992, partial_match=0.992, missing=0.75),
            ),
            AttributeRule(
                name="Rule-002",
                description="given name, dob, address 1, zip",
                number=2,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-003",
                description="given name, date of birth, email",
                number=3,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.EMAIL,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-004",
                description="given name, date of birth, phone",
                number=4,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.PHONE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-005",
                description="given name, family name, year of date of birth, gender, address 1, zip",
                number=5,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE_YEAR,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-006",
                description="given name, family name, dob month, dob date, gender, address 1, zip",
                number=6,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE_MONTH,
                    Attribute.BIRTH_DATE_DAY,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                # very high uniqueness rule:
                # https://sequoiaproject.org/wp-content/uploads/2015/11/The-Sequoia-Project-Framework-for-Patient-Identity-Management.pdf
                name="Rule-007",
                description="given name, family name, date of birth, gender, phone",
                number=7,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.PHONE,
                ],
                # 4         FN+LN+DoB+Sex+Phone         76.2%           99.5%
                weight=RuleWeight(exact_match=0.995, partial_match=0.995, missing=0.75),
            ),
            AttributeRule(
                name="Rule-008",
                description="first name, last name, date of birth, gender, phone local exchange, phone line",
                number=8,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.PHONE_LOCAL,
                    Attribute.PHONE_LINE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-009",
                description="first name, last name, date of birth, gender, phone area code, phone line",
                number=9,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LINE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-010",
                description="given name, dob, gender, address 1 street number, zip, email username, phone line",
                number=10,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                    Attribute.EMAIL_USERNAME,
                    Attribute.PHONE_LINE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-011",
                description="given name, dob, gender, address 1 street number, zip, "
                + "phone area code, phone local exchange code",
                number=11,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LOCAL,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-012",
                description="given name, dob, gender, address 1 street number, zip, phone area code, phone line number",
                number=12,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                    Attribute.PHONE_AREA,
                    Attribute.PHONE_LINE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-013",
                description="given name, dob, gender, address 1 street number, zip, "
                + "phone local exchange code, phone line number",
                number=13,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1_ST_NUM,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                    Attribute.PHONE_LOCAL,
                    Attribute.PHONE_LINE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-014",
                description="family name, date of birth, is adult today flag, gender, address 1, zip, phone",
                number=14,
                attributes=[
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.IS_ADULT_TODAY,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                    Attribute.PHONE,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-015",
                description="family name, date of birth, is adult today flag, gender, address 1, zip, email",
                number=15,
                attributes=[
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.IS_ADULT_TODAY,
                    Attribute.GENDER,
                    Attribute.ADDRESS_LINE_1,
                    Attribute.ADDRESS_POSTAL_CODE_FIRST_FIVE,
                    Attribute.EMAIL,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                name="Rule-016",
                description="given name, email, phone, dob_year",
                number=16,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.EMAIL,
                    Attribute.PHONE,
                    Attribute.BIRTH_DATE_YEAR,
                ],
                weight=standard_weight,
            ),
            AttributeRule(
                # This is a very high uniqueness rule:
                # https://sequoiaproject.org/wp-content/uploads/2015/11/The-Sequoia-Project-Framework-for-Patient-Identity-Management.pdf
                name="Rule-017",
                description="given name, last name, date of birth, gender, SSN (last 4)",
                number=16,
                attributes=[
                    Attribute.NAME_GIVEN,
                    Attribute.NAME_FAMILY,
                    Attribute.BIRTH_DATE,
                    Attribute.GENDER,
                    Attribute.SSN,
                ],
                # 7         FN+LN+DoB+Sex+SSN(last 4)   61.9%           99.7%
                weight=RuleWeight(exact_match=0.997, partial_match=0.997, missing=0.75),
            ),
        ]

        if options and len(options) > 0:
            available_extra_rules = [
                BoosterRule(
                    name="Rule-050",
                    description="fixed score",
                    number=50,
                    weight=RuleWeight(
                        boost=0.51, exact_match=0.0, partial_match=0.0, missing=0.0
                    ),
                )
            ]
            rules.extend(
                [
                    rule
                    for rule in available_extra_rules
                    if any([r for r in options if rule.name == r.rule_name])
                ]
            )

            for option in options:
                matching_rules = [
                    rule for rule in rules if rule.name == option.rule_name
                ]
                if len(matching_rules) > 0:
                    matching_rule = matching_rules[0]
                    if option.weight is not None:
                        matching_rule.weight = option.weight

        return rules
