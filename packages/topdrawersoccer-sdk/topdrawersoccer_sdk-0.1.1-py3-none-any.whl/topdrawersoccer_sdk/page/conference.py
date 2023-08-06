from soccer_sdk_utils.gender import Gender
from soccer_sdk_utils.model.player import Player
from soccer_sdk_utils.model.values import Values
from soccer_sdk_utils.model.school import School
from soccer_sdk_utils.model.conference import Conference
from soccer_sdk_utils.page import PageObject
from soccer_sdk_utils.tools import urljoin, slugify, get_href_from_anchor, get_text_from_anchor

from soccer_sdk_utils.dao.club import ClubDAO

from soccer_sdk_utils.division import Division

from topdrawersoccer_sdk.constants import PREFIX
from topdrawersoccer_sdk.page.team import TeamsPage
from topdrawersoccer_sdk.utils import get_identifier_from_url
from topdrawersoccer_sdk import mapping


class ConferenceCommitmentsPage(PageObject):
    def __init__(self, gender: Gender,
                 division: Division,
                 conference_name: str,
                 **kwargs):

        super().__init__(**kwargs)

        conferences_page = ConferencesPage(division)
        conference = conferences_page.get_conference_by_name(conference_name, gender)

        self.gender = gender
        self.division = division

        self.url = urljoin(PREFIX, "/college-soccer/college-conferences/conference-details/")

        if gender == Gender.Male:
            self.url = urljoin(self.url, "/men")
        else:
            self.url = urljoin(self.url, "/women")

        self.url = urljoin(self.url, f"{conference.slug}")
        self.url = urljoin(self.url, f"cfid-{conference.ids.tds}")
        self.url = urljoin(self.url, "tab-commitments")

        self.load()

    def get_commitments(self, year: str = None, lookup_league: bool = False) -> list[Player]:
        """Returns a list of players who have committed to a school in the conference"""
        tables = self.soup.find_all(
            "table", class_=["table-striped", "tds-table", "female"]
        )

        body = None
        for table in tables:
            header = table.find("thead", class_="female")
            if header is not None:
                body = table.find("tbody")

        if body is None:
            return []

        players = []
        rows = body.find_all("tr")
        current_school = None
        for row in rows:
            columns = row.find_all("td")

            if len(columns) == 1:
                current_school = columns[0].text.strip()
                continue

            grad_year = columns[1].text.strip()

            if year is not None and grad_year != year:
                continue

            name = get_text_from_anchor(columns[0])

            player = Player()
            player.gender = self.gender
            player.first_name = name.split(" ")[0] if name is not None else None
            player.last_name = name.split(" ")[-1] if name is not None else None
            player.club = columns[5].text.strip().replace("  ", " ")
            player.state = columns[4].text.strip()
            player.position = columns[2].text.strip()

            href = get_href_from_anchor(columns[0])
            if href is not None:
                url = urljoin(PREFIX, href)
                player.add_property("tds_url", url)

            player.add_property("city", columns[3].text.strip())
            player.add_property("grad_year", grad_year)
            player.add_property("commitment", current_school)

            if lookup_league:
                player.add_property("league", ClubDAO().lookup_league(player.club))

            players.append(player)

        return players


