import pyttsx3

data = input("Enter text to convert to speech: ")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()