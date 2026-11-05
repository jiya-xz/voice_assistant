import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

    print("Speak something now...")
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    print("Audio captured successfully!")