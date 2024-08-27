from src.lyrically import Lyrically


def main():
    lyrically = Lyrically()

    artist_name = "JuStIn BiEbEr"
    discography = lyrically.get_artist_discography(artist_name)

    print(discography)


if __name__ == "__main__":
    main()
