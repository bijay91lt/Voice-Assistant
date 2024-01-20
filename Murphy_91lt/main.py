import subprocess
import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import ctypes
import time
import requests
import sys
from twilio.rest import Client
from ecapture import ecapture as ec
from urllib.request import urlopen
from googletrans import Translator
import pywhatkit

translator = Translator()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# import tensorflow as tf
# from keras import Sequential
# from keras.layers import SimpleRNN, Dense
# from sklearn.model_selection import train_test_split
# import pandas as pd
# import numpy as np

# # Define your model
# model = Sequential([
#   SimpleRNN(50, return_sequences=True, input_shape=(None, 1)),
#   SimpleRNN(50),
#   Dense(3, activation='softmax')
# ])

# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Assume you have collected user commands and their corresponding actions
# user_commands = ["play music", "set alarm", "turn off lights"]
# actions = ["action1", "action2", "action3"]

# # Convert user commands and actions to numerical representations
# # Here, we assume that the actions are one-hot encoded
# X = np.array([[1], [2], [3]])
# y = np.eye(len(actions))[actions]

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Train the model
# model.fit(X_train, y_train, epochs=10, batch_size=32)

# # Now, let's say a new command comes in
# new_command = np.array([[4]])

# # Predict the action for the new command
# prediction = model.predict(new_command)

# # Print the predicted action
# print(prediction)



def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Bijay !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Bijay !") 

	else:
		speak("Good Evening Bijay !") 

	asst_name =("Murph")
	speak("I am your Assistant")
	speak(asst_name)
	

def username():
	
	uname = 'Bijay'
	print("Welcome ", uname)	
	speak("How can I help you today?")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1 #pause allowed: 1 seconds.
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"Bijay: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

# def sendEmail(to, content):
# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.ehlo()
# 	server.starttls()
	
# 	# Enable low security in gmail
# 	server.login('your email id', 'your email password')
# 	server.sendmail('your email id', to, content)
# 	server.close()

def search_wikipedia():
	speak('Searching Wikipedia...')
	query = query.replace("wikipedia", "")
	results = wikipedia.summary(query, sentences = 3)
	speak("According to Wikipedia")
	print(results)
	speak(results)

def search_google():
	speak("Here's what I found on Google.")
	pywhatkit.search(query)

def search_youtube():
	speak("I will bring that up on youtube for you.")    
	pywhatkit.playonyt(query)
	
def play_music():
	music_dir = r"C:\Users\Kaker\Music"
	songs = os.listdir(music_dir)
	print(songs) 
	os.startfile(os.path.join(music_dir, songs[1]))

def time_now():
	strTime = datetime.datetime.now().strftime("%H:%M:%S") 
	speak(f"Sir, the time is {strTime}")


def time_and_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Sir, the date is {current_date}")

def open_notepad():
	codePath = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\Notepad.txt"
	os.startfile(codePath)

def exit_1():
	speak("Murph, Signing off")
	sys.exit()

def tell_joke():
	joke = pyjokes.get_joke()
	print(joke)
	speak(joke)

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
			
	speak("what language would you like to translate to")
	language = takeCommand().lower()

	if language == "japanese":
		file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to ja.csv"
		lang ='ja'

	elif language == "spanish":
		file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to es.csv"
		lang = 'es'

	elif language == "french":
		file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to fr.csv"
		lang = 'fr'

	elif language == "german":
		file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Murphy_91lt\datasets_for_translation\en to de.csv"
		lang = 'de'

	elif language == "nepali":
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

	speak("What should I translate")

	# Your text input (replace this with your desired text)
	input_text = takeCommand().lower()

	input_sentence = input_text
	translation = get_translation(input_sentence, dataset)

	print(translation)

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


