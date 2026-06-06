import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def get_microphone():
    '''automatically detects microphone.
    Priority:
    1. Default system microphone
    2. Iriun Webcam microphone
    3. Any other available microphone
    '''
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        if "default" in name.lower():
            return sr.Microphone(device_index=i)
    return None # fall back to default behavior if no microphone is found

def listen():
    # listen for user input and return it as text
    r= sr.Recognizer()
    mic = get_microphone()
    
    # to increase threshold frequecy for better recognition in noisy environments
    r.energy_threshold = 10000
    r.dynamic_energy_ratio = 3.0
    
    # use default microphone if no specific microphone is found
    with mic if mic else sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def Wait_for_wake_word(wake_word="nova"):
    """Continuously listens for the wake word and returns when it is detected."""
    while True:
        text = listen().lower()
        if wake_word in text:
            print("Wake word detected!")
            return