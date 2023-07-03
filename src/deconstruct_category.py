

class Playlist:
    def __init__(self, data):

        self.description = data["description"]
        self.id = data["id"]
        self.name = data["name"]
        self.snapshot_id = data["snapshot_id"]
        self.tracks = Tracks(data["tracks"])





class Tracks:
    def __init__(self, data):
        self.href = data["href"]
        self.total = data["total"]


# class SpotifyCategory:
#     def __init__(self, result):  ##everything needs to have reference to self in OO programming
#         self.result = Playlist(result)

        # self.collaborative = data["collaborative"]
        # self.external_urls = data["external_urls"]
        # self.href = data["href"]
        ## self.images = [Image(image_data) for image_data in data["images"]]
        ## self.owner = Owner(data["owner"])
        # self.primary_color = data["primary_color"]
        # self.public = data["public"]

        # self.type = data["type"]
        # self.uri = data["uri"]
        # print(self.description)
# class Image:
#     def __init__(self, data):
#         self.height = data["height"]
#         self.url = data["url"]
#         self.width = data["width"]

# class Owner:
#     def __init__(self, data):
#         self.display_name = data["display_name"]
#         self.external_urls = data["external_urls"]
#         self.href = data["href"]
#         self.id = data["id"]
#         self.type = data["type"]
#         self.uri = data["uri"]
