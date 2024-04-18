#Main file of Voice Assistant
#git add .
#git commit -m "Add new feature"
#git push origin main

from flask import Flask, render_template, request, jsonify, redirect, g, flash
from packages.Va_Functions import VA_func
import sqlite3

app = Flask(__name__)
app.secret_key = 'qwertyuiop1234567890'

app.static_url_path= '/static'
app.static_folder = 'static'


va = VA_func() 

# Connect to SQLite database
DATABASE = 'users.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the login form
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Connect to the SQLite database and query for user
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    if user:
        # If a user with matching credentials is found, redirect to index.html
        welcome_message = va.wish_me(username)  # Call wish_me function with username
        return render_template('index.html', welcome_message=welcome_message)
    else:
        # If no matching user is found, render the login page again with an error message
        return render_template('login.html', error='Invalid username or password')


# Define the route for the forgot password page
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Get the username and new password from the form
        username = request.form['username']
        new_password = request.form['new_password']
        
        # Connect to the SQLite database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Check if the username exists in the database
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        
        if user:
            # If the username exists, update the password
            cursor.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
            conn.commit()
            conn.close()
            return render_template('login.html', success='Password reset successfully. Please login with your new password.')
        else:
            # If the username does not exist, render the forgot password page with an error message
            conn.close()
            return render_template('forgot_password.html', error='Username not found. Please enter a valid username.')
    else:
        # If the request method is GET, render the forgot password page
        return render_template('forgot_password.html')

# Define the route for the index page
@app.route('/index')
def index():
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
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            # Username already exists, handle the error (e.g., display a message to the user)
            return "Username already exists. Please choose a different username."
        else:
            # Insert data into users table
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            
            # Redirect to the login page
            return redirect('/')
    
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)