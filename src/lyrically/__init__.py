import requests


class Lyrically:
    """A class which contains methods used to retrieve and store song data."""

    def __init__(self) -> None:
        self.s = requests.Session()
