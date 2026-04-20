import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import os
import platform
import urllib.parse
import pywhatkit
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Init
recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = os.getenv("NEWS_API_KEY")

def speak(text):
    print(f"Jarvis: {text}")
    try:
        engine.stop()
    except:
        pass

    if platform.system() == "Darwin":
        os.system(f'say "{text}"')
    else:
        engine.say(text)
        engine.runAndWait()

# Play ANY song 
def play_song(song):
    try:
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)   
    except Exception as e:
        print("Song Error:", e)
        speak("Error playing song")

#  Open ANY website
def open_website(site):
    speak(f"Opening {site}")
    query = urllib.parse.quote(site)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#  News
def get_news():
    if not newsapi:
        speak("API key is missing")
        return

    speak("Fetching latest news")

    try:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?language=en&apiKey={newsapi}"
        )

        data = r.json()
        articles = data.get("articles", [])

        if not articles:
            speak("No news available")
            return

        for article in articles[:10]:
            speak(article["title"])

            print("Say 'stop' to stop news...")
            stop_command = listen()

            if stop_command and "stop" in stop_command.lower():
                speak("Stopping news")
                break

    except Exception as e:
        print("News Error:", e)
        speak("Error fetching news")

# Command handler
def processCommand(command):
    command = command.lower()

    if command.startswith("play"):
        song = command.replace("play", "").strip()
        if song:
            play_song(song)
        else:
            speak("Please tell me the song name")

    elif command.startswith("open"):
        site = command.replace("open", "").strip()
        if site:
            open_website(site)
        else:
            speak("Please tell me what to open")

    elif "news" in command:
        get_news()

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that")

#  Listen
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command

    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        speak("Sorry, I could not understand")
    except Exception as e:
        print("Error:", e)

    return None

#  Main
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        print("Say 'Jarvis' to activate...")

        word = listen()

        if word and "jarvis" in word.lower():
            speak("Yes")

            command = listen()
            if command:
                processCommand(command)