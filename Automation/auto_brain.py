from Automation.open_app import open_App
from Automation.web_open import openweb
import pyautogui as gui
from Automation.play_music_yt import play_music_on_youtube
from TTS.fast_df import speak
from Automation.play_music_sfy import play_music_on_spotify
import time
from Automation.tab_automation import perform_browser_action
from Automation.yt_play import perform_media_action
import pywhatkit
from Automation.scroll import perform_scroll_action
from STT.listen import listen   
import threading


def play():
    gui.press("space")
    
def search_google(text):
    pywhatkit.search(text)

def close():
    gui.hotkey('alt','f4')
    
def search(text):
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)

def Open_Brain(text):
    if "website" in text or "open website named" in text:
        text = text.replace("open","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website named","").strip()
        t1 = threading.Thread(target=speak,args=(f"Navigating {text} website",))
        t2 = threading.Thread(target=openweb,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        t1 = threading.Thread(target=speak,args=(f"Navigating {text} application",))
        t2 = threading.Thread(target=open_App,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        


def Auto_main_brain(text):
   try: 
    
    if text.startswith("open"):
        Open_Brain(text)
    elif "close" in text:
        close()

    elif "play music" == text or "play music on youtube" in text:
        speak("which song do you want to play sir.")
        while True:
            output_text=listen()
            play_music_on_youtube(output_text)
            break
                    
     
    elif  "play music spotify" in text:
        speak("Which song do you want to play, sir.")
        while True:
            output_text=listen()
            play_music_on_spotify(output_text)
            break

    elif "search in google" in text:
        text = text.replace("search","")
        text = text.replace("in","")
        text = text.replace("google","")
        t1 = threading.Thread(target=speak,args=(f"performing research about {text} in google search engine",))
        t2 = threading.Thread(target=search_google,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    elif "play" in text or "stop" in text or "pause" in text:
        play()

    else:
        perform_browser_action(text)
        perform_media_action(text)
        perform_scroll_action(text)
        

   except Exception as e:
       return 1
       pass
       