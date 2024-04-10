#Main file of Voice Assistant
#git add .
#git commit -m "Add new feature"
#git push origin main

from flask import Flask, render_template, request, jsonify
from packages.Va_Functions import VA_func

app = Flask(__name__)

app.static_url_path= '/static'
app.static_folder = 'static'


va = VA_func() 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_command', methods=['POST'])
def submit_command():
    
    data = request.get_json()
    command = data['command'].lower()
    response_text = handle_command(command)
    if response_text is None:
        response_text = "No response from the Voice Assistant."
    return jsonify({'output_text': response_text})

def handle_command(command):
    response_text = None
    if "wikipedia" in command:
        response_text = va.search_wikipedia(command)
    elif "hello" in command:
        response_text = va.wish_me()
    elif "google" in command:
        response_text = va.search_google(command)
    elif "youtube" in command:
        response_text = va.search_youtube(command)
    elif "music" in command:
        response_text = va.play_music()
    elif "time" in command:
        response_text = va.time_now()
    elif "date" in command:
        response_text = va.time_and_date()
    elif "notepad" in command:
        response_text = va.open_notepad()
    elif "joke" in command:
        response_text = va.tell_joke()
    elif "translation" in command:
        response_text = va.voice_translation()
    elif "background" in command:
        response_text = va.change_bg()
    elif "news" in command:
        response_text = va.news()
    elif "lock" in command:
        response_text = va.lock_window()
    elif "shutdown" in command:
        response_text = va.shut_down()
    elif "recycle bin" in command:
        response_text = va.empty_bin()
    elif "sleep" in command:
        response_text = va.sleep()
    elif "where is" in command:
        response_text = va.locate(command)
    elif "picture" in command or "photo" in command:
        response_text = va.camera()
    elif "take a note" in command:
        response_text = va.write_note()
    elif "show note" in command:
        response_text = va.show_note()
    elif "restart" in command:
        response_text = va.restart()
    elif "logout" in command:
        response_text = va.logout()
    elif "weather" in command:
        response_text = va.get_weather()
    else:
        response_text = "Sorry, I didn't get that. Can you repeat?"
        va.speak("Sorry, I didn't get that. Can you repeat?")
    
    return response_text
    

if __name__ == '__main__':
    app.run(debug=True)