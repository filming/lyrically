import requests
from bs4 import BeautifulSoup

from ..utils.types import Album, List, Song


class Lyrically:
    """A class which contains methods used to retrieve and store song data."""

    def __init__(self) -> None:
        self.BASE_URL = "https://www.azlyrics.com"
        self.s = requests.Session()

    def get_artist_discography(self, artist_name: str) -> List[Album]:
        """Retrieve the album titles and song information of an artist."""

        artist_name = artist_name.lower().replace(" ", "")
        artist_page_url = self.BASE_URL + f"/{artist_name[0]}/{artist_name}.html"

        r = self.s.get(artist_page_url)

        discography = []
        curr_album = {
            "title": None,
            "songs": [],
        }

        soup = BeautifulSoup(r.text, "html.parser")
        album_container = soup.find(id="listAlbum")
        album_container_contents = album_container.findAll("div")

        for curr_div in album_container_contents:

            if curr_div.has_attr("class"):
                curr_div_classes = curr_div.get("class")

                if "album" in curr_div_classes or "listalbum-item" in curr_div_classes:

                    if "album" in curr_div_classes:
                        # store currently stored album data before moving onto next
                        if curr_album["title"] != None:
                            discography.append(curr_album)

                            curr_album = {
                                "title": None,
                                "songs": [],
                            }

                        album_title = curr_div.find("b").text

                        if album_title == "other songs:":
                            curr_album["title"] = album_title[:-1]

                        else:
                            curr_album["title"] = album_title[1:-1]

                    else:
                        curr_song_data = curr_div.find("a")
                        curr_song = {
                            "title": curr_song_data.text,
                            "link": self.BASE_URL + curr_song_data.get("href"),
                        }

                        curr_album["songs"].append(curr_song)

        # push the remaining songs into the albums list
        discography.append(curr_album)

        return discography

    def get_song_lyrics(self, song_url: str) -> Song:
        """Retrieve the song lyrics of a specific song."""

        song = {"title": None, "lyrics": []}

        r = self.s.get(song_url)
        soup = BeautifulSoup(r.text, "html.parser")

        content_container = soup.find("div", class_="col-xs-12 col-lg-8 text-center")

        # Get the song title
        bold_elements = content_container.findAll("b")

        for curr_bold_element in bold_elements:

            if curr_bold_element.parent.has_attr("class"):

                class_string = " ".join(curr_bold_element.parent.get("class"))

                if class_string == "col-xs-12 col-lg-8 text-center":
                    song["title"] = curr_bold_element.text[1:-1]

        # Get the song lyrics
        lyric_container = content_container.find("div", class_="")

        lyrics = lyric_container.text.replace("\r", "")
        lyric_lines = lyrics.split("\n")

        sanitized_lyric_lines = []

        for curr_line in lyric_lines:
            if curr_line:
                sanitized_lyric_lines.append(curr_line)

        song["lyrics"] = sanitized_lyric_lines

        return song
