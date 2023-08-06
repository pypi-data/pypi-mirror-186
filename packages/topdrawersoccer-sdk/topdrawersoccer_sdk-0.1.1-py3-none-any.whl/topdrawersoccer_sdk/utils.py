PREFIX = "https://www.topdrawersoccer.com"

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

REGION_MAPPING = {
    "All": 0,
    "Florida": 10,
    "Great Lakes": 7,
    "Heartland": 5,
    "International": 17,
    "Mid Atlantic": 100,
    "Midwest": 6,
    "New Jersey": 14,
    "New York": 15,
    "Northeast": 16,
    "Northern California & Hawaii": 2,
    "Pacific Northwest": 3,
    "Pennsylvania": 13,
    "Rocky Mountains & Southwest": 4,
    "South": 9,
    "South Atlantic": 11,
    "Southern California": 1,
    "Texas": 8,
}


def get_identifier_from_url(url):
    if url is None:
        return None

    url = url.strip()
    if len(url) == 0:
        return None

    tokens = url.split("/")
    last_segment = tokens[-1]

    if "-" not in last_segment:
        return None

    tokens = last_segment.split("-")

    return tokens[-1]


def url_to_gender(url: str):
    if url is None:
        return "All"

    url = url.strip()
    if len(url) == 0:
        return "All"

    if "/men" in url:
        return "Male"

    if "/women":
        return "Female"

    return "All"
