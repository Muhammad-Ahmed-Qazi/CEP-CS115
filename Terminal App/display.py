from database_setup import create_database
from data_manipulation import add_record, search_record, delete_record, edit_record
from file_handler import get_db_names, get_tables, get_fields, get_records

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
                print("\n\033[92mDatabase created successfully!\033[0m")
                print(
                    "\nTo add records, follow these steps:\n"
                    "\t1. Return to the main menu and select 'Open Existing Database.'\n"
                    "\t2. Choose the database you just created.\n"
                    "\t3. Select the table where you want to add records.\n"
                    "This will allow you to start entering records into your table."
                )
            else:
                print("\n\033[91mDatabase already exists with this name!\033[0m")
        elif choice == '2':
            if len(get_db_names()) == 0:
                print("\n\033[91mNo databases exist! Please create one first!\033[0m")
            else:
                open_database()
        elif choice == '3':
            print("\n\033[94mExiting the program. Goodbye!\033[0m")
            break
        else:
            print("\n\033[91mInvalid option. Please select a valid option (1-3).\033[0m")

def open_database():
    db_names = get_db_names()

    # Selecting database to open
    db_name = show_list("database", db_names)

    while True:
        tables = get_tables(db_name)
        print(f"\n--- Database: {db_name} ---\n")
        print("1. Add a Record")
        print("2. Edit a Record")
        print("3. Delete a Record")
        print("4. Search for and Display a Record")
        print("5. Display All Records in a Table")
        print("6. Return to Main Menu")

        choice = input("Select an option (1-6): ")

        # Add a record
        if choice == '1':
            if not add_record(db_name, show_list("table", tables)):
                print("\nRecord with this primary key already exists!")
            else:
                print("\nRecord successfully added!")

        elif choice == '2':
            edit_record(db_name, show_list("table", tables))

        # Delete a record
        elif choice == '3':
            table = show_list("table", tables)
            if delete_record(db_name, table, search_record(db_name, table)):
                print("\nRecord successfully deleted!")
            else:
                print("\nRecord with this primary key does not exist!")

        # Search for and Display a record
        elif choice == '4':
            display_selected(db_name, show_list("table", tables))

        # Display all records in a table
        elif choice == '5':
            display_all(db_name, show_list("table", tables))

        # Returning to main menu
        elif choice == '6':
            print("\nReturning to main menu.")
            break

        else:
            print("\nInvalid option. Please select a valid option (1-6).")

def show_list(entities, info):
    print("\nChoose a table from the list below to perform the operation:")
    for i in range(len(info)):
        print(f"{i + 1}. {info[i]}")

    while True:
        if len(info) == 1:
            entity = input(f"Select {entities} (1): ")
        else:
            entity = input(f"Select {entities} (1-{len(info)}): ")
        try:
            entity = info[int(entity) - 1]
            return entity
        except IndexError:
            print(f"Invalid option. Please select a valid option (1-{len(info)})." if len(info) != 1 else f"Invalid option. Please select a valid option (1).")

def display_selected(db_name, table):
    record = search_record(db_name, table).split(",")
    header = "|"
    data = "|"

    if record != ['']:
        fields = get_fields(db_name)[table]
        for field, entry in zip(fields, record):
            if len(entry) > len(field):
                col_length = len(entry) + 2
            else:
                col_length = len(field) + 2
            header += f" \033[1m\033[3m{field.strip():{col_length}}\033[0m |"
            data += f" {entry.strip():{col_length}} |"
        print("\n" + header)
        print(data)
    else:
        print("\nRecord with this primary key entry does not exist.")

# Muhammad Ahmed Qazi
# def display_all(db_name, table):
#     fields = get_fields(db_name)[table]
#     records = get_records(db_name, table)

#     header = "|"
#     data = "|"

#     for field in fields:
#         header += f" \033[1m\033[3m{field:{fields[field]}}\033[0m |"

#     print("\n" + header)

#     field_names = list(fields.keys())
#     field_lengths = list(fields.values())
#     for record in records:
#         record = record.split(",")
#         for i in range(len(record)):
#             if len(field_names[i]) > field_lengths[i]:
#                 col_length = len(field_names[i])
#             else:
#                 col_length = field_lengths[i]
#             data += f" {record[i].strip():{col_length}} |"
#         print(data)
#         data = "|"

# Usman Rasheed Siddiqui
def display_all(db_name, table):
    '''This function is being used to fetch fields, their lengths and the respective records from the table
    in order to view them when the user gives the appropriate prompt'''


    fields = get_fields(db_name)[table]        # Fetching fields
    records = get_records(db_name, table)      # Fetching records


    # Fetching Field Lengths And Names

    field_lengths = list(fields.values())               # Fetching field lengths
    field_names = list(fields.keys())                   # Fetching field names

    # Display the field names as headings:
    # For headings to be Bold And Italic
    bold_italic = '\033[1m\033[3m'
    reset = '\033[0m'

    header = ''
    for field in range(len(field_lengths)):
        header += f"{bold_italic}{field_names[field]:{field_lengths[field]}}{reset} |"    # Displaying each heading separated by pipelines
    print(header.strip())                                             #   Removing whitespaces and newline commands

    #Iterating on record:
    # Display Records (values of each field)
    for record in records:  # Loop through all records
        record = record.strip()  # Remove any leading/trailing whitespace/newline characters
        if not record:  # Skip empty lines if any
            continue
        record_values = record.split(', ')  # Split the record into its individual values


    #   Fetching Each record one by one:
        row = ''
        for values, field in zip(record_values, range(len(field_names))):

        # To determine appropriate spaces and alignment of pipes from top to bottom
            if len(field_names[field]) > field_lengths[field]:
                col_length = len(field_names[field])
            else:
                col_length = field_lengths[field]

            row += f'{str(values):{col_length}} |'      # To display each record separated by pipes

        print(row.strip())