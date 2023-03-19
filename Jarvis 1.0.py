import time

def greet():
    print("Welcome back, sir.")
    print("Initializing Jarvis...")
    time.sleep(2)
    print("Jarvis online and ready for duty.")

def ask_command():
    command = input("What can I do for you, sir? ")
    return command.lower()

def process_command(command):
    if "play music" in command:
        print("Playing your favorite playlist, sir.")
    elif "weather" in command:
        print("Fetching current weather information, sir.")
    elif "news" in command:
        print("Fetching latest news headlines, sir.")
    elif "time" in command:
        print("The current time is", time.strftime("%H:%M:%S"))
    elif "shutdown" in command:
        print("Shutting down Jarvis...")
        time.sleep(2)
        print("Goodbye, sir.")
        exit()
    else:
        print("I'm sorry, sir. I don't understand that command.")

if __name__ == "__main__":
    greet()
    while True:
        command = ask_command()
        process_command(command)
