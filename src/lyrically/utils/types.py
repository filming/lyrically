from typing import TypedDict, List


class SongRef(TypedDict):
    """Represent a reference to a song, meaning its title and a URL to its lyrics."""

    title: str
    link: str


class Song(TypedDict):
    """Represent a song with its title and lyrics."""

    title: str
    lyrics = List[str]


class Album(TypedDict):
    """Represent an album with its title and song references."""

    title: str
    songs: List[SongRef]
