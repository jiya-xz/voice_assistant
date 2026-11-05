import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

print("Available voices:")

for index, voice in enumerate(voices):
    print(index, voice.name)

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

engine.say("Hello! I am Nyx. I am back!")
engine.runAndWait()