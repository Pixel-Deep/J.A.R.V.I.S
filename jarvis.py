from Alert import Alert
from Others.internet_check import is_Online
from Others.respond import wait_for_jarvis
from Data.dlg_data import online_dlg
from Time_Function.time import get_greeting
from TTS.fast_df import speak,print_animated_message
from STT.listen import listen
from co_brain import check_inputs
import random
import pygame
import time
import os


music_file = "Musics/booting.mp3"
music_file_path = os.path.abspath(music_file)
ran_online_dlg = random.choice(online_dlg)

greeting=get_greeting()

def main(): 
    print_animated_message("System Authentication...")
    
    if wait_for_jarvis() == 1:
        print_animated_message("Jarvis Activated")
        pygame.mixer.init()
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(14)

        if is_Online():
            Alert(ran_online_dlg,greeting)
            speak(greeting)
            speak(ran_online_dlg)
            

            while True:
                output_text=listen()
                check_inputs(output_text)
                
                if output_text == "shut down" or output_text=="close" or output_text=="exit" or output_text=="quit" or output_text=="bye" or output_text=="goodbye" or output_text=="shutdown" or output_text=="close jarvis" or output_text=="close Jarvis" :
                    speak("Goodbye Sir")
                    break
     

main()