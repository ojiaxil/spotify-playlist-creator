# a single sound track

class Track:
    def __init__(self, name, id, artist):
        self.name = name # name of song
        self.id = id # spotify track id
        self.artist = artist # artist name

    def create_uri(self):
        return f"spotify:track:{self.id}"
    
    def __str__(self):
        return self.name + " by " + self.artist