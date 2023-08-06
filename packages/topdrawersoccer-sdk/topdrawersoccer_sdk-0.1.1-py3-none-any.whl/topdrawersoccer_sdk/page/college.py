import re

from soccer_sdk_utils.gender import Gender
from soccer_sdk_utils.tools import slugify, urljoin
from soccer_sdk_utils.page import PageObject
from topdrawersoccer_sdk.page.team import TeamsPages
from topdrawersoccer_sdk.constants import PREFIX
from soccer_sdk_utils.tools import get_href_from_anchor, get_text_from_anchor


class CollegeDetailsPage(PageObject):
    def __init__(self, gender: Gender, name: str, **kwargs):
        super().__init__(**kwargs)

        self.gender = gender
        self.name = name
        self.clgid = kwargs.get("clgid", None)

        if self.clgid is None:
            self.clgid = TeamsPages().clgid_lookup(gender, name)

        self.url = urljoin(PREFIX, "/college-soccer/college-soccer-details")

        if gender == Gender.Male:
            self.url = urljoin(self.url, "/men")
        elif gender == Gender.Female:
            self.url = urljoin(self.url, "/women")
        else:
            raise ValueError(f"Unsupported gender {gender.name}!")

        self.url = urljoin(self.url, f"/{slugify(name)}")
        self.url = urljoin(self.url, f"/clgid-{self.clgid}")

        self.load()

    def get_details(self):
        header = self.soup.find("th", text=re.compile(r"Program Information"))
        table = header.parent.parent.parent
        body = table.find("tbody")
        rows = body.findChildren("tr")

        details = {}
        for row in rows:
            cells = row.findChildren("td")
            attribute = cells[0].text.strip()

            if len(attribute) > 0 and attribute[-1] == ":":
                attribute = attribute[:-1]  # Omit the trailing colon.

            attribute = attribute.strip()  # Strip one more time just in case.

            cell = cells[1]
            if attribute == "Conference":
                details["conference"] = get_text_from_anchor(cell)
                details["conferenceUrl"] = urljoin(PREFIX, get_href_from_anchor(cell))
            elif attribute == "Nickname":
                details["nickname"] = cell.text.strip()
            elif attribute == "State":
                details["state"] = cell.text.strip()
            elif attribute == "City":
                details["city"] = cell.text.strip()
            elif attribute == "Enrollment":
                details["enrollment"] = int(cell.text.strip())
            elif attribute == "Head Coach":
                details["coach"] = cell.text.strip()
            elif attribute == "Phone Number":
                details["phone"] = cell.text.strip()
            else:
                # Do nothing for now
                pass

        return details


if __name__ == "__main__":
    details = CollegeDetailsPage(Gender.Female, "University of North Carolina").get_details()

    for key, value in details.items():
        print(f"{key}: {value}")
