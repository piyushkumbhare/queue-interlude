import os
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# FILL IN THESE WITH YOUR CREDENTIALS
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def main():
    scope = ["user-modify-playback-state", "user-read-playback-state"]
    token = SpotifyOAuth(
        username=None,
        scope=scope,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback"
    ).get_access_token(as_dict=False)

    

    client = spotipy.Spotify(auth=token)

    try:
        client.queue()
    except Exception as e:
        print(f"Ran into exception: {e}")
        print("Are you worthy?")
        exit(1)

    f = subprocess.Popen(['playerctl', '--player=spotify', 'metadata', 'xesam:url', '-F'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

    INIT_GUARD = True

    while True:
        if INIT_GUARD:
            INIT_GUARD = False
        else:
            line = f.stdout.readline().strip()
            print(f"New song: {line}")
            if line == b'https://open.spotify.com/track/2A3DQcqRgArPwaOP7CWqtQ':
                print("FALLING AWAY WITH YOU DETECTED")
                try:
                    print("Attempting to queue Interlude")
                    client.add_to_queue("spotify:track:0Qe6Us6taV5fVd3r87dFRP")
                except Exception as e:
                    print(f"Exception: {e}")
                    continue

if __name__ == "__main__":
    main()
