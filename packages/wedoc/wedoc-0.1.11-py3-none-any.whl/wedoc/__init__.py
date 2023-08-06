
from wedoc.api import document
from wedoc.api import spreadsheet
from wedoc.api.client import WedocClientBase


class WedocClient(WedocClientBase):
    doc = document.Document()
    wb = spreadsheet.Spreadsheet()

    def __init__(self, corpid, corpsecret) -> None:
        super().__init__(corpid, corpsecret)
