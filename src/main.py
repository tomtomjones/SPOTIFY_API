import requests

from src.config.config_util import get_config_value
from src.token_auth import get_app_access_token
from src.deconstruct_category import Playlist
from src.deconstruct_playlist import PlaylistTracks
from src.csv_handler import write_to_csv
from src.csv_handler import compress_csv_file

CLIENT_ID = get_config_value('API_KEYS', 'CLIENT_ID')
CLIENT_SECRET = get_config_value('API_KEYS', 'CLIENT_SECRET')
SPOTIFY_URL = get_config_value('base_config', 'SPOTIFY_API_URL')
DATA_DIR = get_config_value('base_config', 'DATA_DIR')

## get access token
ACCESS_TOKEN = get_app_access_token(CLIENT_ID, CLIENT_SECRET)
BEARER_TOKEN_HEADERS = {
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}

playlist_limit = 50 # number of playlists to get from chosen category
playlist_category = "latin" # category of playlists to retrieve

# Stores all playlist IDs retrieved from first category call
playlist_id_holder = [] # placeholder for playlist IDs, used to get playlist info later
category_playlists_records = [] # description:, name:, id:, tracks_url, total_tracks, snapshot_id
playlist_records = [] # id, followers of each playlist
tracks_records = [] #album_type id: , name: a track's name, popularity: a track's popularity value at the time of the API calluri: a track's URI
playlist_track_id_records = [] # playlist_id: the ID of a playlist, playlist_added_at: time at which a track was added to the playlist, track_id: the ID of a track
track_artist_id_records = [] #track_id: the ID of a track, artist_id: the ID of an artist
artists_records = [] #id: unique artist identifier, name: name of an artist
    

def make_api_call(url, params=None):
    try:
        response = requests.get(url=url, params=params, headers=BEARER_TOKEN_HEADERS)
        if response.status_code == 200:
            return response
        else:
            print("make_api_call call failed with status code:", response.status_code, "\n", url, "\n", response.text)
            raise SystemExit 
        
    except requests.exceptions.RequestException as e:
        print("make_api_call call failed: ", e)


## build request and get playlist category
def get_playlists_in_category(category_id: str):
    endpoint_url =  f"{SPOTIFY_URL}browse/categories/{category_id}/playlists"
    call_params = { "limit": playlist_limit }
    response =  make_api_call(endpoint_url, call_params) 
    return response


def get_playlists_info(playlist_id: str):
    
    endpoint_url = f"{SPOTIFY_URL}playlists/{playlist_id}"
    response = make_api_call(endpoint_url)
    return response


def create_category_playlists_records(category_id: str):

    response = get_playlists_in_category(category_id)
    category_json = response.json()
    playlists_data = category_json["playlists"]
    playlists = [Playlist(item_data) for item_data in playlists_data["items"]] # for each item in the list of items, create a Playlist object
    # playlists = []
    # for item_data in playlists_data["items"]:
    #     playlists.append(Playlist(item_data))
    
    for playlist in playlists:
        category_playlists_records.append([playlist.description, playlist.name, playlist.id, playlist.snapshot_id, playlist.tracks.href, playlist.tracks.total])
        playlist_id_holder.append(playlist.id) # add all category playlist IDs to playlist_id_holder list

    return category_playlists_records


def create_playlist_records():      

    for playlist_id in playlist_id_holder:
        response = get_playlists_info(playlist_id) # category_playlists_records contains the playlists retrieved in chosen category
        playlist_json = response.json() 

        track_playlist = PlaylistTracks(playlist_json)
        items = track_playlist.tracks.items # nested list of objects
        
        # first list of objects loop
        for item in items:
            playlist_added_at = item.added_at
            track = item.track
            track_name = track.name
            track_popularity = track.popularity
            track_uri = track.uri
            track_id = track.id
            album = track.album
            album_type = album.type
            artists = album.artists
            # produce the tracks_records and playlist_track_id_records datasets
            tracks_records.append([album_type, track_id, track_name, track_popularity, track_uri])
            playlist_track_id_records.append([playlist_id, playlist_added_at, track_id])

            # second list of objects loop
            for artist in artists:
                artist_id = artist.id
                artist_name = artist.name
                # produce the track_artist_id_records and artists_records datasets
                track_artist_id_records.append([track_id, artist_id])
                artists_records.append([artist_id, artist_name])

        # produce the playlist_records dataset
        followers_total = track_playlist.followers.total # nested object
        playlist_id = track_playlist.id
        playlist_records.append([playlist_id, followers_total])

    # de-dupe the artists_records list
    artists_records_deduplicated = []
    seen_names = set()
    for artist in artists_records:
        artist_name = artist[1] # get the artist name
        if artist_name not in seen_names: # if the artist name is not in the set, add it to the set and the list
            artists_records_deduplicated.append(artist)
            seen_names.add(artist_name)
    artists_records_deduplicated.sort(key=lambda x: x[1]) # sort the list by artist name, alphabetically

    return  playlist_records, tracks_records,  playlist_track_id_records, track_artist_id_records, artists_records_deduplicated


def main():

    category_playlists_records = create_category_playlists_records(playlist_category)
    write_to_csv("category_playlists_records.csv", DATA_DIR, ["description","name", "id", "snapshot_id", "tracks_url", "total_tracks"], category_playlists_records)

    playlist_records, tracks_records,  playlist_track_id_records, track_artist_id_records, artists_records_deduplicated = create_playlist_records()
    write_to_csv("playlist_records.csv", DATA_DIR, ["id", "followers"], playlist_records)
    write_to_csv("tracks_records.csv", DATA_DIR, ["album_type", "track_id", "track_name", "track_popularity", "track_uri"], tracks_records)
    write_to_csv("playlist_track_id_records.csv", DATA_DIR, ["playlist_id", "playlist_added_at", "track_id"], playlist_track_id_records)
    write_to_csv("track_artist_id_records.csv", DATA_DIR, ["track_id", "artist_id"], track_artist_id_records)
    write_to_csv("artists_records.csv", DATA_DIR, ["artist_id", "artist_name"], artists_records_deduplicated)

    ## compress and delete csv files
    compress_csv_file(DATA_DIR)

    print("Done!")

if __name__ == "__main__":
    main()
