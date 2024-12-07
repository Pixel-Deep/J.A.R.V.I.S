import pygame
import os

# Relative path to the music file
music_file = "Musics/booting.mp3"  # Ensure the relative path is correct for your directory structure

# Resolve the relative path to an absolute path
music_file_path = os.path.abspath(music_file)

# Check if the file exists
if not os.path.exists(music_file_path):
    print(f"Error: The file '{music_file_path}' does not exist.")
else:
    # Initialize the pygame mixer
    pygame.mixer.init()

    try:
        # Load and play the music file
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.play()
        print(f"Playing: {music_file}")

        # Keep the program running while the music is playing
        while pygame.mixer.music.get_busy():
            pass  # Busy-wait for the music to finish

    except Exception as e:
        print(f"Error: Could not play the music. Details: {e}")

    finally:
        # Quit the mixer after playback
        pygame.mixer.quit()
