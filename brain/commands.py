def hello():
    print("FRIDAY: Hello, Nekkanti Jahnavi!")

def greet():
    date =datetime.now().date
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    print("=" * 50)
    print("        F.R.I.D.A.Y. v0.0.1 Alpha")
    print("Future-Ready Intelligent Digital Assistant")
    print("=" * 50)
    print(f"{greeting}, Nekkanti Jahnavi.")
    print("I am FRIDAY.")
    print("Ready to assist.")
    print("=" * 50)

    from datetime import datetime

def show_time():
    current = datetime.now().strftime("%I:%M %p")
    print(f"FRIDAY: {current}")

def command_center():
    while True:
        command = input("\nYou: ").lower()

        if command == "hello":
            hello()

        elif command == "date":
            show_date()

        elif command == "time":
            show_time()

        elif command == "help":
            print("FRIDAY: Available commands:")
            print("- hello")
            print("- date")
            print("- time")
            print("- help")
            print("- exit")

        elif command == "exit":
            print("FRIDAY: Shutting down. Have a productive day!")
            break

        else:
            print("FRIDAY: I don't understand that command yet.")