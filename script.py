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


