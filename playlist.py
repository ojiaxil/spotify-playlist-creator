# spotify playlist

class Playlist:
    def __init__(self, name, id) -> None:
        self.name = name # name of playlist
        self.id = id # spotify playlist id

    def __str__(self):
        return f"Playlist: {self.name}"