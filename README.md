# Apple Music to Spotify Playlist Converter

This is a simple Python script that converts an Apple Music playlist to a Spotify playlist. It uses the Spotipy library to interact with the Spotify API, and the Requests and Beautiful Soup libraries to scrape the song information from the Apple Music playlist page.

## Requirements

- Python 3.x
- Spotipy library (`pip install spotipy`)
- Requests library (`pip install requests`)
- Beautiful Soup library (`pip install beautifulsoup4`)
- Fake User Agent library (`pip install fake-useragent`)

## Setup

1. Create a new Spotify application and note down the `Client ID`, `Client Secret`, and `Redirect URI`.
2. Clone this repository to your local machine or download the `main.py` file.
3. Open the `main.py` file in a text editor and replace the `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI` placeholders in the `os.environ` lines with the respective values from your Spotify application.
4. Open a command prompt or terminal window in the same directory as the `main.py` file.
5. Run the command `python main.py` to start the script.

## Usage

1. Enter the URL of the Apple Music playlist when prompted.
2. The script will scrape the song information from the playlist page and search for each song on Spotify.
3. If a match is found on Spotify, the song will be added to a new Spotify playlist with the same name as the Apple Music playlist.
4. The script will print a message indicating the number of songs that were successfully added to the new Spotify playlist. 

Note: You must have a Spotify account and be logged in to use this script. Also, the Spotify account must have permission to create public playlists.