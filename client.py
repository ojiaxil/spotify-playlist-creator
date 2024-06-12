import json
import requests
from requests.models import Response
from track import Track
from playlist import Playlist

# this class serves as the client class which works with the Spotify API

class Client:
    def __init__(self, auth_token, user_id):
        self.auth_token = auth_token # Spotify API token
        self.user_id = user_id # Spotify user ID

    # get API request
        
    def _get_api_request(self, url):
        response = requests.get(url, headers = {"Content-Type": "application/json",
                                                "Authorization": f"Bearer {self.auth_token}"})
        return response
    
    # post API request

    def _post_api_request(self, url, data):
        response = requests.post(url, data = data, headers = {
            "Content-Type": "application/json", "Authorization": f"Bearer {self.auth_token}"
        })
        return response
    
    # get last played songs/tracks

    def last_played_songs(self, limit = 10):
        url = f"https://api.spotify.com/v1//me/player/recently-played?limit={limit}"
        response = self._get_api_request(url)
        response_json = response.json()
        songs = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]
        return songs
    
    # get list of recommended songs from reference tracks

    def recommendations(self, ref_tracks, limit = 50):
        ref_tracks_url = ""
        for ref_track in ref_tracks:
            ref_tracks_url += ref_track.id + ','
        ref_tracks_url = ref_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={ref_tracks_url}&limit={limit}"
        response = self._get_api_request(url)
        response_json = response.json()
        songs = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response_json["tracks"]]
        return songs
    
    # create playlist

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Recommended Songs: ",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._post_api_request(url, data)
        response_json = response.json()

        p_id = response_json["id"]
        playlist = Playlist(name, p_id)
        return playlist
    
    # add songs to created playlist

    def add_to_playlist(self, playlist, songs):
        song_urls = [song.create_uri() for song in songs]
        data = json.dumps(song_urls)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._post_api_request(url, data)
        response_json = response.json()
        return response_json