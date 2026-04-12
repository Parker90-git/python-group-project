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

print("\n---LEVEL COMPLETE!---")
print("---Level 2: The Desert---")
print("\nYou see three items in front of you:")
while True:
    print("1. Soda")
    print("2. Water")
    print("3. Twig")
    choice7=input("Which item do you take?: ")
    if choice7 == "1":
        print("Drinking the soda made you more thirsty.")
        print("You have fallen due to dehydration.")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice7 == "2":
        print("Good choice! You remain hydrated by drinking the water!")
        break
    elif choice7 == "3":
        print("Out of all the choices you picked the twig.")
        print("What is wrong with you?")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    else:
        print("Invalid Choice. Please try again.")

print("\n---THIEF ENCOUNTER!---")
while True:
    print("A thief wants to steal your water!")
    print("What do you do?")
    print("1. Give water")
    print("2. Attack thief")
    print("3. Look in inventory")
    choice8=input("Select your choice: ")
    if choice8 == "1":
        print("The thief took your water.")
        print("Honestly why would you pick that.")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice8 == "2":
        print("The thief had a stronger weapon!")
        print("You have fallen")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice8 == "3":
        print("Your inventory includes:")
        print("1. Money")
        print("2. Leaf")
        print("3. Dragon's Sword")
        choice9=input("Select your choice: ")
        if choice9 == "1":
            print("That's actually the right choice!")
            print("Currency doesn't matter in this game.")
            print("The thief thanked you and ran away!")
            break
        elif choice9 == "2":
            print("The thief felt disrespected and struck you.")
            print("\n---GAME OVER---")
            print("Returning you back to last save...")
        elif choice9 == "3":
            print("Uhhh how did that get here so soon.")
            print("This isn't to be used until the final battle.")
            print("\n---GAME OVER---")
            print("Returning you back to last save...")
        else:
            print("Invalid Choice. Please try again.")
    else:
        print("Invalid Choice. Please try again.")

while True:
    list1=["Apple","Banana","Pear"]
    print("\nYou feel uncomfortable with how disorganized your inventory is.")
    print("Change it?")
    print("1. Yes")
    print("2. No")
    choice10=input("Select your choice: ")
    if choice10 == "2":
        print("The stress got to you.")
        print("You kept thinking about how disorganized your inventory is.")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice10 == "1":
        break
    else:
        print("Invalid Choice. Please try again.")

while True:
    print("\nCurrent inventory:")
    print(list1)
    print("The apple feels heavier than the rest.")
    print("What do you do?:")
    print("1. Move the apple to the back")
    print("2. Move the banana to the front")
    print("3. Eat the pear")
    choice11=input("Select your choice: ")
    if choice11 == "1":
        list1.append("Apple")
        list1.pop(0)
        print(list1)
        print("Your posture feels better!")
        break
    elif choice11 == "2":
        print("The apple is now in the middle.")
        print("Your posture feels worse.")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice11 == "3":
        print("Why?")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    else:
        print("Invalid Choice. Please try again.")
