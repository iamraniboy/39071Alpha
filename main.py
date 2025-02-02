# ELEC 3907 Group 1A
# API Interface Code
# Written by Tanner Krauter

# TODO: get input info and modify event triggers, GUI Implementation (Ranishka),


# imports the spotipy library
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser


# Define key variables
username = 'tawseefpatel'
clientID = '0e82adf631c444569cce986dea9e374c'
clientSecret = '----'
redirectURI = 'https://www.google.ca/'
playback_state = False
loop_running = True
track_info = ""

# Creates OAuth object for Spotify
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI)

# Creates a spotify token
token_dict = oauth_object.get_cached_token()
token = token_dict['access_token']

# Create spotify object to interact with
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI,
                                               scope="user-modify-playback-state user-read-currently-playing user-read-playback-state"))

# Opens spotify webpage on device
webbrowser.open("https://open.spotify.com/", new=1, autoraise=False)

# Gets the device ID of the current device
devices = sp.devices()
device_id = devices['devices'][0]['id']
# print(device_id)

# Makes the current device active for the software to interact with
sp.transfer_playback(device_id)
playback_state = True
# Functions


# Adds media to the spotify queue
def add_to_queue(song_uri):
    sp.add_to_queue(song_uri)
    try:
        sp.start_playback(device_id)
    except:
        print("Song Playing")
    return True


# Gets info about the current media
def get_current_song_info():
    try:
        track = sp.current_user_playing_track()
        return (track['item']['name'] + " by " + track['item']['artists'][0]['name'])
    except:
        return 'none'


# Pauses or plays media depending on the current state
def play_pause_song(is_playing):
    if is_playing:
        sp.pause_playback(device_id)
        return False
    else:
        sp.start_playback('ab0bc3e6e491c36b242dc54eff8d7a61373ae60f')
        return True


# Skips to next media
def skip_song():
    sp.next_track(device_id)
    track = get_current_song_info()
    return track


# Returns to previous media
def return_to_song():
    sp.previous_track(device_id)
    track = get_current_song_info()
    return track


# Gets the most recent episode of a podcast
def get_most_recent_podcast(show_id):
    recent_episode = sp.show_episodes(show_id, '1')
    episode_id = recent_episode['items'][0]['id']
    full_id = 'spotify:episode:' + episode_id
    return full_id


# Main software loop
while loop_running:
    song_info = get_current_song_info()
    print(song_info)
    request = input("What would you like to do? \n")

    if request.lower() == "play song":
        song = input("What song would you like to hear? \n")

        if song.lower() == "enemy":
            playback_state = add_to_queue("spotify:track:1r9xUipOqoNwggBpENDsvJ")
            track_info = get_current_song_info()
        elif song.lower() == "warriors":
            playback_state = add_to_queue("spotify:track:1lgN0A2Vki2FTON5PYq42m")
            track_info = get_current_song_info()
        elif song.lower() == "never gonna give you up":
            playback_state = add_to_queue("spotify:track:4cOdK2wGLETKBW3PvgPWqT")
            track_info = get_current_song_info()
        elif song.lower() == "spooky scary skeletons":
            playback_state = add_to_queue("spotify:track:1sUdq3kWa9dJXHu3eYOUll")
            track_info = get_current_song_info()
        elif song.lower() == "guns for hire":
            playback_state = add_to_queue("spotify:track:2H3HPGuPyhcbg5AqoQ4BWr")
            track_info = get_current_song_info()
        else:
            print("Invalid Song, please enter a valid song")
    elif request.lower() == "play podcast":
        add_to_queue(get_most_recent_podcast("spotify:show:4rOoJ6Egrf8K2IrywzwOMk"))
        track_info = get_current_song_info()
    elif request.lower() == "skip":
        skip_song()
    elif request.lower() == "return":
        return_to_song()
    elif request.lower() == "pause/play":
        playback_state = play_pause_song(playback_state)
    elif request.lower() == "end session":
        if playback_state:
            playback_state = play_pause_song(playback_state)
        loop_running = False
    else:
        print("Invalid Command")
        
