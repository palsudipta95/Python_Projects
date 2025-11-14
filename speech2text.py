import pyttsx3
import speech_recognition as sr

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Done!")

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

    except sr.UnknownValueError as e:
        print("Could not understand audio")

get()