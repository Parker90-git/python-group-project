def main_menu():
    print("\n--- Main Menu ---")
    print("1. Start Game")
    print("2. Exit")

    choice = input("Select your choice: ")
    if choice == "1":
        return "Gameplay"
    elif choice == "2":
        return "Exit"
        sys.exit()
    else:
        print("Invalid Choice")
        return main_menu()

playername=input("Hello, please enter your name: ")
print("Hello", playername, "welcome to the adventure.")