def change_bg():
	folder_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\print"
	image_files=[f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

	if not image_files:
		speak("No image found")

	random_image = os.path.join(folder_path, random.choice(image_files))

	ctypes.windll.user32.SystemParametersInfoW(20, 0, random_image, 3)	
	speak("Background changed successfully")

def news():
	try:
		bbc_url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=aa553f5d9b4e46c2994f532f2fc7b962'
				
		jsonObj = urlopen(bbc_url)
		data = json.load(jsonObj)
		i = 1

		speak('Here are some top news from BBC')

		for item in data['articles']:
			print(str(i) + '. ' + item['title'] + '\n')
			print(item['description'] + '\n')
			speak(str(i) + '. ' + item['title'] + '\n')
			i += 1

	except Exception as e:
		print(str(e))

def lock_window():
	speak("locking the device")
	ctypes.windll.user32.LockWorkStation()

def shut_down():
	speak("Hold On a Sec ! Your system is on its way to shut down")
	subprocess.call('shutdown / p /f')

def empty_bin():
	winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
	speak("Recycle Bin Recycled")

def sleep():
	speak("for how much time you want to stop Murph from listening commands")
	a = int(takeCommand())
	time.sleep(a)
	print(a)

def locate(query):
	query = query.replace("where is", "")
	location = query
	speak("User asked to Locate")
	speak(location)
	webbrowser.open("https://www.google.com.np/maps/place/" + location + "")

# Mapping commands to actions
command_to_action = {
	"music": play_music,
	"time": time_now,
	"date": time_and_date,
	"notepad": open_notepad,
	"change background": change_bg,
	"news": news,
	"lock": lock_window,
	"turn off": shut_down,
	"empty bin": empty_bin,
	"sleep": sleep,
	"joke": tell_joke,
	"translate": voice_translation,
	"exit": exit_1
}


if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()
	wishMe()
	username()
	
	while True:
		
		user_commands = [ "music","time","date","notepad","change background","news","lock","shut down","empty bin","sleep","joke","translate","exit"]
		actions = ["play_music", "time_now", "time_and_date", "open_notepad", "change_bg", "news", "lock_window", "shut_down", "empty_bin", "sleep", "tell_joke", "voice_translation", "exit_1"]
		query = takeCommand().lower()

		
		if query in command_to_action:
			action = command_to_action[query]
			action()  # Execute the corresponding action

		else:
			if "wikipedia" in query:
				search_wikipedia

			elif "youtube" in query:
				search_youtube()

			elif "google" in query:
				search_google()

			elif "where is" in query:
				locate(query)
			
			# else:
			# 	speak("Sorry, I didn't get that. Could you please rephrase?")

		# elif 'email to Bijay' in query:
		# 	try:
		# 		speak("What should I say?")
		# 		content = takeCommand()
		# 		to = "Receiver email address"
		# 		sendEmail(to, content)
		# 		speak("Email has been sent !")
		# 	except Exception as e:
		# 		print(e)
		# 		speak("I am not able to send this email")

		# elif 'send a mail' in query:
		# 	try:
		# 		speak("What should I say?")
		# 		content = takeCommand()
		# 		speak("whome should i send")
		# 		to = input() 
		# 		sendEmail(to, content)
		# 		speak("Email has been sent !")
		# 	except Exception as e:
		# 		print(e)
		# 		speak("I am not able to send this email")
			
		# elif "calculate" in query: 
			
		# 	app_id = "Wolframalpha api id"
		# 	client = wolframalpha.Client(app_id)
		# 	indx = query.lower().split().index('calculate') 
		# 	query = query.split()[indx + 1:] 
		# 	res = client.query(' '.join(query)) 
		# 	answer = next(res.results).text
		# 	print("The answer is " + answer) 
		# 	speak("The answer is " + answer) 


		# elif 'power point presentation' in query:
		# 	speak("opening Power Point presentation")
		# 	power = r"C:\\Users\\Bijay\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
		# 	os.startfile(power)

		if "camera" in query or "take a photo" in query:
			ec.capture(0, "Murph Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('Murph_notes.txt', 'w')
			strTime = datetime.datetime.now().strftime("%H:%M:%S") 
			file.write(f"{strTime} :- {note}")
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("Murph_notes.txt", "r") 
			print(file.read())
			speak(file.read(6))

		elif "weather" in query:
			# Google Open weather website
			# to get API of Open weather 
			api_key = "25a3bb3d5afa9f62331fcdc01dc892cf"
			base_url = "https://api.openweathermap.org"
			speak("City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name
			response = requests.get(complete_url) 
			x = response.json() 
			
			if 'cod' in x and x['cod'] != "404" and 'main' in x: 
				y = x["main"] 
				current_temperature = y.get("temp")
				current_pressure = y.get("pressure")
				current_humidity = y.get("humidity")
				z = x["weather"] 
				weather_description = z[0].get("description")
				if all(item is not None for item in [current_temperature, current_pressure, current_humidity, weather_description]):
					print("Temperature (in kelvin unit) =", current_temperature)
					print("Atmospheric pressure (in hPa unit) =", current_pressure)
					print("Humidity (in percentage) =", current_humidity)
					print("Description =", weather_description)
				else:
					speak("Weather information not available.")
			else: 
				speak("City Not Found")


			
		elif "send message " in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)
				print(message.sid)

		elif "what is" in query or "who is" in query:
			
			# Use the same API key 
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		# elif "" in query:
			# Command go here
			# For adding more commands