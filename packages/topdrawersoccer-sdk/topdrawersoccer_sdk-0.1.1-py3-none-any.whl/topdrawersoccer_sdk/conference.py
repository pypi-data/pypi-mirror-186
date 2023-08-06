from urllib.parse import urljoin

from soccer_sdk_utils.page import PageObject
from soccer_sdk_utils.gender import Gender
from soccer_sdk_utils.tools import get_href_from_anchor, get_text_from_anchor

from soccer_sdk_utils.model.school import School

from soccer_sdk_utils.division import Division
from topdrawersoccer_sdk.constants import PREFIX
from soccer_sdk_utils.model.conference import Conference
from soccer_sdk_utils.model.values import Values
from topdrawersoccer_sdk.utils import get_identifier_from_url


def division_to_conference_url(division: Division) -> str:
    """
    Retrieve the conference URL for a given division.

    :param division:
    :return:
    """
    if division == Division.DI:
        return urljoin(PREFIX, "college-soccer/college-conferences/di/divisionid-1")

    if division == Division.DII:
        return urljoin(PREFIX, "college-soccer/college-conferences/dii/divisionid-2")

    if division == Division.DIII:
        return urljoin(PREFIX, "college-soccer/college-conferences/diii/divisionid-3")

    if division == Division.NAIA:
        return urljoin(PREFIX, "college-soccer/college-conferences/naia/divisionid-4")

    if division == Division.NJCAA:
        return urljoin(PREFIX, "college-soccer/college-conferences/njcaa/divisionid-5")

    raise ValueError(f"Unsupported division '{division}'")


class ConferencePage(PageObject):
    def __init__(self, _conference: Conference, **kwargs):
        super().__init__(**kwargs)
        self.conference = _conference

    def schools(self) -> list:
        """Returns a list of schools in the conference"""
        schools = []

        self.load(self.conference.urls.tds)
        anchors = self.soup.find_all("a", class_=["player-name"])
        for anchor in anchors:
            school = School()
            school.name = get_text_from_anchor(anchor)
            school.gender = self.conference.gender
            school.urls = Values(
                tds=urljoin(PREFIX, get_href_from_anchor(anchor))
            )
            school.ids = Values(tds=get_identifier_from_url(school.urls.tds))

            schools.append(school)

        return schools


class ConferencesPage(PageObject):
    def __init__(self, gender: Gender, division: Division, **kwargs):
        pass

    def get_conferences(self) -> list[Conference]:
        pass
