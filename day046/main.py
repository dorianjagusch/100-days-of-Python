from bs4 import BeautifulSoup
import requests
import datetime as dt
import dotenv, os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'


url = "https://www.billboard.com/charts/hot-100"


def get_date():
    user_input = ""
    while user_input == "":
        user_date = input("From what day would you like to get the Top 100 Songs? (YYYY-MM-DD): ")

        try:
            date = dt.datetime.strptime(user_date, "%Y-%m-%d")
        except:
            user_input = ""
            continue
        else:
            return user_date


def scrape_billboard(date):

    response = requests.get(f"{url}/{date}")
    response.raise_for_status()
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    songs_raw = soup.select("div ul li ul li h3")
    songs = [song.getText().strip("\n\t") for song in songs_raw]
    return songs
    # artists_raw = soup.select("div ul li ul li ")
    # artists = [artist.getText().strip("\n\t") for artist in artists_raw]
    # print(artists)


def connect_to_spotify():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username="Dude DudeBro"
        )
    )

    return sp


def search_songs(date, songs, sp):

    user_id = sp.current_user()["id"]

    song_uris = []
    year = date.split("-")[0]
    for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris


def create_playlist(date, tracks, sp):
    user_id = sp.current_user()["id"]
    playlist_title = f"{date} Billboad 100"
    playlist_id = sp.user_playlist_create(user=user_id,
                                          name=playlist_title,
                                          public=False)
    sp.playlist_add_items(playlist_id["id"], items=tracks)


def main():
    date = get_date()
    songs = scrape_billboard(date)
    sp = connect_to_spotify()
    tracks = search_songs(date, songs, sp)
    create_playlist(date, tracks, sp)


if __name__ == "__main__":
    main()
