import os
import linecache

# Function to generate a file path based on database name and type (system or table file)
def create_path(name, table_opt="s"):
    if table_opt == 's':    # System file path
        return f"{os.getcwd()}/System Files/{name}.txt"
    else:       # Data file path for a specific table
        return f"{os.getcwd()}/Data Files/{name}/{table_opt}.txt"

# Function to set up a new database
def setup_database(db_name, info):

    try:
        # Create a directory for the database's data files
        os.mkdir(f"Data Files/{db_name}")
    except FileExistsError:
        return 0    # Return 0 if the database directory already exists

    # Append the database name to a file that tracks all database names
    with open(create_path('db_names'), 'a+') as file:
        file.write(db_name + '\n')

    # Create a system file for the database and write formatted metadata
    with open(create_path(db_name), "w") as file:
        file.write(info[0])

    # Create empty files for each table in the database
    for table in info[1]:
        with open(create_path(db_name, table), "w"):
            pass

    return 1    # Return 1 to indicate successful database creation

# Function to get a list of all database names
def get_db_names():
    with open(create_path("db_names"), "r") as file:
        db_names = file.readlines()
        return [db_name.strip() for db_name in db_names]    # Remove trailing whitespace from names

# Function to get the list of tables in a database
def get_tables(db_name):
    # Retrieve the line containing table names from the system file
    tables = linecache.getline(create_path(db_name), 2)
    return eval(tables)     # Convert the string representation of the list into an actual list

# Function to get the fields and their lengths for each table
def get_fields(db_name):
    # Retrieve the line containing fields and their lengths from the system file
    fields = linecache.getline(create_path(db_name), 5)
    return eval(fields)     # Convert the string representation of the dictionary into an actual dictionary

# Function to get the primary keys for each table
def get_primary_keys(db_name):
    # Retrieve the line containing primary keys from the system file
    pk = linecache.getline(create_path(db_name), 8)
    return eval(pk)  # Convert the string representation of the dictionary into an actual dictionary

# Function to append a record to a specific table
def write_record(db_name, table, info):
    with open(create_path(db_name, table), "a") as file:
        file.write(info)  # Write the record to the table file

# Function to check if a record with the given primary key exists in the table
def record_exists(db_name, table, pk):
    with open(create_path(db_name, table), "r") as file:
        for line in file:  # Read each line in the table
            if pk in line:  # Check if the primary key exists in the line
                return line  # Return the record if found
    return ""  # Return an empty string if the record is not found

# Function to retrieve all records from a specific table
def get_records(db_name, table):
    with open(create_path(db_name, table), "r") as file:
        return file.readlines()  # Return all lines (records) in the table file

# Function to update records in a table
def update_records(db_name, table, record, edit=""):
    records = get_records(db_name, table)  # Retrieve all records from the table
    with open(create_path(db_name, table), "w") as file:
        for line in records:
            if not edit:  # Deleting a record
                if record != line:  # Write back only records that are not to be deleted
                    file.write(line)
            else:  # Editing a record
                if record == line:  # Replace the old record with the new one
                    file.write(edit)
                else:  # Write back other records unchanged
                    file.write(line)
