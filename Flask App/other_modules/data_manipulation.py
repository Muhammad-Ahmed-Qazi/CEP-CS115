"""
- The system should allow the user to open any database from the already existing databases.
- The system must provide the following operations on the opened database:
    - Add a record: Allow users to input data for each field, ensuring it does not exceed the specified field
      length.
    - Edit a record: Provide functionality to modify an existing record.
    - Delete a record: Enable users to remove records from the database.
    - Display all records: Enable users to view all records from the database.
    - Display a selected record: Enable users to view a selected record from the database.
"""
from other_modules.file_handler import get_fields, write_record, get_primary_keys, record_exists, update_records

# Function to add a new record to a specific table in the database
def add_record(db_name, table, data):
    # Retrieve the fields and primary key for the specified table
    fields = get_fields(db_name)[table]
    pk = get_primary_keys(db_name)[table]

    # Check if a record with the same primary key already exists
    if record_exists(db_name, table, data[pk]):
        return '<div class="alert alert-warning">Record with this primary key already exists in the database!</div>'

    # Prepare the record data for writing
    record = [value for value in data.values()]

    # Write the formatted record to the database
    write_record(db_name, table, format_data(record))
    return '<div class="alert alert-success">Record successfully added!</div>'

# Helper function to format record data into a comma-separated string
def format_data(record):
    data_info = ""

    # Concatenate each field value with a comma separator
    for field in record:
        data_info += field + ', '

    # Remove the trailing comma and add a newline character
    return data_info[:-2] + '\n'

# Function to edit an existing record in the specified table
def edit_record(db_name, table, data):
    # Retrieve the primary key of the table
    pk = get_primary_keys(db_name)[table]

    # Search for the original record using the primary key
    orig_record = record_exists(db_name, table, data[pk])

    # Prepare the updated record data
    record = [value for value in data.values()]

    # Update the record in the database by replacing the original with the new record
    update_records(db_name, table, orig_record, format_data(record))

    return '<div class="alert alert-success">Record successfully edited!</div>'

# Function to delete a specific record from the database
def delete_record(db_name, table, record):
    if record:  # Check if the record exists
        # Use the update_records function to remove the specified record
        update_records(db_name, table, record)
        return '<div class="alert alert-success">Record successfully deleted!</div>'
    else:
        return 0  # Return 0 if no record is provided

# Function to search for a record in the database by primary key
def search_record(db_name, table, data):
    # Retrieve the primary key of the table
    pk = get_primary_keys(db_name)[table]

    # Check if a record with the provided primary key exists
    return record_exists(db_name, table, data[pk])
