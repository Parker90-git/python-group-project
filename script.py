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


print("\nDESERT COMPLETE!")
print("\n---FINAL LEVEL: Dragon's Lair---")
print(". . . To defeat the dragon, you must find the Dragon's Sword!")
chestpuzzle={"Chest 1":"Wooden Sword","Chest 2":"Brass Knuckles","Chest 3":"Dragon's Sword"}
while True:
    print("\nIn front of you are three chests:")
    print("1. Open chest 1")
    print("2. Open chest 2")
    print("3. Open chest 3")
    choice12=input("Select your choice: ")
    if choice12 == "1":
        print(chestpuzzle["Chest 1"])
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice12 == "2":
        print(chestpuzzle["Chest 2"])
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice12 == "3":
        print(chestpuzzle["Chest 3"])
        break
    else:
        print("Invalid Choice. Please try again.")

print("\n---THIS IS IT! FINAL ENCOUNTER!---")
print("\n---SLAY THE DRAGON---")
while True:
    print("\nWhich part of the dragon do you want to attack?")
    print("1. Head")
    print("2. Tail")
    print("3. Arms")
    print("4. Legs")
    print("5. Wings")
    choice13=input("Select your choice: ")
    if choice13 == "1":
        print("The head is too high up!")
        print("The dragon spews out fire!")
        print("1. Dodge")
        print("2. Reflect")
        choice14=input("Select your choice: ")
        if choice14 == "1":
            print("That was close!")
        elif choice14 == "2":
            print("You reflect the fireball back!")
            print("The dragon is DIZZY!")
            print("1. Attack")
            print("2. Wait")
            choice15=input("Select your choice: ")
            if choice15 == "1":
                print("You SLICED the dragon's head!")
                print("\n---EASY ENDING---")
                break
            elif choice15 == "2":
                print("Why would you do that.")
                print("\n---GAME OVER---")
                print("Returning you back to last save...")
            else:
                print("Invalid Choice. Please try again.")
        else:
            print("Invalid Choice. Please try again.")
    elif choice13 == "2":
        print("That's the least of your concerns!")
        print("The dragon took the opportunity to ATTACK!")
        print("\n---GAME OVER---")
        print("Returning you back to last save...")
    elif choice13 == "3":
        print("You SLICED the dragon's arms!")
        print("It panics and attempts to attack with its LEGS!")
        print("1. Block")
        print("2. Counterattack")
        choice16=input("Select your choice: ")
        if choice16 == "1":
            print("The weight of the dragon crushes you!")
            print("\n---GAME OVER---")
            print("Returning you back to last save...")
        elif choice16 == "2":
            print("You SLICE the dragon's legs!")
            print("The dragon FLEW AWAY in fear!")
            print("\n---BRAVE ENDING---")
            break
        else:
            print("Invalid Choice. Please try again.")
    elif choice13 == "4":
        print("You SLICE the legs off!")
        print("The dragon panics and attempts to attack with its ARMS!")
        print("1. Block")
        print("2. Counterattack")
        choice17=input("Select your choice: ")
        if choice17 == "1":
            print("The weight of the dragon crushes you!")
            print("\n---GAME OVER---")
            print("Returning you back to last save...")
        elif choice17 == "2":
            print("You SLICE the arms off!")
            print("The dragon FLEW AWAY in fear!")
            print("\n---BRAVE ENDING---")
            break
        else:
            print("Invalid Choice. Please try again.")
    elif choice13 == "5":
        print("You THROW the dragon sword like a boomerang!")
        print("The wings cut RIGHT off!")
        print("You dash under the dragon to prepare a finishing blow!")
        print("\n. . .The dragon crushes you.")
        print("What a way to go out.")
        print("\n---BAD ENDING---")
        break
    else:
        print("Invalid Choice. Please try again.")

print("\n---THANK YOU FOR PLAYING!---")
