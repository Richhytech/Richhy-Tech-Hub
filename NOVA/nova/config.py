# load environment variables from .env file
from dotenv import load_dotenv
import os

load_dotenv()
# get the OpenAI API key from environment variables
AI_MODE = os.getenv("AI_MODE", "offline")
WAKE_WORD = os.getenv("WAKE_WORD", "NOVA")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
