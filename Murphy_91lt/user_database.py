import sqlite3
import hashlib

class UserDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                username TEXT UNIQUE,
                                password TEXT
                            )''')
        self.connection.commit()

    def register_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hashed_password))
        self.connection.commit()

    def verify_credentials(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, hashed_password))
        return self.cursor.fetchone() is not None

# Example usage:
db = UserDatabase('user_credentials.db')
# Register user
db.register_user('user1', 'password123')  # Example registration
# Verify credentials
if db.verify_credentials('user1', 'password123'):
    print("Login successful")
else:
    print("Invalid username or password")
