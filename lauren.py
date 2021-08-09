import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<21:
        speak("Good Evening!")   

    else:
        speak("Good Night!")  

    speak("I am Lauren . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("please say that again ma'am...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('riyadutta24556@gmail.com', 'iamajealousperson')
    server.sendmail('riyadutta24556@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Ma'am, what should I search on google")
            cm=takeCommand()
            webbrowser.open(f"{cm}")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open twitter" in query:
            webbrowser.open("twitter.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\indian\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "shubhanjanbarai18@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Riya Ma'am . I am not able to send this email")    

        elif " no thanks" in query:
            speak("Thanks for using me ma'am , have a good day.")
            sys.exit()

        