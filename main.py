import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ['SPOTIPY_CLIENT_ID'] = 'CLIENT_ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'CLIENT_SECRET'
os.environ['SPOTIPY_REDIRECT_URI'] = 'REDIRECT_URI'
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
ua = UserAgent()

url = input("Enter the URL of the Apple Music playlist: ")

response = requests.get(url, headers={'User-Agent': ua.random})

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    playlist_name = soup.select_one('h1.headings__title').text.strip()
    song_name_divs = soup.select('div.songs-list-row__song-name')
    song_names = [div.text.strip() for div in song_name_divs]

    song_uris = []
    for song_name in song_names:
        results = sp.search(q=song_name, type='track', limit=1)
        if results and len(results['tracks']['items']) > 0:
            song_uri = results['tracks']['items'][0]['uri']
            song_uris.append(song_uri)

    playlist = sp.user_playlist_create(sp.current_user()['id'], playlist_name, public=True)

    sp.playlist_add_items(playlist['id'], song_uris)

    sp.playlist_change_details(playlist['id'], description=url)

    print(f'{len(song_uris)} songs successfully added to the new Spotify playlist!')
else:
    print(f'Request failed with status code {response.status_code}')