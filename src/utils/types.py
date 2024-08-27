from typing import TypedDict, List


class Song(TypedDict):
    title: str
    link: str


class Album(TypedDict):
    title: str
    songs: List[Song]
