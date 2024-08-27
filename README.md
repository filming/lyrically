# Lyrically

Lyrically is a Python-based lyric scraper for obtaining complete artist discographies.

## Description

Lyrically is your solution for effortlessly collecting and organizing the complete lyrical works of your favorite artists.  Build a comprehensive library, fuel your music analysis, or simply enjoy having all the words at your fingertips.

## Getting Started

### Dependencies

* Python
* requests
* beautifulsoup4

### Installing

* Python can be downloaded from [here](https://www.python.org/).
* Install dependencies using `pip install -r requirements.txt` stored in the src directory.

### Executing program

* Creating an instance of Lyrically
```
from lyrically import Lyrically

lyrically = Lyrically()

```

* Getting an artist's lyrics
```
from lyrically import Lyrically

lyrically = Lyrically()

artist_name = "JuStIn BiEbEr"
discography = lyrically.get_artist_discography(artist_name)

lyrics = []

for song_ref in discography["songs"]:
    curr_song_lyrics = lyrically.get_song_lyrics(song_ref["link"])
    lyrics.append(curr_song_lyrics)
```

## Authors

Contributors

* [Filming](https://github.com/filming)

## License

This project is licensed under the MIT License - see the LICENSE file for details
