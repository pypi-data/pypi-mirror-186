from common.gender import Gender
from common.model.player import Player
from common.utils import slugify, urljoin
from page.object import PageObject
from page.tds.utils import PREFIX
from page.utils import get_href_from_anchor, get_text_from_anchor

POSITION_MAPPING = {
    "All": 0,
    "Goalkeeper": 1,
    "Defender": 2,
    "Midfielder": 6,
    "Forward": 5,
}

STATE_MAPPING = {
    "All": 0,
    "Alabama": 1,
    "Alaska": 2,
    "Arizona": 3,
    "Arkansas": 4,
    "California": 5,
    "Colorado": 6,
    "Connecticut": 7,
    "Delaware": 8,
    "District of Columbia": 9,
    "Florida": 10,
    "Georgia": 11,
    "Hawaii": 12,
    "Idaho": 13,
    "Illinois": 14,
    "Indiana": 15,
    "International": 99,
    "Iowa": 16,
    "Kansas": 17,
    "Kentucky": 18,
    "Louisiana": 19,
    "Maine": 20,
    "Maryland": 21,
    "Massachusetts": 22,
    "Michigan": 23,
    "Minnesota": 24,
    "Mississippi": 25,
    "Missouri": 26,
    "Montana": 27,
    "Nebraska": 28,
    "Nevada": 29,
    "New Hampshire": 30,
    "New Jersey": 31,
    "New Mexico": 32,
    "New York": 33,
    "North Carolina": 34,
    "North Dakota": 35,
    "Ohio": 36,
    "Oklahoma": 37,
    "Oregon": 38,
    "Pennsylvania": 39,
    "Rhode Island": 40,
    "South Carolina": 41,
    "South Dakota": 42,
    "Tennessee": 43,
    "Texas": 44,
    "Utah": 45,
    "Vermont": 46,
    "Virginia": 47,
    "Washington": 48,
    "West Virginia": 49,
    "Wisconsin": 50,
    "Wyoming": 51,
}


def _extract_club(el):
    buffer = el.find("div", class_="ml-2").text.strip()
    tokens = buffer.split("\t\t\t\t")

    if len(tokens) > 1:
        target = tokens[1].strip()
        pieces = target.split("/")

        if len(pieces) >= 1:
            return pieces[0]
    else:
        tokens = buffer.split("\n\n\n\n")

        target = tokens[1].strip()

        if target.startswith("N/A"):
            return None

        pieces = target.split("/")

        if len(pieces) >= 1:
            return pieces[0]

    return None


def _extract_high_school(el):
    buffer = el.find("div", class_="ml-2").text.strip()
    target = buffer.split("\t\t\t\t")[1].strip()
    pieces = target.split("/")

    if len(pieces) == 1:
        high_school = None
    elif len(pieces) == 2:
        high_school = pieces[1]
    else:
        high_school = None

    return high_school


def _extract_image_url(el):
    image = el.find("img", class_="imageProfile")

    if image is not None:
        return PREFIX + image["src"]

    return None


def _extract_rating(el):
    rating = el.find("span", class_="rating")["style"]
    rating = int(rating.split(":")[-1].split("%")[0]) // 20

    if rating > 0:
        rating = str(rating) + " star"
    else:
        rating = "Not Rated"

    return rating


def _extract_commitment(el):
    commitment_span = el.find("span", class_="text-uppercase")

    if commitment_span is not None:
        anchor = commitment_span.find("a")
        return anchor.text.strip()

    return None


def _extract_commitment_url(el):
    commitment_span = el.find("span", class_="text-uppercase")

    if commitment_span is not None:
        anchor = commitment_span.find("a")
        return urljoin(PREFIX, anchor.get("href"))

    return None


def _extract_player_id(el):
    name_anchor = el.find("a", class_="bd")

    return name_anchor["href"].split("/")[-1].split("-")[-1]


def _extract_player_name(el):
    name_anchor = el.find("a", class_="bd")

    return name_anchor.text.strip()


def _extract_player_url(el):
    name_anchor = el.find("a", class_="bd")

    return urljoin(PREFIX, name_anchor.get("href"))


