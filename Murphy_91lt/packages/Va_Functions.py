import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import subprocess
import winshell
import ctypes
import json
import random
import time
import requests
import threading
from ecapture import ecapture as ec
from urllib.request import urlopen



class VA_func:
    @staticmethod
    def speak(text):
        """Speaks the provided text using the text-to-speech engine."""
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def take_command():
        """Listens for user input and returns the recognized text."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"User Command: {command}")
            return command
        except Exception as e:
            print(f"Error recognizing voice: {e}")
            return ""

    @staticmethod
    def wish_me(username):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            message = f"Good Morning, {username}. I am your Voice Assistant. How may I help you?"
        elif 12 <= hour < 18:
            message = f"Good Afternoon, {username}. I am your Voice Assistant. How may I help you?"
        else:
            message = f"Good Evening, {username}. I am your Voice Assistant. How may I help you?"
        
        VA_func.speak(message)  # Assuming you have a speak() method in your VA_func class
        return message


    @staticmethod
    def search_wikipedia(query):
        VA_func.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        VA_func.speak("According to Wikipedia")
        VA_func.speak(results)
        return results

    @staticmethod
    def search_google(query):
        VA_func.speak("Here's what I found on Google.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return "Displaying Google Results..."

    @staticmethod
    def search_youtube(query):
        VA_func.speak("I will bring that up on youtube for you.")
        pywhatkit.playonyt(query)
        return "Playing Youtube Video..."

    @staticmethod
    def play_music():
        music_dir = r"C:\Users\Kaker\Music"
        songs = os.listdir(music_dir)
        print(songs) 
        os.startfile(os.path.join(music_dir, songs[1]))
        return "Playing Music..."

    @staticmethod
    def time_now():
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        VA_func.speak(f"Sir, the time is {str_time}")
        return "The time is " + str_time

    @staticmethod
    def time_and_date():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        VA_func.speak(f"Sir, the date is {current_date}")
        return "The date is " + current_date

    @staticmethod
    def open_notepad():
        code_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Github\Voice-Assistant\Murphy_91lt\packages\Notepad.txt"
        os.startfile(code_path)
        return "Notepad Opened"

    @staticmethod
    def tell_joke():
        joke = pyjokes.get_joke()
        VA_func.speak(joke)
        return joke

    @staticmethod
    def change_bg():
        folder_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\print"
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        if not image_files:
            VA_func.speak("No image found")

        random_image = os.path.join(folder_path, random.choice(image_files))

        ctypes.windll.user32.SystemParametersInfoW(20, 0, random_image, 3)
        VA_func.speak("Background changed successfully")
        return "Background Changed Successfully..."

    @staticmethod
    def news():
        try:
            bbc_url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=aa553f5d9b4e46c2994f532f2fc7b962'

            jsonObj = urlopen(bbc_url)
            data = json.load(jsonObj)
            i = 1

            VA_func.speak('Here are some top news from BBC')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                VA_func.speak(str(i) + '. ' + item['title'] + '\n')
                i += 1

        except Exception as e:
            print(str(e))
        
        return "Playing News..."

    @staticmethod
    def lock_window():
        VA_func.speak("Locking the device")
        ctypes.windll.user32.LockWorkStation()
        return None

    @staticmethod
    def shut_down():
        VA_func.speak("Hold On a Sec! Your system is on its way to shut down")
        subprocess.call('shutdown /p /f')
        return None

    @staticmethod
    def empty_bin():
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        VA_func.speak("Recycle Bin emptied")
        return "Recycle Bin emptied..."

    @staticmethod
    def sleep():
        VA_func.speak("For how much time do you want to stop Murph from listening to commands?")
        time.sleep(int(VA_func.take_command()))
        return "Sleeping..."

    @staticmethod
    def locate(query):
        query = query.replace("where is", "")
        location = query
        VA_func.speak("User asked to locate")
        VA_func.speak(location)
        webbrowser.open(f"https://www.google.com/maps/place/{location}")
        return "Location Found..."

    @staticmethod
    def camera():
        def capture_image():
            ec.capture(0, "Murph Camera ", "img.jpg")
        
        # Create a thread to execute the capture_image function
        camera_thread = threading.Thread(target=capture_image)
        camera_thread.start()
        camera_thread.join()
        return None
        

    @staticmethod
    def restart():
        subprocess.call(["shutdown", "/r"])
        return None

    @staticmethod
    def logout():
        VA_func.speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])
        return None

    @staticmethod
    def write_note():
        VA_func.speak("What should i write, sir")
        note = VA_func.take_command()
        file = open(r'packages\Murph_notes.txt', 'w')
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        file.write(f"{strTime} :- {note}")
        return "Writing Note..."
    
    @staticmethod
    def show_note():
        VA_func.speak("Showing Notes")
        file = open(r"packages\Murph_notes.txt", "r") 
        print(file.read())
        VA_func.speak(file.read(6))
        return "Showing Notes..."

    @staticmethod
    def get_weather():
        VA_func.speak("Tell me the location")
        location = VA_func.take_command()
        base_url = "http://dataservice.accuweather.com/currentconditions/v1/"
        params = {
            "apikey": "hr6ctCtWHxxRMFr2jdwRvmuOY4hKY2Tr",
            "q": location,
            "language": "en-us",
            "details": "true"
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            VA_func.speak(data[0])  # Return the first result (current conditions)
        except requests.exceptions.RequestException as e:
            VA_func("Error:", e)
        
        return None

    @staticmethod
    def voice_translation():
        from gtts import gTTS
        import csv
        from io import BytesIO
        import pygame
        import time
        
        error = "No translation in dataset"

        def load_dataset(file_path):
            dataset = []
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    dataset.append(row)
            return dataset

        def get_translation(english_sentence, dataset):
            for pair in dataset:
                if pair[0] == english_sentence:
                    return pair[1]
            return error
                
        VA_func.speak("What language would you like to translate to")
        language = VA_func.take_command().lower()

        if "japanese" in language:
            file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to ja.csv"
            lang ='ja'

        elif "spanish" in language:
            file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to es.csv"
            lang = 'es'

        elif "french" in language:
            file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to fr.csv"
            lang = 'fr'

        elif "german" in language:
            file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to de.csv"
            lang = 'de'

        elif "nepali" in language:
            file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to ne.csv"
            lang = 'ne'

        else:
            raise ValueError("Language not recognized.")
                    
        dataset = load_dataset(file_path)

        # Initialize pygame mixer
        pygame.mixer.init()

        # Set the voice (you can adjust the index based on your preference)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load("output.mp3")  # Load a blank audio file

        VA_func.speak("What should I translate")

        # Your text input (replace this with your desired text)
        input_text = VA_func.take_command().lower()

        input_sentence = input_text
        translation = get_translation(input_sentence, dataset)

        # Use gTTS to convert the translated text into speech
        tts = gTTS(translation, lang)

        # Save the gTTS audio to a BytesIO buffer
        buffer = BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)

        # Play the gTTS audio using pygame
        pygame.mixer.music.load(buffer)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        return translation