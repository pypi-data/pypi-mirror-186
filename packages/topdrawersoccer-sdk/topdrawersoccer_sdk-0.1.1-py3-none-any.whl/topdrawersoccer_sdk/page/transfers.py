from soccer_sdk_utils.model.transfer import Transfer
from soccer_sdk_utils.page import PageObject

from topdrawersoccer_sdk.utils import PREFIX

from soccer_sdk_utils.tools import urljoin, get_href_from_anchor, get_text_from_anchor


def _get_transfer_position(cell):
    caption = cell.text.strip()
    if caption == "Player":
        return None

    if "\xa0" in caption:
        return caption.split("\xa0")[0].strip()

    return caption.split(" ")[0].strip()


def _get_transfer_name(cell):
    caption = cell.text.strip()
    if caption == "Player":
        return None

    if "\xa0" in caption:
        return caption.split("\xa0")[1].strip()

    return " ".join(caption.split(" ")[1:]).strip()


def _get_transfer(row):
    try:
        cells = row.find_all("td")

        name = _get_transfer_name(cells[0])

        if name is None or len(name) == 0:
            return None

        transfer = Transfer()
        transfer.name = name
        transfer.position = _get_transfer_position(cells[0])

        if transfer.position == "F":
            transfer.position = "Forward"
        elif transfer.position == "GK":
            transfer.position = "Goalkeeper"
        elif transfer.position == "M":
            transfer.position = "Midfielder"
        elif transfer.position == "D":
            transfer.position = "Defender"
        elif transfer.position == "M/F":
            transfer.position = "Midfielder/Forward"
        elif transfer.position == "F/D":
            transfer.position = "Forward/Defender"
        elif transfer.position == "M/D":
            transfer.position = "Midfielder/Defender"

        transfer.url = get_href_from_anchor(cells[0])

        if transfer.url is not None:
            transfer.url = urljoin(PREFIX, transfer.url)

        if len(cells) > 1:
            transfer.former_school_name = get_text_from_anchor(cells[1])
            transfer.former_school_url = get_href_from_anchor(cells[1])

            if transfer.former_school_url is not None:
                transfer.former_school_url = urljoin(PREFIX, transfer.former_school_url)

        if len(cells) > 2:
            transfer.new_school_name = get_text_from_anchor(cells[2])
            transfer.new_school_url = get_href_from_anchor(cells[2])

            if transfer.new_school_url is not None:
                transfer.new_school_url = urljoin(PREFIX, transfer.new_school_url)

        return transfer
    except Exception as err:
        print(row.text)
        print(err)


class TransferTrackerPage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "https://www.topdrawersoccer.com/college-soccer-articles/2022-womens-di-transfer-tracker_aid50187"

        self.load()

    def get_transfers(self):
        rows = self.soup.find_all("tr")

        transfers = []
        for row in rows:
            player = _get_transfer(row)
            if player is None:
                continue

            transfers.append(player)

        return transfers


if __name__ == "__main__":
    page = TransferTrackerPage()
    transfers = page.get_transfers()

    for transfer in transfers:
        print(transfer)
