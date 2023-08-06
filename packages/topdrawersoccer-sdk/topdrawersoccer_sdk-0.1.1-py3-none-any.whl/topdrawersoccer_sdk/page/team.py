from urllib.parse import urlparse
from urllib.parse import parse_qs

import bs4
import requests
from soccer_sdk_utils.division import Division, DivisionList
from soccer_sdk_utils.gender import Gender, string_to_gender
from soccer_sdk_utils.model.conference import Conference
from soccer_sdk_utils.model.school import School
from soccer_sdk_utils.tools import urljoin
from soccer_sdk_utils.page import PageObject
from soccer_sdk_utils.tools import get_href_from_anchor, get_text_from_anchor

from topdrawersoccer_sdk.constants import PREFIX
from topdrawersoccer_sdk.mapping import TEAMS_URL
from topdrawersoccer_sdk.utils import url_to_gender, get_identifier_from_url


class TeamsPage(PageObject):
    def __init__(self, division: Division, **kwargs):
        super().__init__(**kwargs)

        self.division = division
        self.url = TEAMS_URL[self.division]

        self.load()

    @property
    def division(self) -> Division:
        return self._division

    @division.setter
    def division(self, value: Division):
        self._division = value

    def get_conference_names(self):
        conference_names = []

        tables = self.soup.find_all("table", class_=["table-striped", "tds-table"])

        for table in tables:
            conference_name = table.find("caption").text
            conference_names.append(conference_name)

        conference_names.sort()

        return conference_names

    def get_conferences(self) -> list[Conference]:
        conferences = []

        tables = self.soup.find_all("table", class_=["table-striped", "tds-table"])

        for table in tables:
            caption_tag = table.find("caption")

            text = get_text_from_anchor(caption_tag)
            href = get_href_from_anchor(caption_tag)
            url = urljoin(PREFIX, href)

            parsed_url = urlparse(url)
            conference_id = parse_qs(parsed_url.query)["conferenceId"][0]

            conference = Conference()
            conference.name = text
            conference.division = self.division
            conference.urls.tds = url
            conference.ids.tds = conference_id

            conferences.append(conference)

        return conferences

    def get_conference_by_name(self, conference_name: str) -> Conference | None:
        tables = self.soup.find_all("table", class_=["table-striped", "tds-table"])

        for table in tables:
            caption_tag = table.find("caption")

            name = get_text_from_anchor(caption_tag)

            if name != conference_name:
                continue

            conference = Conference()
            conference.name = name
            conference.division = self.division
            conference.urls.tds = urljoin(
                PREFIX, get_href_from_anchor(caption_tag)
            )

            url = urljoin(PREFIX, conference.urls.tds)

            parsed_url = urlparse(url)
            conference_id = parse_qs(parsed_url.query)["conferenceId"][0]

            conference.ids.tds = conference_id

            return conference

        return None

    def get_schools_by_conference_name(self, target_conference_name: str, gender: Gender) -> list[School]:
        schools = []

        tables = self.soup.find_all("table", class_=["table-striped", "tds-table"])

        for table in tables:
            caption_tag = table.find("caption")

            conference_name = get_text_from_anchor(caption_tag)

            if conference_name != target_conference_name:
                continue

            rows = table.find_all("tr")
            for row in rows:
                column = row.find("td")

                href = get_href_from_anchor(column)

                buffer = url_to_gender(href)
                href_gender = string_to_gender(buffer)

                if href_gender != gender:
                    continue

                href_id = get_identifier_from_url(href)

                school = School()
                school.name = get_text_from_anchor(column)
                school.urls.tds = urljoin(PREFIX, href)
                school.ids.tds = href_id
                school.gender = href_gender

                schools.append(school)

        return schools

    def get_clgid_by_name(self, target_school_name: str, gender: Gender) -> str | None:
        for division in DivisionList:
            teams_page = TeamsPage(division)
            conferences = teams_page.get_conferences()

            for conference in conferences:
                schools = teams_page.get_schools_by_conference_name(conference.name, gender)
                for school in schools:
                    if school.name != target_school_name:
                        continue

                    if school.gender != gender:
                        continue

                    return school.ids.tds

        return None


def get_division_by_conference_name(conference_name: str) -> Division | None:
    for division in DivisionList:
        conferences = TeamsPage(division).get_conferences()

        for name, conference_data in conferences.items():
            if name == conference_name:
                return division

    return None


