from Automation.auto_brain import Auto_main_brain
from Features.check_app import *
from TTS.fast_df import speak
from STT.listen import listen
from Features.create_file import create_file
from weather_check.check_weather import get_weather_by_address
from weather_check.places import extract_location
from Features.mic_health import mike_health
from Features.speaker_health import speaker_health_test
from Features.set_get_win import *
from Features.check_app import *
from Brain.brain_phind import Main_Brain
from Features.find_ip import find_my_ip
from Features.get_joke import get_random_joke
from Features.get_advice import get_random_advice
from Others.extract import extract_volume_level
from Brain.imdb import fetch_movie_data
from Brain.wiki import search_on_wikipedia
from Time_Function.time import get_greeting, get_current_time
from Brain.news import fetch_news, _format_headlines
from Brain.datafeatch import main
from TTS.fast_df import print_animated_message
import pygame
import os

music_file = "Musics/intro.mp3"
music_file_path = os.path.abspath(music_file)

def check_inputs(output_text):
    if "check running application" in output_text or "say the running applications" in output_text or "running application" in output_text or "running applications" in output_text or "check running application" in output_text or "check running applications" in output_text:
        check_running_app()

    elif output_text.startswith("create"):
        if "file" in output_text:
            create_file(output_text)

    elif "weather" in output_text:
        text = extract_location(output_text)
        ans = get_weather_by_address(text)
        speak(ans)

    elif "introduce yourself" in output_text or "who are you" == output_text:
        pygame.mixer.init()
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.play()
        pass
        print_animated_message("Allow me to introduce my, I am JARVIS. . ")
        print_animated_message("A virtual artificial inteligence and i am here to asist you with variety of task as best i can.")
        print_animated_message("24 hours a day 7 days a week .")
        print_animated_message("Importing all preferences from home interface")
        print_animated_message("System is about fully operational")

    elif "greet" in output_text:
        speak(get_greeting())

    elif "time" in output_text:
        speak(get_current_time())

    elif "news" in output_text:
        keywords = 'latest news'
        timelimit = 'd'
        news_list = fetch_news(keywords, timelimit)
        formatted_headlines = _format_headlines(news_list)
        print(formatted_headlines)

    elif "data" in output_text:
        main(output_text)
        
    elif "movie" in output_text:
        speak("Please tell me the movie name:")
        text = listen()
        fetch_movie_data(text)

    elif "wikipedia" in output_text:
        text=search_on_wikipedia(output_text)
        speak(text)
    
    elif "advice" in output_text :
        ans = get_random_advice()
        speak(ans)

    elif "joke" in output_text :
        ans = get_random_joke()
        speak(ans)

    elif "find ip" in output_text or "what is my ip" == output_text or "what is my ip address" == output_text :
        ans =find_my_ip()
        print(ans)

    elif "explain" in output_text or "explain me" in output_text or "explain this" in output_text or "what is" in output_text or "what is this" in output_text or "define " in output_text or "define this" in output_text or "definition of" in output_text or "definition of this" in output_text or "define this" in output_text or "definition of this" in output_text or "who is" in output_text or "who is this" in output_text or "where is" in output_text or "where is this" in output_text:
        ans =Main_Brain(output_text)
        speak(ans)

    
    elif "check mic" in output_text or "check mike health" in output_text or "check microphone" in output_text:
        mike_health()

    elif "check speaker health" in output_text or "check speaker" in output_text:
        speaker_health_test()


    elif "check volume level" in output_text:
        get_volume_windows()
                 

    else:
        if (Auto_main_brain(output_text) ==1):
            pass
        pass