def _extract_position(el):
    position = el.find("div", class_="col-position")
    if position is None:
        return None

    position = position.text.strip()
    upper_position = position.upper()

    if upper_position in ["M", "MF"]:
        position = "Midfielder"
    elif upper_position in ["F", "FW"]:
        position = "Forward"
    elif upper_position in ["D", "DF"]:
        position = "Defender"
    elif upper_position in ["KEEPER", "GK"]:
        position = "Goalkeeper"

    return position


def _extract_year(el):
    year = el.find("div", class_="col-grad")
    if year is None:
        return None

    return year.text.strip()


def _extract_state(el):
    state = el.find("div", class_="col-state")
    if state is None:
        return None

    return state.text.strip()


def _extract_first_name(el):
    name = _extract_player_name(el)

    tokens = name.split(" ")

    if len(tokens) == 0:
        return None

    return tokens[0]


def _extract_last_name(el):
    name = _extract_player_name(el)

    tokens = name.split(" ")

    if len(tokens) <= 1:
        return None

    return tokens[-1]


def _extract_slug(el):
    name = _extract_player_name(el)

    return slugify(name)


class ClubPlayerPage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        url = kwargs.get("url")

        if url is None:
            self.slug = kwargs.get("slug")
            self.pid = kwargs.get("pid")

            if self.slug is None:
                self.name = kwargs.get("name")

                if self.name is not None:
                    self.slug = slugify(self.name)

            if self.slug is None:
                raise ValueError("Either slug or name must be provided")

            if self.pid is None:
                raise ValueError("pid must be provided")

            self.url = f"https://www.topdrawersoccer.com/club-player-profile/{self.slug}/pid-{self.pid}"
        else:
            self.url = url

        self.load()

    @property
    def profile_grid(self):
        details = {}

        container = self.soup.find("ul", class_=["profile_grid"])

        if container is not None:
            items = container.find_all("li")
            for item in items:
                lvalue, rvalue = item.text.strip().split(":")

                lvalue = lvalue.strip()
                rvalue = rvalue.strip()

                if lvalue == "Club":
                    details["club"] = rvalue
                elif lvalue == "Team Name":
                    details["team"] = rvalue
                elif lvalue == "Jersey Number":
                    details["jerseyNumber"] = rvalue
                elif lvalue == "High School":
                    details["highSchool"] = rvalue
                elif lvalue == "Region":
                    details["region"] = rvalue
                else:
                    print(f"Unknown lvalue '{lvalue}' on player detail page.")

        return details

    @property
    def club(self):
        return self.profile_grid.get("club")

    @property
    def team_name(self):
        return self.profile_grid.get("team")

    @property
    def high_school(self):
        return self.profile_grid.get("highSchool")

    @property
    def region(self):
        return self.profile_grid.get("region")

    @property
    def rating(self) -> str | None:
        span = self.soup.find("span", class_=["rating"])

        if span is None:
            return None

        result = span["style"]
        result = int(result.split(":")[-1].split("%")[0]) // 20

        if result > 0:
            result = str(result) + " star"
        else:
            result = "Not Rated"

        return result

    @property
    def position(self) -> str | None:
        div = self.soup.find("div", class_=["player-position"])

        if div is None:
            return None

        buffer = div.text.strip()
        tokens = buffer.split("-")
        result = tokens[0].strip()

        return result

    @property
    def year(self) -> str | None:
        div = self.soup.find("div", class_=["player-position"])

        if div is None:
            return None

        buffer = div.text.strip()
        tokens = buffer.split("-")

        if len(tokens) > 1:
            result = tokens[1].strip()
            tokens = result.split(" ")
            result = tokens[-1]
        else:
            result = None

        return result

    @property
    def commitment(self) -> str | None:
        div = self.soup.find("div", class_=["player-position"])

        if div is None:
            return None

        return get_text_from_anchor(div)

    @property
    def is_professional(self) -> bool:
        div = self.soup.find("div", class_=["player-position"])

        if div is None:
            return False

        span = div.find("span", class_=["badge", "badge-success"])

        if span is None:
            return False

        text = span.text.strip().lower()

        return text == "professional"

    @property
    def commitment_url(self) -> str | None:
        div = self.soup.find("div", class_=["player-position"])

        if div is None:
            return None

        href = get_href_from_anchor(div)

        if href is None:
            return None

        return urljoin(PREFIX, href)

    def get_player(self, **kwargs) -> Player:
        tokens = self.name.split(" ")

        player = Player()
        player.first_name = tokens[0].strip()
        player.last_name = tokens[1].strip()
        player.club = self.club
        player.state = None
        player.position = self.position

        player.add_property("tds_id", str(self.pid))
        player.add_property("tds_region", self.region)
        player.add_property("tds_rating", self.rating)
        player.add_property("tds_pro", str(self.is_professional))

        player.add_property("jersey_number", self.profile_grid.get("jerseyNumber"))
        player.add_property("grad_year", self.year)
        player.add_property("commitment", self.commitment)
        player.add_property("commitment_url", self.commitment_url)
        player.add_property("team", self.team_name)
        player.add_property("high_school", self.high_school)

        return player


