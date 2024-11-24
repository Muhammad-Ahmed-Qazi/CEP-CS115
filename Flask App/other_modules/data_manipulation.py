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

# Adding a new record
def add_record(db_name, table, data):
    fields = get_fields(db_name)[table]
    pk = get_primary_keys(db_name)[table]

    if record_exists(db_name, table, data[pk]):
        return '<div class="alert alert-warning">Record with this primary key already exists in the database!</div>'

    record = [value for value in data.values()]

    write_record(db_name, table, format_data(record))
    return '<div class="alert alert-success">Record successfully added!</div>'

# Formatting record entries into a string to be written to the data files
def format_data(record):
    data_info = ""

    for field in record:
        data_info += field + ', '

    return data_info[:-2] + '\n'

# Edit a record
def edit_record(db_name, table, data):
    pk = get_primary_keys(db_name)[table]
    print(data)
    orig_record = record_exists(db_name, table, data[pk])
    
    record = [value for value in data.values()]
    
    update_records(db_name, table, orig_record, format_data(record))
    
    return '<div class="alert alert-success">Record successfully edited!</div>'

# Delete a record using the primary key input by the user
def delete_record(db_name, table, record):
    if record:
        update_records(db_name, table, record)
        return '<div class="alert alert-success">Record successfully deleted!</div>'
    else:
        return 0

# Searching whether a record with the primary key input exists in the database or not
def search_record(db_name, table, data):
    pk = get_primary_keys(db_name)[table]

    return record_exists(db_name, table, data[pk])