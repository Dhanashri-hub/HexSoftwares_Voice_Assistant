import datetime

def greet_user():
    print("Hello! I am your Voice Assistant.")
    print("How can I help you today?")

def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Current time is {time}")

def get_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    print(f"Today's date is {date}")

def help_menu():
    print("\nAvailable Commands:")
    print("time  - Get current time")
    print("date  - Get today's date")
    print("greet - Greeting message")
    print("exit  - Exit assistant\n")

def voice_assistant():
    greet_user()
    help_menu()

    while True:
        command = input("Enter your command: ").lower()

        if command == "time":
            get_time()
        elif command == "date":
            get_date()
        elif command == "greet":
            greet_user()
        elif command == "help":
            help_menu()
        elif command == "exit":
            print("Thank you for using the Voice Assistant. Goodbye!")
            break
        else:
            print("Sorry, command not recognized. Type 'help'.")

voice_assistant()
