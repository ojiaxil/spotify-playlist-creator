from client import Client

def main():
    AUTH_TOKEN = input("Enter Authorization Token: ")
    User_ID = input("Enter Username: ")

    spotify_client = Client(AUTH_TOKEN, User_ID)

    # last played songs

    visualize_songs = int(input("Songs to visualize?: "))
    last_played_songs = spotify_client.last_played_songs(visualize_songs)

    print(f"Here are the last {visualize_songs} songs you listened to: ")
    for i, song in enumerate(last_played_songs):
        print(f"{i}:{song}")

    # seed songs

    indices = input("Enter a list of up to 5 songs to use as seeds. (Use indices separated by space): ")
    indices = indices.split()
    seed_songs = [last_played_songs[int(i) - 1] for i in indices]

    # recommended songs from seeds

    recommended_songs = spotify_client.recommendations(seed_songs)
    print("\nHere are the recommended songs that will be included in the new playlist: ")
    for i, song in enumerate(recommended_songs):
        print(f"{i - 1}:{song}")
    
    # create new playlist
        
    playlist_name = input("Name of new playlist: ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"Playlist '{playlist_name} created successfully!")

    # add to playlist

    spotify_client.add_to_playlist(playlist, recommended_songs)
    print(f"\nSongs successfully added to playlist '{playlist_name}'")

if __name__ == '__main__':
    main()