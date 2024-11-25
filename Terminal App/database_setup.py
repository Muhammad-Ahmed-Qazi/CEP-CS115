"""
- The user should be able to create a new database by specifying field names and their corresponding
  maximum lengths.
- Two files will be created for each database:
    - System file: Stores the names of fields and their lengths.
    - Data file: Stores the actual records in a structured format.
"""
from file_handler import setup_database, get_db_names

def create_database():
    # Name of database
    name = input("\nEnter a unique name for the new database: ")
    db_names = get_db_names()
    db_names = [db_name.upper() for db_name in db_names]
    if name.upper() in db_names:
        return 0

    # Tables in the database
    tables = dict()
    print(f"\nDefine tables for the database '{name}':")
    while True:
        table = input("Enter a name for the new table, or type '-1' to finish adding tables: ")
        if table == '-1':
            break
        tables[table] = []

    # Fields and lengths for each table in the database
    for table in tables:
        fields = dict()
        print(f"\nDefine fields for the table '{table}':")
        while True:
            field = input("Enter a name for the field, or type '-1' to finish adding fields: ")
            if field == '-1':
                break
            length = int(input(f"Enter the maximum character length for the field '{field}': "))
            fields[field] = length
        tables[table].append(fields)

    # Primary key for each table in the database
    for table in tables:
        fields = list(tables[table][0].keys())
        print(f"\nSelect the primary key for the table '{table}':")
        for i in range(len(fields)):
            print(f"{i + 1}. {fields[i]}")
        while True:
            primary_key = int(input("Enter the number corresponding to the field you'd like to set as the primary key: ")) - 1
            if primary_key in range(len(fields)):
                tables[table].append(fields[primary_key])
                break
            print("Invalid choice. Please select a valid field number from the list.")

    return setup_database(name, format_data(tables))

def format_data(data):
    sys_info = ""

    # List of tables
    sys_info += "Tables\n"
    tables = list(data.keys())
    sys_info += str(tables) + ('\n' * 2)

    # Dictionary of fields & lengths
    sys_info += "Fields & Lengths\n"
    fields = dict()
    for table in data:
        fields[table] = data[table][0]
    sys_info += str(fields) + ('\n' * 2)

    # Dictionary of primary keys
    sys_info += "Primary Keys\n"
    primary_keys = dict()
    for table in data:
        primary_keys[table] = data[table][1]
    sys_info += str(primary_keys) + '\n'

    return sys_info, tables