#Main file of Voice Assistant
from packages.Va_Functions import VA_func


def main():
    va1 = VA_func()
    va1.wish_me()

    while True:
        command = va1.take_command().lower()

        if "wikipedia" in command:
            va1.search_wikipedia(command)
        elif "google" in command:
            va1.search_google(command)
        elif "youtube" in command:
            va1.search_youtube(command)
        elif "music" in command:
            va1.play_music()
        elif "time" in command:
            va1.time_now()
        elif "date" in command:
            va1.time_and_date()
        elif "notepad" in command:
            va1.open_notepad()
        elif "exit" in command:
            va1.exit_assistant()
        elif "joke" in command:
            va1.tell_joke()
        elif "translation" in command:
            va1.voice_translation()
        elif "background" in command:
            va1.change_bg()
        elif "news" in command:
            va1.news()
        elif "lock" in command:
            va1.lock_window()
        elif "shutdown" in command:
            va1.shut_down()
        elif "empty bin" in command:
            va1.empty_bin()
        elif "sleep" in command:
            va1.sleep()
        elif "where is" in command:
            va1.locate(command)
        elif "picture" in command or "photo" in command:
            va1.camera()
        elif "take a note" in command:
            va1.write_note()
        elif "show note" in command:
            va1.show_note()
        elif "restart" in command:
            va1.restart()
        elif "logout" in command:
            va1.logout()
        elif "weather" in command:
            va1.get_weather()
        else:
            va1.speak("Sorry, I didn't get that. Can you repeat?")
            
if __name__ == "__main__":
    main()