class SchoolCommitmentsPage(PageObject):
    def __init__(self, gender: Gender, name: str, **kwargs):
        super().__init__(**kwargs)

        self.gender = gender
        self.name = name
        self.clgid = kwargs.get("clgid", None)

        if self.clgid is None:
            self.clgid = TeamsPage(Division.DI).get_clgid_by_name(gender, name)

        self.url = urljoin(PREFIX, "/college-soccer/college-soccer-details")

        if gender == Gender.Male:
            self.url = urljoin(self.url, "/men")
        elif gender == Gender.Female:
            self.url = urljoin(self.url, "/women")
        else:
            raise ValueError(f"Unsupported gender {gender.name}!")

        self.url = urljoin(self.url, f"/{slugify(name)}")
        self.url = urljoin(self.url, f"/clgid-{self.clgid}")
        self.url = urljoin(self.url, "/tab-commitments")

        self.load()

    def get_commitments(self, year: str = None, lookup_league: bool = False) -> list[Player]:
        """
        Note: The players leagues really need to be set properly before this method returns.
        OMC
        :return:
        """
        tables = self.soup.find_all(
            "table", class_=["table-striped", "tds-table", "female"]
        )

        body = None
        for table in tables:
            header = table.find("thead", class_="female")
            if header is not None:
                body = table.find("tbody")

        if body is None:
            return []

        players = []
        rows = body.find_all("tr")
        for row in rows:
            columns = row.find_all("td")

            if len(columns) == 1:
                continue

            grad_year = columns[1].text.strip()

            if year is not None and grad_year != year:
                continue

            name = get_text_from_anchor(columns[0])

            player = Player()
            player.gender = self.gender
            player.first_name = name.split(" ")[0] if name is not None else None
            player.last_name = name.split(" ")[-1] if name is not None else None
            player.club = columns[5].text.strip().replace("  ", " ")
            player.state = columns[4].text.strip()
            player.position = columns[2].text.strip()

            href = get_href_from_anchor(columns[0])
            if href is not None:
                url = urljoin(PREFIX, href)
                player.add_property("tds_url", url)

            player.add_property("city", columns[3].text.strip())
            player.add_property("grad_year", grad_year)

            if lookup_league:
                player.add_property("league", ClubDAO().lookup_league(player.club))

            players.append(player)

        return players


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
    def __init__(self, division: Division, **kwargs):
        super().__init__(**kwargs)

        self.division = division
        self.url = mapping.DIVISION_URL.get(self.division)

        self.load()

    @property
    def division(self) -> Division:
        return self._division

    @division.setter
    def division(self, value: Division):
        self._division = value

    def get_conference_by_name(self, target_name: str | None, gender: Gender) -> Conference | None:
        """Returns a conference by name"""

        if target_name is None:
            return None

        target_name = target_name.strip()
        target_name = target_name.lower()

        columns = self.soup.find_all("div", class_="col-lg-6")

        for column in columns:
            heading = column.find("div", class_=["heading-rectangle"])

            if heading is None:
                continue

            heading = heading.text.strip()

            if gender == Gender.Male and "Men's" not in heading:
                continue

            if gender == Gender.Female and "Women's" not in heading:
                continue

            table = column.find("table", class_=["table_stripped", "tds_table"])
            cells = table.find_all("td")

            for cell in cells:
                anchor = cell.find("a")
                name = get_text_from_anchor(anchor)

                if name is None:
                    continue

                if name.strip().lower() != target_name:
                    continue

                href = get_href_from_anchor(anchor)

                conference = Conference()

                conference.name = get_text_from_anchor(anchor)
                conference.division = self.division
                conference.gender = gender

                conference.ids = Values()
                conference.urls = Values()

                conference.urls.tds = urljoin(PREFIX, href)
                conference.ids.tds = str(get_identifier_from_url(href))

                return conference

        return None

    def get_conference_by_id(self, target_id: str, gender: Gender) -> Conference | None:
        if target_id is None:
            return None

        target_id = target_id.strip()

        columns = self.soup.find_all("div", class_="col-lg-6")

        for column in columns:
            heading = column.find("div", class_=["heading-rectangle"])

            if heading is None:
                continue

            heading = heading.text.strip()

            if gender == Gender.Male and "Men's" not in heading:
                continue

            if gender == Gender.Female and "Women's" not in heading:
                continue

            table = column.find("table", class_=["table_stripped", "tds_table"])
            cells = table.find_all("td")

            for cell in cells:
                anchor = cell.find("a")
                href = get_href_from_anchor(anchor)
                id = str(get_identifier_from_url(href))

                if id is None:
                    continue

                if id != target_id:
                    continue

                name = get_text_from_anchor(anchor)

                if name is None:
                    continue

                conference = Conference()

                conference.name = get_text_from_anchor(anchor)
                conference.division = self.division
                conference.gender = gender

                conference.ids = Values()
                conference.urls = Values()

                conference.urls.tds = urljoin(PREFIX, href)
                conference.ids.tds = str(get_identifier_from_url(href))

                return conference

        return None

    def has_conference(self, name: str, gender: Gender) -> bool:
        """Returns True if the conference exists"""
        conference = self.get_conference_by_name(name, gender)

        return conference is not None

    def get_conference_names(self, gender: Gender):
        """Returns a list of conference names"""
        names = []

        columns = self.soup.find_all("div", class_="col-lg-6")

        for column in columns:
            heading = column.find("div", class_=["heading-rectangle"])

            if heading is None:
                continue

            heading = heading.text.strip()

            if gender == Gender.Male and "Men's" not in heading:
                continue

            if gender == Gender.Female and "Women's" not in heading:
                continue

            table = column.find("table", class_=["table_stripped", "tds_table"])
            cells = table.find_all("td")

            for cell in cells:
                anchor = cell.find("a")
                name = get_text_from_anchor(anchor)

                names.append(name)

        names.sort()

        return names

    def get_conferences(self, gender: Gender):
        conferences = []

        columns = self.soup.find_all("div", class_="col-lg-6")

        for column in columns:
            heading = column.find("div", class_=["heading-rectangle"])

            if heading is None:
                continue

            heading = heading.text.strip()

            if gender == Gender.Male and "Men's" not in heading:
                continue

            if gender == Gender.Female and "Women's" not in heading:
                continue

            table = column.find("table", class_=["table_stripped", "tds_table"])
            cells = table.find_all("td")

            for cell in cells:
                anchor = cell.find("a")
                href = get_href_from_anchor(anchor)

                conference = Conference()

                conference.name = get_text_from_anchor(anchor)
                conference.division = self.division
                conference.gender = gender

                conference.ids = Values()
                conference.urls = Values()

                conference.urls.tds = urljoin(PREFIX, href)
                conference.ids.tds = str(get_identifier_from_url(href))

                conferences.append(conference)

        return conferences

    @staticmethod
    def get_division_by_conference_name(name: str, gender: Gender) -> Division | None:
        for division in Division:
            if division == Division.All:
                continue

            page = ConferencesPage(division)
            if page.has_conference(name, gender):
                return division

        return None


if __name__ == "__main__":
    import sys
    from os import path
    from dotenv import load_dotenv

    load_dotenv(path.join(sys.path[1], ".env"))

    print()
    print("West Cost Conference Commitments")
    page = ConferenceCommitmentsPage(Gender.Female, Division.DI, "West Coast")

    players = page.get_commitments()

    for player in players:
        print(player)

    print()
    print("Santa Clara Commitments")
    page = SchoolCommitmentsPage(Gender.Female, "Santa Clara", clgid=474)

    players = page.get_commitments_by_year("2023")

    for player in players:
        print(player)
