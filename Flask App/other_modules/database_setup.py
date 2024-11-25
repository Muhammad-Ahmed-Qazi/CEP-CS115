"""
- The user should be able to create a new database by specifying field names and their corresponding
  maximum lengths.
- Two files will be created for each database:
    - System file: Stores the names of fields and their lengths.
    - Data file: Stores the actual records in a structured format.
"""
from other_modules.file_handler import setup_database, get_db_names

# Function to create a new database with specified tables, fields, and constraints
def create_database(data):
    # Extract the database name from the user-provided data
    name = data['db_name']

    # Retrieve a list of existing database names and normalize them to uppercase for comparison
    db_names = get_db_names()
    db_names = [db_name.upper() for db_name in db_names]

    # Check if the database already exists; if yes, terminate with an error message
    if name.upper() in db_names:
        print("Database already exists!")
        return 0

    # Extract all keys from the input data except the database name
    keys = list(data.keys())
    keys.pop(0)

    # Initialize variables for parsing the table and field structure
    tables = 1
    fields = list()
    table_dict = {}

    # Loop through the keys to parse table and field information
    for key in keys:
        parts = key.split('[')  # Split the key into parts for extracting table and field details
        table_index = int(parts[1][0])  # Extract the table index from the key
        if table_index not in table_dict:
            # Create a new entry for the table if it doesn't exist
            table_dict[table_index] = {'name': '', 'fields': []}

        # Parse the table name or field information based on the key structure
        if 'name' in parts[2]:
            table_dict[table_index]['name'] = data[key]  # Set the table name
        elif 'fields' in parts[2]:
            field_index = int(parts[3][0])  # Extract the field index
            if field_index >= len(table_dict[table_index]['fields']):
                # Ensure the field list is large enough to accommodate the field index
                table_dict[table_index]['fields'].append(['', 0])

            # Set the field name or length based on the key structure
            if 'name' in parts[4]:
                table_dict[table_index]['fields'][field_index][0] = data[key]  # Set field name
            elif 'length' in parts[4]:
                table_dict[table_index]['fields'][field_index][1] = int(data[key])  # Set field length

    # Convert the parsed data into the required format for database creation
    master_dict = {}
    for table in table_dict.values():
        table_name = table['name']
        fields = {field[0]: field[1] for field in table['fields']}  # Map field names to lengths
        primary_key = list(fields.keys())[0] if fields else None  # Assign the first field as the primary key
        master_dict[table_name] = {'fields': fields, 'primary_key': primary_key}

    data = master_dict

    # Call the function to set up the database with the formatted data
    return setup_database(name, format_data(data))

# Helper function to format the database schema into a structured string for the system file
def format_data(data):
    sys_info = ""

    # Add the list of tables to the system file
    sys_info += "Tables\n"
    tables = list(data.keys())
    sys_info += str(tables) + ('\n' * 2)

    # Add the fields and their lengths for each table to the system file
    sys_info += "Fields & Lengths\n"
    fields = dict()
    for table in data:
        print(table, data[table])  # Debugging: Print the table name and its schema
        fields[table] = data[table]['fields']
    sys_info += str(fields) + ('\n' * 2)

    # Add the primary keys for each table to the system file
    sys_info += "Primary Keys\n"
    primary_keys = dict()
    for table in data:
        primary_keys[table] = data[table]['primary_key']
    sys_info += str(primary_keys) + '\n'

    # Return the system file content and table names
    return sys_info, tables
