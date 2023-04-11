import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2 
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voice[0],id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("recognizing...")
        querry = r.recognize_google(audio, language='en-id')
        print(f"user said:{querry}")

    except Exception as e:
        speak("say that again pleasse sir...")
        return "none"
    return querry

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour>=12:
        speak("good morning")
    elif hour>=12 and hour>=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i m jarvis sir, please tell how can i help you")
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to,content)
    server.close()

if __name__ =="__main__":
    wish()
    #while True:
    if 1:

        query = takecommand().lower()
         # logic building for task
        
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)


        elif "open cmd" in query:
             os.system("start cmd")

        elif "open camera" in query:
             cap = cv2.VideoCapture(0)
             while True:
                 ret, img = cap.read()
                 cv2.imshow('webcam', img)
                 k = cv2.waitKey(50)
                 if k==27:
                     break;
             cap.release()
             cv2.destroyAllWindows()
        
        elif "play music" in query:
             music_dir = "C:\music"
             songs = os.listdir(music_dir)
             #rd = random.choice(songs)
             for song in songs:
                 if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "ip address" in query:
             ip = get('https://api.ipify.org').text
             speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
             speak("searching wikipedia...")
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             speak(results)
             print(results)
        
        elif "open youtube" in query:
             webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
             webbrowser.open("www.facebook.com")
        
        elif "open stackoverflow" in query:
             webbrowser.open("www.stackoverflow.com")
        
        elif "open instagram" in query:
             webbrowser.open("www.instagram.com")

        elif "open google" in query:
             speak("sir, what should i search on google")
             cm = takecommand().lower()
             webbrowser.open(f"{cm}")
        
        # elif "send message" in query:
        #      kit.sendwhatmsg("+62895605902537, this is testing protocol",2,25)

        # elif "play song in youtube" in query:
        #      kit.playonyt("see you again")

        elif "email to hamdi" in query:
             try:
                 speak("what should i say?")
                 content = takecommand().lower()
                 to = "alhamdirifai20@gmail.com"
                 sendEmail(to,content)
                 speak("email has benn sent to hamdi")
            
             except Exception as e:
                 print(e)
                 speak(" sorry sir, i am not able to sent this email to hamdi")
        
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day....")
            sys.exit()
        
        speak("sir, do you have any other work")