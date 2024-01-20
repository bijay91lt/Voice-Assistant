import tkinter as tk
from tkinter import Scrollbar, Text
import threading
import time
import speech_recognition as sr
import subprocess

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant App")
        self.root.geometry("600x400")

        self.text_box = Text(self.root, wrap="word", width=40, height=10)
        self.text_box.pack(pady=20)

        self.scrollbar = Scrollbar(self.root, command=self.text_box.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.text_box.config(yscrollcommand=self.scrollbar.set)

        self.start_button = tk.Button(self.root, text="Start Assistant", command=self.start_assistant)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Assistant", command=self.stop_assistant)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

        self.recognizer = sr.Recognizer()
        # ... (same as before)

    def start_assistant(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.thread = threading.Thread(target=self.listen_and_process)
        self.thread.start()

    def stop_assistant(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        if hasattr(self, 'thread') and self.thread.is_alive():
            self.thread.join()

    def listen_and_process(self):
        with sr.Microphone() as source:
            self.text_box.insert(tk.END, "Listening...\n")
            self.text_box.update_idletasks()

            try:
                audio_data = self.recognizer.listen(source, timeout=5)
                query = self.recognizer.recognize_google(audio_data)
                self.text_box.insert(tk.END, f"You said: {query}\n")
                self.text_box.update_idletasks()

                # Check for a specific command to execute main.py
                if "run main program" in query.lower():
                    self.execute_main_program()

            except sr.UnknownValueError:
                self.text_box.insert(tk.END, "Sorry, I couldn't understand that.\n")
                self.text_box.update_idletasks()

            except sr.RequestError as e:
                self.text_box.insert(tk.END, f"Error connecting to Google API: {e}\n")
                self.text_box.update_idletasks()

            time.sleep(2)  # Pause for readability, remove in a real implementation

    def execute_main_program(self):
        try:
            # Replace 'python' with 'python3' if needed
            subprocess.run(["python", "main.py"])
        except Exception as e:
            self.text_box.insert(tk.END, f"Error executing main.py: {e}\n")
            self.text_box.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()