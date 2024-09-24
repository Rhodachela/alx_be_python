def display_menu():
             print("\033[4mShopping List Manager\033[0m")
             print("1. Add Item")
             print("2. Remove Item")
             print("3. View List")
             print("4. Exit") 

display_menu()
def main():
    shopping_list = [] 
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4: ")
            continue

        if choice == 1:
           item = input("Enter the item to add: ")
           shopping_list.append(item)
        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} is not on the list.")
        elif choice == 3:
            print(shopping_list)
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        elif choice == 4:
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()  