# filepath: brain.py
from nova.utils import search_web
from nova.vision import detect_face  # Changed to relative import
import datetime
import os
from google.generativeai import GenerativeModel, configure
from nova.config import GEMINI_API_KEY
from google.api_core import exceptions


# Initialize GENAI client
configure(api_key=GEMINI_API_KEY)

model = GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are NOVA AI assistant."
)

chat = model.start_chat(history=[])

def ask_ai(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text

    except exceptions.ResourceExhausted:
        return "⚠️ API quota exceeded. Try again later."

    except exceptions.GoogleAPIError:
        return "⚠️ Google API error occurred."

    except Exception as e:
        print(e)
        return "⚠️ Unexpected AI error."
    
def offline_response(command):
    if "hello" in command:
        return "Hello! I'm NOVA."
    elif "your name" in command:
        return "I am NOVA, your assistant."
    elif "how are you" in command:
        return "I'm functioning perfectly."
    else:
        return "I'm currently offline, but still learning."


def handle_command(command):
    """
    Handle system commands first, then fallback to AI
    """
    command = command.lower()

    # 🌐 WEB SEARCH
    if "search" in command:
        query = command.replace("search", "").strip()
        return search_web(query)

    # 📷 CAMERA
    elif "open camera" in command or "detect face" in command:
        detect_face()
        return "Camera activated."

    # 📂 OPEN FILE
    elif "open file" in command:
        filename = command.replace("open file", "").strip()
        if os.path.exists(filename):
            os.startfile(filename)
            return f"Opening {filename}"
        return "File not found."

    # 💻 OPEN APPLICATION
    elif "open" in command:
        app = command.replace("open", "").strip()
        try:
            os.startfile(app)
            return f"Opening {app}"
        except:
            return "Application not found."

    # ⏰ TIME
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The time is {now}"

    # ❌ EXIT
    elif "exit" in command:
        return "EXIT"

    # 🤖 DEFAULT → AI
    else:
        if GEMINI_API_KEY:
            return ask_ai(command)
        else:
            return offline_response(command)
def respond(user):
    return handle_command(user)