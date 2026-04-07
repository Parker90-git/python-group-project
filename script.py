def display_list(grocery_list):
    if not grocery_list:
        print("Your grocery list is currently empty.")
    else:
        print("Current Grocery List")
        for index, item in enumerate(grocery_list, start=1):
            print(f"{index}. {item}")

def main():
    grocery_list = []

    print("Grocery List Manager")

    while True:
        print("Options:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice in ['1', 'add']:
            item = input("Enter the name of the item to add: ")
            if item:
                grocery_list.append(item)
                print(f"'{item}' has been added.")
            else:
                print("Item name cannot be empty.")

        elif choice in ['2', 'remove']:
            if not grocery_list:
                print("The list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the name of the item to remove: ")
            if item_to_remove in grocery_list:
                grocery_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed.")
            else:
                print(f"Error: '{item_to_remove}' was not found in your list.")

        elif choice in ['3', 'view']:
            display_list(grocery_list)

        elif choice in ['4']:
            print("Exiting the program.")
            break

        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()


