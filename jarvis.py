import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha

app = wolframalpha.Client("WAA29E-PPU8K9L47J")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or 'tell me' in query or 'do you know' in query:
            speak('Just a minute sir')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("okay     sir, following your command")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

        elif 'open google' in query:
            speak("okay     sir, following your command")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

        elif 'open stack overflow' in query:
            speak("okay     sir, following your command")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(
        "http://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2019.3.2/bin/idea64.exe"
            os.startfile(codePath)

        elif 'weather' in query:
            res = app.query("weather in banka")
            nes = (next(res.results).text)

            if int(nes[14]) > 5 and int(nes[14]) < 10:
                speak(
                    "Alright, ....... sir right now  at your place  " + nes + " and I suggest you to be in your  blanket, if you wanna play safe hand")
        elif 'temperature' in query:
            res = app.query("temperature in banka")
            nes = (next(res.results).text)
            if int(nes[0]) > 5 and int(nes[0]) < 10:
                speak(
                    "Alright, ....... sir right now temperature at your place is  " + nes + " and it's really chilly outside, I suggest you to be here and have a cup of hot tea")
            if int(nes[0]) > 10 and int(nes[0]) < 15:
                speak("It seems that temperature right now is" + nes + "but it will be a sunny day ahead")
            else:
                speak("Sir the temperature is " + nes + "and it's probable that you will go outside to enjoy the day")


        else:
            res = app.query(query)
            speak(next(res.results).text)