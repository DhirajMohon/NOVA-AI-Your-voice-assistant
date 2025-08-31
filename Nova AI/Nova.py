import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import openai_request as ai
import mtranslate

engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content= " "
    while content== " ":
        print("Type your command:")
        content = input(">>> ")  # Accept user input via keyboard
        print("You Typed =>", content)

    
    return content

def main_process():
    chat = []
    while True:
        request = command().lower()
        if "hello" in request:
            a="Welcome, How can I help you?"
            print(a)
            speak("") 
        elif "play music" in request:
            print("Playing Music.........")
            # speak("Playing Music")
            song = random.randint(1,3)
            if song==1:
                webbrowser.open("https://www.youtube.com/watch?v=sg5iiZoD3I0")
            elif song==2:
                webbrowser.open("https://www.youtube.com/watch?v=nqydfARGDh4")
            elif song==3:
                webbrowser.open("https://www.youtube.com/watch?v=DAYszemgPxc")
        elif "say time" in request:
            now_time= datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        elif "say date" in request:
            now_time= datetime.datetime.now().strftime("%d:%M")
            speak("Current date is " + str(now_time))
        elif "new task" in request:
            task= request.replace("new task", "")
            task= task.strip()
            if task != "":
                speak("Adding task : " + task)
                print("Adding Task " + task)
                with open("todo.txt","a") as file:
                    file.write(task+ "\n")
        elif "speak task" in request:
            with open("todo.txt","r") as file:
                speak("Work we have to do today is: " + file.read())
        elif "show work" in request:
            with open("todo.txt","r") as file:
                tasks = file.read()
            notification.notify(
                title= "Today's Work",
                message= tasks
            )
        elif "open youtube" in request:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query=request.replace("open", "")
            pyautogui.press("Super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            request = request.replace("Nova", "")
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            print(result)
            speak(result)
        elif "search google" in request:
            request = request.replace("Nova", "")
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q="+request)
        # elif "send whatsapp" in request:
        #     msg=input("Enter your Message: ")
        #     h=int(input("Set Time: "))
        #     m=int(input("Set Minute: "))
        #     pwk.sendwhatmsg("+8801608165301", msg,  h, m, 30)
        elif "send message" in request:
            msg = input("Enter your Message: ")
            h = int(input("Set Hour (24-hour format): "))
            m = int(input("Set Minute: "))
            
            try:
                pwk.sendwhatmsg("+8801608165301", msg, h, m, 10)
                speak("Message will be sent successfully.")
            except Exception as e:
                speak("Sorry, an error occurred while trying to send the message.")
                print(e)

        elif "ask ai" in request:
            chat = []

            request = request.replace("Nova ", "")
            request = request.replace("ask ai ", "")
            chat.append({"role": "user", "content": request})

            response = ai.send_request(chat)
            print(response)
            speak(response)
        elif "clear chat" in request:
            chat = []
            speak("Chat Cleared")
        else:
            request = request.replace("Nova ", "")

            chat.append({"role": "user", "content": request})
            # print(chat)
            response = ai.send_request(chat)

            chat.append({"role": "assistant", "content": response})
            # print(chat)
            print(response)
            speak(response)


main_process()