def get_schools_by_conference_name(conference_name: str, gender: Gender):
    for division in DivisionList:
        page = TeamsPage(division)

        tables = page.soup.find_all("table", class_=["table-striped", "tds-table"])

        for table in tables:
            schools = []

            caption_tag = table.find("caption")
            current_conference_name = get_text_from_anchor(caption_tag)

            if current_conference_name != conference_name:
                continue

            rows = table.find_all("tr")
            for row in rows:
                column = row.find("td")

                href = get_href_from_anchor(column)

                if string_to_gender(url_to_gender(href)) != gender:
                    continue

                school = School()
                school.gender = gender
                school.name = get_text_from_anchor(column)
                school.urls.tds = href
                school.ids.tds = get_identifier_from_url(school.urls.tds)

                schools.append(school)

            return schools

    return None


if __name__ == "__main__":
    data = []

    for division, url in TEAMS_URL.items():
        res = requests.get(url)

        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.content, "html.parser")

        tables = soup.find_all("table", class_=["table-striped", "tds-table"])

        for table in tables:
            caption_tag = table.find("caption")

            conference_name = get_text_from_anchor(caption_tag)
            conference_url = urljoin(PREFIX, get_href_from_anchor(caption_tag))

            parsed_url = urlparse(conference_url)
            conference_id = parse_qs(parsed_url.query)["conferenceId"][0]

            rows = table.find_all("tr")
            for row in rows:
                column = row.find("td")

                href = get_href_from_anchor(column)

                if href is None:
                    continue

                school_name = get_text_from_anchor(column)

                school_url = urljoin(PREFIX, href)
                school_id = get_identifier_from_url(school_url)

                if "/men/" in school_url:
                    gender = Gender.Male
                else:
                    gender = Gender.Female

                data.append({
                    "division": division,
                    "conference_name": conference_name,
                    "conference_url": conference_url,
                    "conference_id": conference_id,
                    "school_name": school_name,
                    "school_url": school_url,
                    "school_id": school_id,
                    "gender": gender
                })

    from pprint import pprint

    for item in data:
        pprint(item)

    # page = TeamsPage(Gender.Female, Division.DI)

    # conference = page.get_conference_by_name("West Coast")
    # print(conference)

    # conferences = page.get_conferences()
    # schools = page.get_schools_by_conference("West Coast")
    #
    # for school in schools:
    #     print(school)

    # clgid = TeamsPages().clgid_lookup(Gender.Female, "Santa Clara")
    #
    # print(clgid)

    # teams_page = TeamsPage(Division.DI)
    #
    # conference_names = teams_page.get_conference_names()
    #
    # conferences = teams_page.get_conferences()
    #
    # for name in conferences:
    #     container = conferences.get(name)
    #     conference = container.get("conference")
    #     schools = container.get("schools")
    #
    #     for school in schools:
    #         print(f"{conference.name} - {school.name} - {school.urls.tds}")

    # female_schools = get_schools_by_conference_name(Gender.Female, "West Coast")
    # male_schools = get_schools_by_conference_name(Gender.Male, "West Coast")
    #
    # for school in female_schools:
    #     print(f"{school.name} - {school.urls.tds}")

    # print(get_division_by_conference_name("Central Atlantic Conference"))

    # pages = TeamsPages()
    #
    # school_name = "South Carolina"
    # female_clgid = pages.clgid_lookup(Gender.Female, school_name)
    # male_clgid = pages.clgid_lookup(Gender.Male, school_name)
    #
    # print(school_name)
    # print(f"Men: {male_clgid}")
    # print(f"Women: {female_clgid}")
    #
    # print()
    #
    # print("ASUN: " + str(pages.division_by_conference_name("ASUN")))
    # print("West Coast: " + str(pages.division_by_conference_name("West Coast")))
    # print("Atlantic Coast: " + str(pages.division_by_conference_name("Atlantic Coast")))
    # print("Central Atlantic Conference: " + str(pages.division_by_conference_name("Central Atlantic Conference")))
    # print("American Southwest: " + str(pages.division_by_conference_name("American Southwest")))
    # print("Allegheny Mountain: " + str(pages.division_by_conference_name("Allegheny Mountain")))
    # print("Kentucky Intercollegiate: " + str(pages.division_by_conference_name("Kentucky Intercollegiate")))
    #
    #
    # print("\n\nSchools By Conference Name")
    # print("ASUN")
    # for school in pages.schools_by_conference_name(Gender.Female, "ASUN"):
    #     print(f"  {school}")
    #
    # print("\nWest Coast")
    # for school in pages.schools_by_conference_name(Gender.Female, "West Coast"):
    #     print(f"  {school}")
    #
    # print("\nSEC")
    # for school in pages.schools_by_conference_name(Gender.Female, "SEC"):
    #     print(f"  {school}")
    #
    # print("\nAtlantic Coast")
    # for school in pages.schools_by_conference_name(Gender.Female, "Atlantic Coast"):
    #     print(f"  {school}")
