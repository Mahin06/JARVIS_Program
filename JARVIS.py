import pyttsx3
import pyautogui as pyg
import speech_recognition as sr
from requests import get
import os
import webbrowser
import pyjokes as pj
import wikipedia
import datetime as dt


engine = pyttsx3.init('sapi5')
volume = engine.getProperty('volume')
voice = engine.getProperty('voices')
rate = engine.getProperty('rate')

engine.setProperty('volume', 0.5)
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 180)


def speak(content):
    engine.say(content)
    engine.runAndWait()

def command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 0.6
        recognizer.energy_threshold = 500
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        QUERY = recognizer.recognize_google(audio, language='en-in')
        print(f"You said : {QUERY.lower()}")
    except Exception as e:
        speak("say that again sir")
        return "none"
    return QUERY

def commandstr():
    input_ = input('Command : ')
    return input_.lower()

def openfile():
    previous_path = os.getcwd()
    os.chdir('C:/')
    tries = 3
    while tries > 0:
        chosen_file = QUERY_()
        filename = chosen_file.capitalize()
        try:
            os.startfile(filename)
            os.chdir(previous_path)
            break
        except Exception as e:
            speak('file not recognised, can you say it again')
            tries -= 1
            continue
    if tries < 1:
        speak('sorry sir, operation is aborted due to multiple fails')

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=59bfb1b1764b4a21896ecc79b2eb29d3'
    main_page = get(main_url).json()
    articles = main_page["articles"]
    head = []
    for article in articles:
        head.append(article["title"])
    for i in range(1,6):
        print(f"another news is : {head[i]}")
        speak(f"another news is {head[i]}")

    speak('do you want to know more')
    answer = QUERY_().lower()
    if 'yes' in answer:
        for article in articles:
            head.append(article["title"])
        for i in range(1,6):
            print(f"another news is : {head[i]}")
            speak(f"another news is {head[i]}")


