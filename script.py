import sys

def main_menu():
        print("\n--- Main Menu ---")
        print("1. Start Game")
        print("2. Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            return "Gameplay"
        elif choice == "2":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid Choice. Please try again.")
            return "Menu"

if __name__ == "__main__":
    state = main_menu()
    if state == "Gameplay":
        print("Game will now start.")
    else:
        print(f"The menu ended with state: {state}")

playername=input("Hello, please enter your name: ")
print("Hello", playername, "welcome to the adventure.")

print("\n---Level 1: The Forest---")
print("1. Continue")
print("2. Turn back")
while True:
    choice2=input("Select your choice: ")
    if choice2 == "1":
        print("Excellent!")
        break
    elif choice2 == "2":
        print("Too late.")
    else:
        print("Invalid Choice. Please try again.")

print("\n---Goblin Encounter!---")
print("A goblin approaches you, what do you do?")
print("1. FIGHT")
print("2. RUN")
while True:
    choice3=input("Select your choice: ")
    if choice3 == "1":
        print("You defeated the goblin!")
        break
    elif choice3 == "2":
        print("The goblin struck while your back was turned!")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    else:
        print("Invalid Choice. Please try again.")

print("\n---Snake Encounter!---")
print("Two snakes block your path!")
print("1. Check first snake")
print("2. Check second snake")
while True:
    choice4=input("Select your choice: ")
    if choice4 == "1":
        print("HEALTH: 10")
        break
    elif choice4 == "2":
        print("HEALTH: 2")
        break
    else:
        print("Invalid Choice. Please try again.")

print("\nWhich snake will you attack?")
print("1. First snake")
print("2. Second snake")
while True:
    choice5=input("Select your choice: ")
    if choice5 == "1":
        print("It's unwise to prioritize the strongest!")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice5 == "2":
        print("Wise choice! The weaker snake fell!")
        break
    else:
        print("Invalid Choice. Please try again.")

print("\nONE SNAKE REMAINS!")
print("1. Attack")
print("2. Retreat and move forward")
while True:
    choice6=input("Select your choice: ")
    if choice6 == "1":
        print("The snake was too tough!")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice6 == "2":
        print("Wise choice! The forest is wide and open.")
        break