def _extract_player(el, gender: Gender) -> Player:
    new_player = Player()
    new_player.gender = gender.name if gender != Gender.All else None
    new_player.first_name = _extract_first_name(el)
    new_player.last_name = _extract_last_name(el)
    new_player.club = _extract_club(el)
    new_player.state = _extract_state(el)
    new_player.position = _extract_position(el)

    new_player.add_property("slug", _extract_slug(el))
    new_player.add_property("tds_club", _extract_club(el))
    new_player.add_property("grad_year", _extract_year(el))
    new_player.add_property("high_school", _extract_high_school(el))
    new_player.add_property("tds_rating", _extract_rating(el))
    new_player.add_property("tds_id", _extract_player_id(el))
    new_player.add_property("tds_url", _extract_player_url(el))
    new_player.add_property("tds_image_url", _extract_image_url(el))
    new_player.add_property("commitment", _extract_commitment(el))
    new_player.add_property("commitment_url", _extract_commitment_url(el))

    return new_player


class SearchPage(PageObject):
    def __init__(
        self, gender: Gender, position: str, year: str, state: str, page: int, **kwargs
    ):
        super().__init__(**kwargs)

        self.gender = gender
        self.position = position
        self.year = year
        self.state = state
        self.page = page

        suffix = "&genderId=" + self.gender_id
        suffix += "&positionId=" + self.position_id
        suffix += "&graduationYear=" + self.year
        suffix += "&regionId=" + self.region_id
        suffix += "&countyId=" + self.county_id
        suffix += "&pageNo=" + str(page)
        suffix += "&area=clubplayer&sortColumns=0&sortDirections=1&search=1"

        self.url = f"https://www.topdrawersoccer.com/search/?query={suffix}"

        self.load()

    @property
    def gender_id(self) -> str:
        if self.gender == Gender.Male:
            return "m"
        elif self.gender == Gender.Female:
            return "f"
        else:
            raise ValueError(f"Unsupported gender {self.gender}!")

    @property
    def position_id(self) -> str:
        return str(POSITION_MAPPING.get(self.position))

    @property
    def region_id(self) -> str:
        return "0"

    @property
    def county_id(self) -> str:
        return str(STATE_MAPPING.get(self.state))

    def get_pagination(self) -> list[int]:
        pagination = self.soup.find("ul", class_=["pagination"])

        if pagination is None:
            return []

        pages = []

        list_items = pagination.find_all("li", class_=["page-item"])
        for list_item in list_items:
            text = list_item.text.strip()

            if text in ["Previous", "1", "Next"]:
                continue

            pages.append(int(text))

        return pages

    def get_players(self) -> list[Player]:
        items = self.soup.find_all("div", class_=["item"])

        players = []
        for item in items:
            players.append(_extract_player(item, self.gender))

        return players


def search(
    gender: Gender, year: str, state: str, position: str = "All"
) -> list[Player]:
    page = SearchPage(gender=gender, position=position, year=year, state=state, page=0)
    pagination = page.get_pagination()

    players = page.get_players()
    for page_number in pagination:
        page = SearchPage(
            gender=gender, position=position, year=year, state=state, page=page_number
        )

        players.extend(page.get_players())

    return players


if __name__ == "__main__":
    player = ClubPlayerPage(name="Jordyn Crosby", pid="109869").get_player()
    print(player)
