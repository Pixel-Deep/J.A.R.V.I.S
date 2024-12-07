import webbrowser
import pyautogui as ui
import time

def play_music_on_spotify(song_name):
    # Open Spotify in the default web browser
    webbrowser.open("https://open.spotify.com/")
    time.sleep(6)  # Wait for the page to load

    # Click the search bar and type the song name
    ui.click(928, 171)
    time.sleep(0.5)
    ui.write(song_name)
    ui.press("enter")  # Search for the song
    time.sleep(3)

    # Click the play button
    ui.click(796, 503)
    time.sleep(2)

