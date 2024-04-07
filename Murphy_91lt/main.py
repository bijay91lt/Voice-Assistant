#Main file of Voice Assistant
#git add .
#git commit -m "Add new feature"
#git push origin main

from flask import Flask, render_template, request
from packages.Va_Functions import VA_func

app = Flask(__name__)

app.static_url_path= '/static'
app.static_folder = 'static'


va1 = VA_func()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_command', methods=['POST'])
def submit_command():
    
    data = request.get_json()
    command = data['command'].lower()
    response = handle_command(command)
    return response

def handle_command(command):
    if "wikipedia" in command:
        return va1.search_wikipedia(command)
    elif "hello" in command:
        return va1.wish_me()
    elif "google" in command:
        return va1.search_google(command)
    elif "youtube" in command:
        return va1.search_youtube(command)
    elif "music" in command:
        return va1.play_music()
    elif "time" in command:
        return va1.time_now()
    elif "date" in command:
        return va1.time_and_date()
    elif "notepad" in command:
        return va1.open_notepad()
    elif "exit" in command:
        return va1.exit_assistant()
    elif "joke" in command:
        return va1.tell_joke()
    elif "translation" in command:
        return va1.voice_translation()
    elif "background" in command:
        return va1.change_bg()
    elif "news" in command:
        return va1.news()
    elif "lock" in command:
        return va1.lock_window()
    elif "shutdown" in command:
        return va1.shut_down()
    elif "recycle bin" in command:
        return va1.empty_bin()
    elif "sleep" in command:
        return va1.sleep()
    elif "where is" in command:
        return va1.locate(command)
    elif "picture" in command or "photo" in command:
        return va1.camera()
    elif "take a note" in command:
        return va1.write_note()
    elif "show note" in command:
        return va1.show_note()
    elif "restart" in command:
        return va1.restart()
    elif "logout" in command:
        return va1.logout()
    elif "weather" in command:
        return va1.get_weather()
    else:
        return "Sorry, I didn't get that. Can you repeat?"

if __name__ == '__main__':
    app.run(debug=True)