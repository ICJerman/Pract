# Create menu.

def display_menu():
    print("\nMenu:")
    print("1. Add a new item")
    print("2. Update the quantity of an existing item")
    print("3. Display the current inventory")
    print("4. Remove an item")
    print("5. Exit")

def add_item(inventory):
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter item quantity: "))
    if item_name in inventory:
        print(f"{item_name} already exists in the inventory.")
    else:
        inventory[item_name] = item_quantity
        print(f"{item_name} added to the inventory.")

def update_item(inventory):
    item_name = input("Enter item name: ")
    if item_name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name] = new_quantity
        print(f"{item_name} quantity updated to {new_quantity}.")
    else:
        print(f"{item_name} does not exist in the inventory.")

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item_name, item_quantity in inventory.items():
        print(f"{item_name}: {item_quantity}")

def remove_item(inventory):
    item_name = input("Enter item name: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} does not exist in the inventory.")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_item(inventory)
        elif choice == 2:
            update_item(inventory)
        elif choice == 3:
            display_inventory(inventory)
        elif choice == 4:
            remove_item(inventory)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
