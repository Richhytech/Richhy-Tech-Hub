import os

# folder structure
folders = [
    "NOVA",
    "NOVA/nova",
    "NOVA/assets",
    "NOVA/tests",
]

# create folders
files= [
    "NOVA/main.py",
    "NOVA/requirements.txt",
    "NOVA/README.md",
    "NOVA/.gitignore",
    "NOVA/.env",
    
    "NOVA/nova/__init__.py",
    "NOVA/nova/brain.py",
    "NOVA/nova/core.py",
    "NOVA/nova/voice.py",
    "NOVA/nova/vision.py",
    "NOVA/nova/utils.py",
    "NOVA/nova/config.py"
]

# create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# create files
for file in files:
    with open(file, 'w') as f:
        pass

print("NOVA project structure created successfully!")

import os

def write_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)

os.makedirs("NOVA/nova", exist_ok=True)
os.makedirs("NOVA/tests", exist_ok=True)
os.makedirs("NOVA/assets", exist_ok=True)

write_file("NOVA/main.py", """from nova.core import respond

while True:
    user = input("You: ")
    if user == "exit":
        break
    print("NOVA:", respond(user))
""")

write_file("NOVA/nova/core.py", """def respond(text):
    return "NOVA is ready: " + text
""")

write_file("NOVA/nova/__init__.py", "")
write_file("NOVA/requirements.txt", "")
write_file("NOVA/README.md", "# NOVA AI Assistant")
write_file("NOVA/.gitignore", "venv/\n__pycache__/\n.env")

print("✅ NOVA with starter code created!")