import pyttsx3 as p
import speech_recognition as sr
import time
from News import *
import randfacts
from Jokes import *
from Weather import *
from datetime import datetime
from Quotes import get_quote

engine = p.init()
engine.setProperty('rate', 180)
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
speak("Hello Mam, I am your voice Assistant. How are you?")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" in text and "about" in text and "you" in text:
    speak("I am also having a good day, Mam.")


while True:
    speak("What can I do for you?")  

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)


    if "information" in text:
        speak("You need information related to which topic?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening...")
            audio = r.listen(source)
            topic = r.recognize_google(audio)
            from selenium_web import infow
        speak(f"Searching {topic} in Wikipedia.")
        print(f"Searching {topic} in Wikipedia.")

        assist = infow()
        assist.get_info(topic)

    elif "play" in text and "video" in text:
        speak("You want me to play which video?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening...")
            audio = r.listen(source)
            
            try:
                vid = r.recognize_google(audio)
                print(f"Recognized command to play: {vid}")  
                
                from YT_code import Music
                assist = Music()
                time.sleep(1)  
                
                if vid:  
                    assist.play(vid)  
                    time.sleep(100000)
                else:
                    print("No video title recognized.")  

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand.")
                speak("Sorry, I couldn't understand. Could you please repeat?")
            
            except sr.RequestError:
                print("Issue connecting to the recognition service.")
                speak("I'm having trouble connecting to the recognition service.")

    elif "news" in text:
        print("Sure, Mam. I will read the news for you...")
        speak("Sure, Mam. I will read the news for you...")
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif "fact" in text or "facts" in text:  
        speak("Sure, Mam.")
        x = randfacts.get_fact()
        print(x)
        speak("Did you know that " + x)

    elif "joke" in text or "jokes" in text:  
        speak("Get ready for some chuckles!")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])

    elif "weather" in text:
        speak("Please tell me the city name.")
        with sr.Microphone() as source:
            audio = r.listen(source)
            city_name = r.recognize_google(audio)
            print(f"City recognized: {city_name}")
            
            weather_info = get_weather(city_name)
            print(weather_info)
            speak(weather_info)
    elif "quote" in text or "motivation" in text:
        quote = get_quote()
        print(quote)
        speak(quote)
    
    

    elif "date" in text or "time" in text:
        current_date = datetime.now().strftime("%B %d, %Y") if "date" in text else ""
        current_time = datetime.now().strftime("%I:%M %p") if "time" in text else ""
        
        response = f"{'Today\'s date is ' + current_date if current_date else ''}" \
                   f"{' and ' if current_date and current_time else ''}" \
                   f"{'the current time is ' + current_time if current_time else ''}"

        print(response)
        speak(response)
    



    elif "no" in text or "nothing" in text:
        speak("Alright, have a great day!")
        break

    else:
        speak("Sorry, I didn't understand that. Please tell me again.")


