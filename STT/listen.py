import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 500
    recognizer.dynamic_energy_adjustment_damping = 0.15
    recognizer.dynamic_energy_ratio = 0.9
    recognizer.pause_threshold = 0.5
    recognizer.operation_timeout = None

    try:
        with sr.Microphone() as source:
            
            audio = recognizer.listen(source)

        try:
            # Attempt to recognize the speech
            text = recognizer.recognize_google(audio, language='en-IN')
            text = text.lower()
            print("\033[93mUser: {}\033[0m".format(text), flush=True)
            return text
        except sr.UnknownValueError:
            # Handle case where speech is not understood
            print("\033[91mCould not understand the audio.\033[0m", flush=True)
        except sr.RequestError as e:
            # Handle API errors or connection issues
            print("\033[91mSpeech recognition service error: {}\033[0m".format(e), flush=True)
    except Exception as e:
        # Handle any other errors, such as microphone access issues
        print("\033[91mAn error occurred: {}\033[0m".format(e), flush=True)

    # Return a fallback value to ensure the program continues
    return ""
