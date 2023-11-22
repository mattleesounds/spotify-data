import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_track_details(track_id, token):
    track_url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(track_url, headers={"Authorization": f"Bearer {token}"})
    track_data = response.json()
    artist_id = track_data['artists'][0]['id']
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    artist_response = requests.get(artist_url, headers={"Authorization": f"Bearer {token}"})
    artist_data = artist_response.json()
    genre = artist_data['genres'][0] if artist_data['genres'] else "Not Available"
    popularity = artist_data['popularity']
    return genre, popularity

token = get_spotify_token(client_id, client_secret)

csv_file_path = 'regional-global-weekly-2022-12-08.csv'
df = pd.read_csv(csv_file_path)

df['artist_genre'] = ''
df['artist_popularity'] = ''

for index, row in df.iterrows():
    print(f"Processing track {index + 1} of {len(df)}")
    track_id = row['uri'].split(':')[-1]
    try:
        genre, popularity = get_track_details(track_id, token)
        df.at[index, 'artist_genre'] = genre
        df.at[index, 'artist_popularity'] = popularity
    except Exception as e:
        print(f"Error processing track ID {track_id}: {e}")

new_csv_file_path = 'december-22.csv'
df.to_csv(new_csv_file_path, index=False)

print(f"Updated CSV file saved as {new_csv_file_path}")
