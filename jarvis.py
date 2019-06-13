import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random 
names= {
    "sam":'mkumar.sgnr96@gmail.com',
    "jadu":'mkmau.sgnr97@gmail.com',
    "aman":"asoni5024@gamil.com"
}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour <18:
        speak("Good Afternooon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis Sir, Please Tell me how may i help You..")

def takeCommand():
    """it take mic input from user and returns string output"""
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold= 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        print(e)

        print("Say that Again Please...")
        return "None"
    return query

def sendEmail(to,content):
    with open('mypr.txt') as f:
        a= f.read()
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('mkumar.sgnr97@gmail.com', a)
    server.sendmail('mkumar.sgnr97@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching Wikipedia...")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("openning youtube..")
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak("openning google..")
            webbrowser.open("www.google.com")

        elif 'play music' in query:
            music_dir='F:\\audio\\jarvis_songs'
            songs = os.listdir(music_dir)
            random_number = random.randint(0,139)
            speak(f"Playing.. {songs[random_number]}")
            print(songs[random_number])
            mu = os.startfile(os.path.join(music_dir,songs[random_number]))

        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'visual studio' in query:            
            speak("openning visual studio code..")
            codepath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'email' in query:
            try:
                speak("To whom should i send this email ?")
                email_to = takeCommand().lower()

                for i in names:
                    try:
                        if i in email_to:
                            print(email_to)
                            speak(f"Sending Email to {i}")
                            key  = i

                    except Exception as e:
                        speak("i Dont know the person sorry")

                to = names[key]
                speak("What shoul i say?")
                content = takeCommand()
                sendEmail(to,content)
                speak(f"your Email to {key} has been sent!")
                print(f"Sending Email to :{to}")

            except Exception as e:
                speak("sorry my friend Sam , i am not able to send this email")

        elif 'exit' in query:
            speak("bye sir, thank you")
            exit()



        
         
