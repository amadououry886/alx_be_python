def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):

        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} is added to the list ")
    

def remove_item(shopping_list):

        item = input("Enter the item to remove: ")
        if item in shopping_list:
             
            shopping_list.remove(item)

            print(f"{item} has been removed ")
        else: 
            print(f"{item} doesn't exit in the list given")
        


def view_list(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is currently empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            
            add_item(shopping_list)
        
        elif choice == '2':
            
            remove_item(shopping_list)
        
        elif choice == '3':
            
            view_list(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()