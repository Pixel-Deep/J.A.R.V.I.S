from STT.listen import listen
import threading   


def wait_for_jarvis():
 
    while True:
        print("................................................................")
        user_input = listen()
        if user_input == "jarvis":
            return 1
            break  
        

