
from soccer_sdk_utils.tools import urljoin
from soccer_sdk_utils.gender import Gender
from soccer_sdk_utils.page import PageObject

from topdrawersoccer_sdk.model.club import ClubCommitmentStats
# from page.object import PageObject
from topdrawersoccer_sdk.constants import PREFIX


class ClubCommitmentsPage(PageObject):
    def __init__(self, gender: Gender, year: str, **kwargs):
        super().__init__(**kwargs)

        self.url = urljoin(PREFIX, "/commitments/club/")

        if gender == Gender.Male:
            self.url = urljoin(self.url, "/men")
        elif gender == Gender.Female:
            self.url = urljoin(self.url, "/women")
        else:
            raise ValueError(f"Unsupported gender {gender.name} !")

        self.url = urljoin(self.url, f"/{year}")

        self.load()

    def get_commitments(self):
        table = self.soup.find("table", class_=["table-striped"])

        if table is None:
            return []

        body = table.find("tbody")
        rows = body.find_all("tr")

        records = []
        for row in rows:
            cells = row.findChildren("td")

            record = ClubCommitmentStats()
            record.club = cells[0].text.strip()
            record.di = int(cells[1].text.strip())
            record.dii = int(cells[2].text.strip())
            record.diii = int(cells[3].text.strip())
            record.naia = int(cells[4].text.strip())
            record.njcaa = int(cells[5].text.strip())
            record.total = int(cells[6].text.strip())

            records.append(record)

        records = sorted(records, key=lambda x: x.di, reverse=True)

        return records


if __name__ == "__main__":
    records = ClubCommitmentsPage(Gender.Female, "2024").get_commitments()

    for record in records:
        print(record)
