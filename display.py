from database_setup import create_database
from data_manipulation import add_record
from file_handler import db_list, tables_list

def main_menu():
    while True:
        print("\n=== Simple Database Management System ===")
        print("1. Create a New Database")
        print("2. Open Existing Database")
        print("3. Exit")

        # Get user choice
        choice = input("Select an option (1-3): ")

        if choice == '1':
            if create_database():
                print("Database created successfully!")
                print(
                    "To add records, follow these steps:\n"
                    "\t1. Return to the main menu and select 'Open Existing Database.'\n"
                    "\t2. Choose the database you just created.\n"
                    "\t3. Select the table where you want to add records.\n\n"
                    "This will allow you to start entering records into your table."
                )
            else:
                print("Database already exists!")
        elif choice == '2':
            open_database()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option (1-3).")

def open_database():
    db_names = db_list()

    # Selecting database to open
    for i in range(len(db_names)):
        print(f"{i + 1}. {db_names[i]}")
    while True:
        if len(db_names) == 1:
            db = input(f"Select database (1): ")
        else:
            db = input(f"Select database (1-{len(db_names)}): ")
        try:
            db_name = db_names[int(db) - 1]
            break
        except:
            print(f"Invalid option. Please select a valid option (1-{len(db_names)}).")

    while True:
        tables = tables_list(db_name)
        print(f"\n--- Database: {db_name} ---\n")
        print("1. Add a Record")
        print("2. Edit a Record")
        print("3. Delete a Record")
        print("4. Search for and Display a Record")
        print("5. Display All Records in a Table")
        print("6. Add Another Table to Database")
        print("7. Return to Main Menu")

        choice = input("Select an option (1-7): ")

        # Adding a record
        if choice == '1':
            for i in range(len(tables)): # Listing loops can be made into a function
                print(f"{i + 1}. {tables[i]}")

            if len(tables) == 1:
                table = input(f"Select table (1): ")
            else:
                table = input(f"Select table (1-{len(tables)}): ")
            try:
                table = tables[int(table) - 1]
                add_record(db_name, table)
            except:
                print(f"Invalid option selected. Returning to menu.")
                continue

        # elif choice == '2':
        #     table = input("Enter the name of the table to edit a record: ")
        #     if table_exists(db_name, table):
        #         edit_record(db_name, table)
        #     else:
        #         print(f"Table '{table}' does not exist in '{db_name}'.")
        #
        # elif choice == '3':
        #     table = input("Enter the name of the table to delete a record: ")
        #     if table_exists(db_name, table):
        #         delete_record(db_name, table)
        #     else:
        #         print(f"Table '{table}' does not exist in '{db_name}'.")
        #
        # elif choice == '4':
        #     table = input("Enter the name of the table to search and display a record: ")
        #     if table_exists(db_name, table):
        #         search_and_display_record(db_name, table)
        #     else:
        #         print(f"Table '{table}' does not exist in '{db_name}'.")
        #
        # elif choice == '5':
        #     table = input("Enter the name of the table to display all records: ")
        #     if table_exists(db_name, table):
        #         display_all_records(db_name, table)
        #     else:
        #         print(f"Table '{table}' does not exist in '{db_name}'.")
        #
        # elif choice == '6':
        #     add_table(db_name)


        elif choice == '7':
            print("Returning to main menu.")
            break

        else:
            print("Invalid option. Please select a valid option (1-7).")