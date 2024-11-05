from database_setup import create_database

def main_menu():
    while True:
        print("\n=== Simple Database Management System ===")
        print("1. Create a New Database")
        print("2. Open Existing Database")
        print("3. Exit")

        # Get user choice
        choice = input("Select an option (1-3): ")

        if choice == '1':
            create_database()
            pass
        elif choice == '2':
            # open_database()
            pass
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option (1-3).")

if __name__ == '__main__':
    pass