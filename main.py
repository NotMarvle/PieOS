#info

OSName = "PieOS"
version = "1.0"
help_cmd = "help"
banner = """
████████████████████████████
█▄─▄▄─█▄─▄█▄─▄▄─█─▄▄─█─▄▄▄▄█
██─▄▄▄██─███─▄█▀█─██─█▄▄▄▄─█
▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀
"""
github = "https://github.com/NotMarvle/PieOS"

#imports
import random

# global variable for the username
Username = ""

#login function
def login():
    global Username
    print(f"Welcome To {OSName} {version}. Type '{help_cmd}' For Help")
    print("Enter Your Username")
    Username = input("> ")
    print("Enter Your Password")
    password = input("> ")

login()
#while loop
while True:
    cmd = input("> ")

    if cmd == "":
        continue

    elif cmd == "help":
        print(f'"{help_cmd}" - Shows This Message')
        print('"exit" - Exits The Program')
        print(f'"version" - Shows The Current Version Of {OSName}')
        print(f'github - Gives You The Github Repo Of {OSName}')
        print(f'"banner" - Shows The Banner Of {OSName}')
        print('"print" - Will Print The Thing You Wanna Say')
        print('"time" - Gives You The Current Time')
        print('"date" - Gives You The Current Date')
        print('"calculator" - Gives You A Calculator')
        print('"coinflip" - Flips A Coin')
        print('"user" - Gives You Your Username')

    elif cmd == "exit":
        break

    elif cmd == "logout":
        login()

    elif cmd == "version":
        print(version)
    
    elif cmd == "github":
        print(f'{github}')

    elif cmd == "banner":
        print(banner)

    elif cmd == "print":
        print("Enter The Value You Wanna Print")
        printCmd = input("> ")
        print(printCmd)

    elif cmd == "time":
        import time
        print(f"The current time is {time.strftime('%I:%M %p')}")

    elif cmd == "calculator":
        import math

        print("Enter Fist Number")
        first_number = int(input("> "))

        print("Enter Operator")
        operator = input("> ")

        print("Enter Second Number")
        second_number = int(input("> "))
        if operator == "+":
            print(first_number + second_number)
        if operator == "-":
            print(first_number - second_number)
        if operator == "*":
            print(first_number * second_number)
        if operator == "/":
            print(first_number / second_number)

    elif cmd == "user":
        print(f'Your Username Is "{Username}"')

    elif cmd == "coinflip":
        import random

        flip_list = ['Heads', 'Tails']

        print(random.choice(flip_list))


    elif cmd == "date":
        from datetime import date

        print(date.today())

    else:
        print(f"Unknown command: {cmd}")