from soccer_sdk_utils.tools import urljoin
from soccer_sdk_utils.division import Division

from topdrawersoccer_sdk.constants import PREFIX


POSITION = {
    "All": 0,
    "Goalkeeper": 1,
    "Defender": 2,
    "Midfielder": 6,
    "Forward": 5,
}

STATE = {
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

REGION = {
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

DIVISION_URL = {
    Division.DI: urljoin(PREFIX, "/college-soccer/college-conferences/di/divisionid-1"),
    Division.DII: urljoin(PREFIX, "/college-soccer/college-conferences/dii/divisionid-2"),
    Division.DIII: urljoin(PREFIX, "/college-soccer/college-conferences/diii/divisionid-3"),
    Division.NAIA: urljoin(PREFIX, "/college-soccer/college-conferences/naia/divisionid-4"),
    Division.NJCAA: urljoin(PREFIX, "/college-soccer/college-conferences/njcaa/divisionid-5")
}

TEAMS_URL = {
    Division.DI: urljoin(PREFIX, "/college/teams/?divisionName=di&divisionId=1"),
    Division.DII: urljoin(PREFIX, "/college/teams/?divisionName=dii&divisionId=2"),
    Division.DIII: urljoin(PREFIX, "/college/teams/?divisionName=diii&divisionId=3"),
    Division.NAIA: urljoin(PREFIX, "/college/teams/?divisionName=naia&divisionId=4"),
    Division.NJCAA: urljoin(PREFIX, "/college/teams/?divisionName=njcaa&divisionId=5")
}
