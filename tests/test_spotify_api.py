import unittest
import csv
import requests_mock
import requests
import json
import gzip
from src.config.config_util import get_config_value

TEST_DATA_DIR = get_config_value('base_config', 'TEST_DATA_DIR')

# Test the CSV header in the extract is what we expected
class TestCSVHeader(unittest.TestCase):
    def test_csv_header(self, data_dir: str = TEST_DATA_DIR):

        expected_tracks_records_headers = ['album_type','track_id','track_name','track_popularity','track_uri']
        csv_file_path = f'{data_dir}tracks_records.csv.gz'
        with gzip.open(csv_file_path, 'rt', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            # retrieves headers
            headers = next(csv_reader)

            self.assertEqual(headers, expected_tracks_records_headers)


# Test the output of the extract is what we expected
class TestPlaylistTrackCount(unittest.TestCase):
    def test_count_songs_in_playlist_track_file(
        self, data_dir: str = TEST_DATA_DIR, expected_song_count: int = 1
    ):  # count the number of songs in playlist_track_id_records.csv
        count = 0 
        with open(f"{data_dir}playlist_track_id_records.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                count += 1

        # Compare the count with an expected value
        expected_count = expected_song_count  # Replace with the actual expected count
        self.assertEqual(
            count,
            expected_count,
            "Unexpected count of songs in playlist_track_id_records.csv",
        )


# Test the API call is successful using a mock response
class TestSpotifyAPI(unittest.TestCase):
    def test_playlist_api_call(self):
        # self.maxDiff = None
        # Mock the API response
        with requests_mock.Mocker() as mock:
            playlist_id = "6dbr7iVBxMyFMSW2Hia6at"
            expected_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"

            with open("data/json_samples/response.json", "r") as file:
                mock_response = json.load(file)

            mock.get(expected_url, json=mock_response)
            # Make the API call
            response = requests.get(expected_url)
            self.assertEqual(response.status_code, 200)



