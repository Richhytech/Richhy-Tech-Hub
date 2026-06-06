import os

def run_command(user):
    user = user.lower()

    if "open chrome" in user:
        os.system("start chrome")
        return "Opening Chrome"

    if "shutdown" in user:
        os.system("shutdown /s /t 5")
        return "Shutting down system"

    return None