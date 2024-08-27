import requests


class Lyrically:
    """A class which contains methods used to retrieve and store song data."""

    def __init__(self) -> None:
        self.BASE_URL = "https://www.azlyrics.com/"
        self.s = requests.Session()

    def get_artist_data(self, artist_name: str):
        """Retrieve links of an artist's full catalouge."""

        artist_name = artist_name.lower().replace(" ", "")
        artist_page_url = self.BASE_URL + f"{artist_name[0]}/{artist_name}.html"

        r = self.s.get(artist_page_url)
        print(r.status_code)
        print(r.text)
