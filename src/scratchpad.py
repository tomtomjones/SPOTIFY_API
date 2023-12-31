import gzip
import csv

def test_csv_header(data_dir: str = "tests/test_data/"):
    expected_tracks_records_headers = ['album_type','track_id','track_name','track_popularity','track_uri']
    csv_file_path = f'{data_dir}tracks_records.csv.gz'
    with gzip.open(csv_file_path, 'rt', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        print(headers)
        print(expected_tracks_records_headers) 

test_csv_header()