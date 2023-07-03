class PlaylistTracks:
    def __init__(self, json_data):
        self.followers = Followers(json_data["followers"])
        self.id = json_data["id"]
        self.name = json_data["name"]
        ##self.snapshot_id = json_data["snapshot_id"]
        self.tracks = Tracks(json_data["tracks"])

class Followers:
    def __init__(self, json_data):
        self.href = json_data["href"]
        self.total = json_data["total"]

class Tracks: 
    def __init__(self, json_data):
        self.href = json_data["href"]
        self.items = [Track(item_data) for item_data in json_data["items"]] # list of objects

class Track:
    def __init__(self, json_data):
        self.added_at = json_data["added_at"]
        self.added_by = json_data["added_by"]
        self.is_local = json_data["is_local"]
        self.primary_color = json_data["primary_color"]
        self.track = TrackData(json_data["track"]) # obbject
        self.video_thumbnail = json_data["video_thumbnail"]

class TrackData:
    def __init__(self, json_data):
        self.album = Album(json_data["album"])
        # self.artists = [Artist(artist_data) for artist_data in json_data["artists"]]
        self.available_markets = json_data["available_markets"]
        self.disc_number = json_data["disc_number"]
        self.duration_ms = json_data["duration_ms"]
        self.episode = json_data["episode"]
        self.explicit = json_data["explicit"]
        self.external_ids = json_data["external_ids"]
        self.external_urls = json_data["external_urls"]
        self.href = json_data["href"]
        self.id = json_data["id"]
        self.is_local = json_data["is_local"]
        self.name = json_data["name"]
        self.popularity = json_data["popularity"]
        self.preview_url = json_data["preview_url"]
        self.track = json_data["track"]
        self.track_number = json_data["track_number"]
        self.type = json_data["type"]
        self.uri = json_data["uri"]

class Album:
    def __init__(self, json_data):
        self.album_type = json_data["album_type"]
        self.artists = [Artist(artist_data) for artist_data in json_data["artists"]]
        self.available_markets = json_data["available_markets"]
        self.external_urls = json_data["external_urls"]
        self.href = json_data["href"]
        self.id = json_data["id"]
        # self.images = [Image(image_data) for image_data in json_data["images"]]
        self.name = json_data["name"]
        self.release_date = json_data["release_date"]
        self.release_date_precision = json_data["release_date_precision"]
        self.total_tracks = json_data["total_tracks"]
        self.type = json_data["type"]
        self.uri = json_data["uri"]

class Artist:
    def __init__(self, json_data):
        self.external_urls = json_data["external_urls"]
        self.href = json_data["href"]
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.type = json_data["type"]
        self.uri = json_data["uri"]