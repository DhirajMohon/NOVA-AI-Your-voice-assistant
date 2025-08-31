import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content= " "
    while content== " ":
        # obtain audio from the microphone 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("You Said....." + content)
        except Exception as e:
            print("Please try again....")
    
    return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("Welcome, How can I help you?") 

main_process()