from nova.voice import speak, listen, Wait_for_wake_word
from nova.core import respond

def run():
    print("NOVA is listening for the wake word...")
    Wait_for_wake_word()
    speak("Hello, how can I assist you today?")
    
    while True:
        user_input = listen()
        if user_input.lower() == "exit":
            speak("Goodbye!")
            break
        response = respond(user_input)
        print("NOVA:", response)
        speak(response)
if __name__ == "__main__":
    run()