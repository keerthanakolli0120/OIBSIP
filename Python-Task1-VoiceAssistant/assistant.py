import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("I am listening.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I didn't understand. Please try again.")
        return ""


command = listen()

if "hello" in command:
    speak("Hello! How are you?")

elif "time" in command:
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)

elif "date" in command:
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + today)

elif "search" in command:
    topic = command.replace("search", "").strip()
    speak("Searching for " + topic)
    webbrowser.open(
        "https://www.google.com/search?q=" + topic
    )

elif "how are you" in command:
    speak("I am doing great. Thank you for asking.")

elif "your name" in command:
    speak("My name is Oasis Voice Assistant.")

elif "open youtube" in command:
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

elif "open google" in command:
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

elif "thank you" in command:
    speak("You are welcome.")

elif "bye" in command or "exit" in command or "stop" in command:
    speak("Goodbye. Have a nice day.")

else:
    speak("Sorry, I don't know that command yet.")