command = input(">")
while command.lower() != "quit":

    if command.lower() == "help":
        print("""Start - To start the car
            Stop - To stop the car
              Quit- To Exit""")

    elif command.lower() == "start":
        print('car started')

    elif command.lower() == "stop":
        print("car stopped")

    else:
        print("Please enter a vaild input")

    command = input("> ")


