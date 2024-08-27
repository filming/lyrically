from lyrically import Lyrically


def main():
    lyrically = Lyrically()

    artist_name = "Justin BIEber"
    discography = lyrically.get_artist_discography(artist_name)


if __name__ == "__main__":
    main()