if __name__ == "__main__":
    QUERY_ = command
    speak("Do you want to talk via voice? : ")
    userChoice = input("Do you want to talk via message? : ")

    if 'no' in userChoice:
        QUERY_ = commandstr
    else:
        QUERY_ = command

    while True:
        QUERY = QUERY_().lower()

        if 'hello' in QUERY:
            speak('hello sir, nice to see you again')

        elif 'are you listening' in QUERY or 'jarvis?' in QUERY:
            speak('yes sir? what do u want?')
        
        elif 'who are you' in QUERY:
            speak('i am your personal voice assisstent')

        elif 'change' in QUERY and 'your rate' in QUERY:
            speak('what should be the rate?')
            rateset = QUERY_().lower()
            if 'decrease' in rateset:
                new_rate = rate-50
                set_rate = engine.setProperty('rate', new_rate)
                speak('rate is changed')
            elif 'increase' in rateset:
                new_rate = rate+50
                set_rate = engine.setProperty('rate', new_rate)
                speak('rate is changed')
            elif 'default' in rateset:
                engine.setProperty('rate', rate)
                speak('rate is changed to default')
            else:
                speak("i didn't understand")

        elif 'change' in QUERY and 'your volume' in QUERY:
            speak('what should be the volume?')
            volset = QUERY_().lower()
            if 'full' in volset:
                engine.setProperty('volume', 1)
                speak(f"volume changed to full")
            elif 'half' in volset:
                engine.setProperty('volume', 0.5)
                speak(f"volume changed to half")
            elif 'mute' in volset:
                engine.setProperty('volume', 0)
                speak(f"volume muted")
            else:
                speak("i didn't understand")

        elif 'ip address' in QUERY or 'my ip' in QUERY:
            print(f"Your IP Address is {get('https://api.ipify.org').text}")
            speak(f"your ip address is")
            engine.setProperty('rate', 100)
            speak(get('https://api.ipify.org').text)
            engine.setProperty('rate', rate)

        elif 'switch to friday' in QUERY or 'i want friday' in QUERY:
            try:
                engine.setProperty('voice', voice[1].id)
                speak('hello sir, i am friday, your another voice assistant')
            except Exception as e:
                speak('operation failed sir, maybe there is a problem')

        elif 'open' in QUERY and 'file' in QUERY:
            speak('which file you want to open')
            try:
                openfile()
            except Exception as e:
                speak("i can't the file. maybe there is a problem")
        
        elif 'wikipedia' in QUERY and 'search' in QUERY:
            try:
                speak('searching wikipedia')
                QUERY = QUERY.replace("wikipedia", "")
                results = wikipedia.summary(QUERY, sentences=3)
                speak('according to wikipedia')
                print(results)
                speak(results)
            except Exception as e:
                speak('sorry sir, an error occured')

        elif 'switch to jarvis' in QUERY or 'i want jarvis' in QUERY:
            try:
                engine.setProperty('voice', voice[0].id)
                speak('hello sir, i am jarvis, your another voice assistant')
            except Exception as e:
                speak('operation failed sir, maybe there is a problem')

        elif 'go away' in QUERY or 'bye jarvis' in QUERY:
            speak('ok sir, run this program if you want something')
            break
    
        elif 'what time' in QUERY :
            speak(f'its {dt.datetime.now().strftime("%I:%M")}')
        
        elif 'day today' in QUERY:
            speak(f"its {dt.date.today().strftime('%A')}")
            print(f"its {dt.date.today().strftime('%A')}")
        
        elif 'date today' in QUERY:
            speak(f'its {dt.datetime.now().date()}')
            print(f'its {dt.datetime.now().date()}')
        
        elif 'date yesterday' in QUERY:
            speak(f'yesterday was {dt.date.today() - dt.timedelta(days=1)}')
            print(f'yesterday was {dt.date.today() - dt.timedelta(days=1)}')
        
        elif 'date tomorrow' in QUERY:
            speak(f"{dt.date.today() + dt.timedelta(days=1)}")
            print(f"{dt.date.today() + dt.timedelta(days=1)}")
        
        elif 'take' in QUERY and 'screenshot' in QUERY:
            speak("what should be the name of the file")
            filename = QUERY_().lower()
            speak('taking screenshot')
            img = pyg.screenshot()
            img.save(f"{filename}.png")
            speak('screenshot has been saved in your current directory')
        
        elif 'hide' in QUERY and 'files' in QUERY:
            speak('sir, please tell me if i have to make files hidden or visible')
            answer = commandstr().lower()
            if 'hide' in answer:
                os.system("attrib +h /s /d")
                speak('all files are hidden sir')
            elif 'visible' in answer:
                os.system("attrib -h /s /d")
                speak('all files are visible now')
            else:
                speak('operation failed')
        
        elif 'tell' in QUERY and 'joke' in QUERY:
            joke = pj.get_joke()
            print(joke)
            speak(joke)
        
        elif 'was i supposed to laugh' in QUERY:
            speak('sorry sir for the bad joke')
        
        elif 'shut down the system' in QUERY:
            os.system("shutdown /s /t 5")
        elif 'restart the system' in QUERY:
            os.system("shutdown /r /t 5")
        elif 'sleep the system' in QUERY:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif 'where am i' in QUERY or 'my location' in QUERY:
            speak('wait sir, let me find')
            try:
                ip_address = get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ip_address+'.json'
                geo_request = get(url)
                geo_data = geo_request.json()
                city = geo_data['city']
                # state = geo_data['state'] #this command may give you error
                country = geo_data['country']
                speak(f'we are in {city} city of {country} country')
            except Exception as e:
                speak('sorry sir, network error occured')
            
        elif 'open youtube' in QUERY:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')
        elif 'open facebook' in QUERY:
            speak('opening facebook')
            webbrowser.open('www.facebook.com')
        elif 'open twitter' in QUERY:
            speak('opening twitter')
            webbrowser.open('www.twitter.com')
        elif 'open instagram' in QUERY:
            speak('opening instagram')
            webbrowser.open('www.instagram.com')
        elif 'open github' in QUERY:
            speak('opening github')
            webbrowser.open('https://github.com/')
        elif 'open fiver' in QUERY:
            speak('opening fiver')
            webbrowser.open('https://www.fiverr.com/users/mahinmirza06/seller_dashboard')
        elif 'open google' in QUERY:
            speak('sir, may i search? :')
            answer = QUERY_().lower()
            if 'no' in answer:
                speak('ok sir, opening google')
                webbrowser.open('www.google.com')
            elif 'yes' in answer:
                speak('what do you want to know')
                command_to_search = QUERY_().lower()
                webbrowser.open(f"{command_to_search}")
            else:
                speak('maybe you want to search')
                speak('opening google')
                webbrowser.open('www.google.com')

        elif 'switch' in QUERY and "window" in QUERY:
            pyg.keyDown("alt")
            pyg.press("tab")
            pyg.sleep(1)
            pyg.keyUp("alt")

        elif 'news' in QUERY:
            speak("please wait sir, data fetching may take some minute")
            try:
                news()
            except Exception as e:
                speak('an error occured, you can check or change it in jarvis.py')

        else:
            speak("i didn't understand")
