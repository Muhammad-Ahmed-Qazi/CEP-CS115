"""
- The user should be able to create a new database by specifying field names and their corresponding
  maximum lengths.
- Two files will be created for each database:
    - System file: Stores the names of fields and their lengths.
    - Data file: Stores the actual records in a structured format.
"""
from file_handler import setup_database, get_db_names

# To create a database
def create_database():
    # Name of database
    name = input("\nEnter a unique name for the new database: ")
    db_names = get_db_names()   # Fetch the list of existing database names
    db_names = [db_name.upper() for db_name in db_names]    #  Convert to uppercase for case-insensitive comparison

    #  Check if the database name already exists
    if name.upper() in db_names:
        return 0    # Returns zero if database already exists

    # Tables in the database
    tables = dict()
    print(f"\nDefine tables for the database '{name}':")

    # Loop to allow the user to add tables to the database
    while True:
        table = input("Enter a name for the new table, or type '-1' to finish adding tables: ")
        if table == '-1':   # If the user types '-1', stop adding tables
            break
        tables[table] = []  # Add the table to the dictionary

    # Fields and lengths for each table in the database
    for table in tables:
        fields = dict()
        print(f"\nDefine fields for the table '{table}':")

        # Loop to allow the user to define fields for each table
        while True:
            field = input("Enter a name for the field, or type '-1' to finish adding fields: ")
            if field == '-1':   # If the user types '-1', stop adding fields
                break
            length = int(input(f"Enter the maximum character length for the field '{field}': "))
            fields[field] = length  # Add the field and its length to the dictionary
        tables[table].append(fields)

    # Primary key for each table in the database
    for table in tables:
        fields = list(tables[table][0].keys())  # Get the list of field names for the table
        print(f"\nSelect the primary key for the table '{table}':")

        # Display available fields for the user to choose the primary key
        for i in range(len(fields)):
            print(f"{i + 1}. {fields[i]}")  # Show the field number and name
        while True:
            primary_key = int(input("Enter the number corresponding to the field you'd like to set as the primary key: ")) - 1
            if primary_key in range(len(fields)):   # Ensure the choice is valid
                tables[table].append(fields[primary_key])    # Add the primary key field to the table's data
                break
            print("Invalid choice. Please select a valid field number from the list.")   # Prompt again if the choice is invalid

    # Pass the database name and the formatted table data to set up the database
    return setup_database(name, format_data(tables))

# Format table data
def format_data(data):
    sys_info = ""   # Initialize an empty string to hold the system file data

    # List of tables
    sys_info += "Tables\n"
    tables = list(data.keys())  # Get list of table names
    sys_info += str(tables) + ('\n' * 2)    # Append table names

    # Dictionary of fields & lengths
    sys_info += "Fields & Lengths\n"
    fields = dict()
    for table in data:
        fields[table] = data[table][0]  # Get fields for each table
    sys_info += str(fields) + ('\n' * 2)    # Append fields and lengths

    # Dictionary of primary keys
    sys_info += "Primary Keys\n"
    primary_keys = dict()
    for table in data:
        primary_keys[table] = data[table][1]    # Get the primary key for each table
    sys_info += str(primary_keys) + '\n'    # Append primary keys

    # Return the formatted system info and the list of table names
    return sys_info, tables