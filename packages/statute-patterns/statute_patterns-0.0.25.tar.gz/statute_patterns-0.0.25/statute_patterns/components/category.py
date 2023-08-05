import re
from enum import Enum

from pydantic import BaseModel


class StatuteSerialCategory(str, Enum):
    """
    This is a non-exhaustive taxonomy of Philippine legal rules for the purpose of enumerating fixed values.

    Both parts of the member declaration have meaning.

    The **name** of each statute category can be "uncamel"-ized to produce a serial title of the member for _most_ of the members enumerated.

    The **value** of each statute category serves 2 purposes:

    1. it refers to the folder to source raw .yaml files for the creation of the Statute object for the database; and
    2. it refers to the category as it appears in the database table.
    """

    RepublicAct = "ra"
    CommonwealthAct = "ca"
    Act = "act"
    Constitution = "const"
    Spain = "spain"
    BatasPambansa = "bp"
    PresidentialDecree = "pd"
    ExecutiveOrder = "eo"
    LetterOfInstruction = "loi"
    VetoMessage = "veto"
    RulesOfCourt = "roc"
    BarMatter = "rule_bm"
    AdministrativeMatter = "rule_am"
    ResolutionEnBanc = "rule_reso"
    CircularOCA = "oca_cir"
    CircularSC = "sc_cir"

    def serialize(self, idx: str):
        """Given a member item and a valid serialized identifier, create a serial title.

        Note that the identifier must be upper-cased to make this consistent with the textual convention, e.g.

        1. `pd` + `570-a` = `Presidential Decree No. 570-A`
        2. `rule_am` + `03-06-13-sc` = `Administrative Matter No. 03-06-13-SC`
        """

        def uncamel(cat: StatuteSerialCategory):
            """See https://stackoverflow.com/a/9283563"""
            x = r"((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))"
            return re.sub(x, r" \1", cat.name)

        match self:
            case StatuteSerialCategory.Spain:
                small_idx = idx.lower()
                if small_idx in ["civil", "penal"]:
                    return f"Spanish {idx.title()} Code"
                elif small_idx == "commerce":
                    return "Code of Commerce"
                raise SyntaxWarning(f"{idx=} invalid serial of {self}")

            case StatuteSerialCategory.Constitution:
                if idx.isdigit() and int(idx) in [1935, 1973, 1987]:
                    return f"{idx} Constitution"
                raise SyntaxWarning(f"{idx=} invalid serial of {self}")

            case StatuteSerialCategory.RulesOfCourt:
                if idx in ["1940", "1964"]:
                    return f"{idx} Rules of Court"
                elif idx in ["cpr"]:
                    return "Code of Professional Responsibility"
                raise SyntaxWarning(f"{idx=} invalid serial of {self}")

            case StatuteSerialCategory.VetoMessage:
                """No need to specify No.; understood to mean a Republic Act"""
                return f"Veto Message - {idx}"

            case StatuteSerialCategory.ResolutionEnBanc:
                """The `idx` needs to be a specific itemized date."""
                return f"Resolution of the Court En Banc dated {idx}"

            case StatuteSerialCategory.CircularSC:
                return f"SC Circular No. {idx}"

            case StatuteSerialCategory.CircularOCA:
                return f"OCA Circular No. {idx}"

            case StatuteSerialCategory.AdministrativeMatter:
                """Handle special rule with variants: e.g.`rule_am 00-5-03-sc-1` and `rule_am 00-5-03-sc-2`"""
                am = uncamel(self)
                small_idx = idx.lower()
                if "sc" in small_idx:
                    if small_idx.endswith("sc"):
                        return f"{am} No. {small_idx.upper()}"
                    elif sans_var := re.search(r"^.*-sc(?=-\d+)", small_idx):
                        return f"{am} No. {sans_var.group().upper()}"
                return f"{am} No. {small_idx.upper()}"

            case StatuteSerialCategory.BatasPambansa:
                if idx.isdigit():
                    return f"{uncamel(self)} Blg. {idx}"  # there are no -A -B suffixes in BPs

            case _:
                # no need to uppercase pure digits
                target_digit = idx if idx.isdigit() else idx.upper()
                return f"{uncamel(self)} No. {target_digit}"


class StatuteTitleCategory(str, Enum):
    """
    Each statute's title can be categorized as being the official title, a serialized title, an alias, and a short title.

    A `Rule` should contain at least 2 of these categories: (a) the official one which is the full length title; and (b) the serialized version which contemplates a category and an identifier.

    A statute however can also have a short title which is still official since it is made explicit by the rule itself.

    An alias on the other hand may not be an official way of referring to a statute but it is a popular way of doing so.
    """

    Official = "official"
    Serial = "serial"
    Alias = "alias"
    Short = "short"


class StatuteTitle(BaseModel):
    """Will be used to populate the database; assumes a fixed `statute_id`."""

    statute_id: str
    category: StatuteTitleCategory
    text: str

    class Config:
        use_enum_values = True

    @classmethod
    def generate(
        cls,
        pk: str,
        official: str | None = None,
        serial: str | None = None,
        short: str | None = None,
        aliases: list[str] | None = None,
    ):
        if aliases:
            for title in aliases:
                if title and title != "":
                    yield cls(
                        statute_id=pk,
                        category=StatuteTitleCategory.Alias,
                        text=title,
                    )
        if short:
            yield cls(
                statute_id=pk,
                category=StatuteTitleCategory.Short,
                text=short,
            )

        if serial:
            yield cls(
                statute_id=pk,
                category=StatuteTitleCategory.Serial,
                text=serial,
            )

        if official:
            yield cls(
                statute_id=pk,
                category=StatuteTitleCategory.Official,
                text=official,
            )
