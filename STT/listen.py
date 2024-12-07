import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        

        while True:  # Loop until valid input is received
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                text = recognizer.recognize_google(audio).strip()
                text = text.lower()
                
                if text:
                    print("User :"+text)  # If valid input is detected
                    return text
            except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
                pass  # Retry silently
            except Exception:
                pass  # Retry silently


