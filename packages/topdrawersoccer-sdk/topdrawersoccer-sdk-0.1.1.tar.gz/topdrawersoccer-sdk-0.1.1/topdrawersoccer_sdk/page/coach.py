import bs4

from soccer_sdk_utils.gender import Gender
from soccer_sdk_utils.model.coach import CoachingChange
from soccer_sdk_utils.page import PageObject
from soccer_sdk_utils.tools import urljoin
from soccer_sdk_utils.tools import get_href_from_anchor
from soccer_sdk_utils.tools import get_text_from_anchor

from topdrawersoccer_sdk.constants import PREFIX
from topdrawersoccer_sdk.utils import get_identifier_from_url


class CoachingChangePage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = urljoin(
            PREFIX,
            "/college-soccer-articles/tracking-division-i-coaching-changes_aid50078",
        )

        self.load()

    def get_coaching_changes(self, gender: Gender):
        grand_parent = self.soup.find("div", class_=["col-sm-11"])
        parent = grand_parent.find("div", class_=["col"])

        if gender == Gender.Male:
            target_title = "MEN'S"
        elif gender == Gender.Female:
            target_title = "WOMEN'S"
        else:
            raise ValueError(f"Unsupported gender {gender.name}!")

        found_it = False
        for child in parent.children:
            if type(child) is not bs4.element.Tag:
                continue

            if child.name not in ["p", "table"]:
                continue

            if child.name == "p" and child.text.strip() == target_title:
                found_it = True
            elif child.name == "table" and found_it:
                changes = []

                rows = child.findChildren("tr")
                for row in rows:
                    cells = row.findChildren("td")

                    program = get_text_from_anchor(cells[0])

                    if program is None:
                        continue

                    if program == "Program":
                        continue

                    if len(program) == 0:
                        continue

                    change = CoachingChange()

                    change.program = get_text_from_anchor(cells[0])
                    change.program_url = get_href_from_anchor(cells[0])
                    change.old_coach = get_text_from_anchor(cells[1])
                    change.old_coach_url = get_href_from_anchor(cells[1])
                    change.new_coach = get_text_from_anchor(cells[2])
                    change.new_coach_url = get_href_from_anchor(cells[2])

                    change.clgid = get_identifier_from_url(change.program_url)

                    change.program_url = urljoin(PREFIX, change.program_url)

                    changes.append(change)

                return changes

        return None


if __name__ == "__main__":
    page = CoachingChangePage()
    changes = page.get_coaching_changes(Gender.Female)

    for change in changes:
        print(change)
