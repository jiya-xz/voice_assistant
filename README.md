# 🎙️ Nyx – Python Voice Assistant

**Nyx** is a Python-based voice assistant designed to make everyday tasks easier through voice commands. It listens to your voice, understands commands, and responds using speech.

## ✨ Features

- 🎤 Voice recognition and command detection
- 🔊 Female voice responses using text-to-speech
- 🌐 Open popular websites
- 🕒 Tell the current time
- 😂 Share random jokes and fun facts
- 💬 Generate random quotes
- 🎵 Open songs
- 🎲 Flip a coin or roll a dice
- 👋 Exit through a voice command

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Windows SAPI5 Text-to-Speech

## 📁 Project Structure

```text
voice/
│
├── app.py
├── requirement.txt
├── test_mic.py
├── test_voice.py
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/jiya-xz/voice_assistant.git
```

### 2. Navigate to the project folder

```bash
cd voice_assistant
```

### 3. Create a virtual environment

```bash
py -3.13 -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirement.txt
```

## ▶️ Run Nyx

Start the voice assistant using:

```bash
python app.py
```

Allow microphone access when prompted and start speaking your commands.

## 💻 Requirements

- Windows operating system
- Python 3.13
- Working microphone
- Internet connection for online speech recognition, if used by the recognition service

## 🚀 Future Improvements

- Add more voice commands
- Improve natural language understanding
- Add a graphical user interface (GUI)
- Integrate AI-powered conversations
- Add customizable voice options

## 👩‍💻 Author

**Jiya**

GitHub: [@jiya-xz](https://github.com/jiya-xz)

---

⭐ If you find this project interesting, consider giving it a star!
