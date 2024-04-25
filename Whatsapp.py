import pywhatkit # type: ignore
import pyttsx3 # type: ignore
import datetime
import speech_recognition # type: ignore
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime =int(datetime.now().strftime("%H"))
update =int((datetime.now()+timedelta(minutes =2)).strftime("%M"))

def sendMessage():
    speak("who do you want to message")
    a=int(input('''Person1- 1
    Person 2 -2'''))
    if a==1:
      speak("what the message")
      message=str(input("Enter the message-"))
      pywhatkit.sendwhatmsg("+916261468454", message,time_hour=strTime,time_nin=update)
    elif a == 2:
      speak("what the message")
      message = str(input("Enter the message-"))
      pywhatkit.sendwhatmsg("+918319168237", message, time_hour=strTime, time_nin=update)
