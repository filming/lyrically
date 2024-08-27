from src.lyrically import Lyrically


def main():
    lyrically = Lyrically()

    urls = [
        "https://www.azlyrics.com/lyrics/danshay/10000hours.html",
        "https://www.azlyrics.com/lyrics/taylorswift/lovestory.html",
        "https://www.azlyrics.com/lyrics/dualipa/illusion.html",
        "https://www.azlyrics.com/lyrics/shaboozey/abarsongtipsy.html",
        "https://www.azlyrics.com/lyrics/arianagrande/theboyismine.html",
    ]
    lyrics = lyrically.get_song_lyrics(urls[4])
    print(lyrics)


if __name__ == "__main__":
    main()
