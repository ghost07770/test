command=""
started = False
while True:
    choice = input("> ").upper()
    if choice=="HELP":
        print("""
Start to start the car
Stop to stop the car
Quit to quit the game""")
    elif choice=="START":
        if started:
            print("The car is already started")
        else:
            started=True
            print("The car has started and is ready to go")
    elif choice=="STOP":
        if not started:
            print("The car has already stopped")
        else:
            print("The car has stopped")
            started=False
    elif choice=="QUIT":
          break
    else :
        print("I don't understand")