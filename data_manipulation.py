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
from file_handler import get_fields, write_record, get_primary_keys, record_exists, update_records

# Adding a new record
def add_record(db_name, table):
    record = list()

    # Get fields and respective lengths
    fields = get_fields(db_name)[table]
    pk = get_primary_keys(db_name)[table]

    # Getting input for each field of the table
    print(f"\nEnter data for respective fields in '{table}':")
    while True:
        data = input(f"{pk}: ")
        if 0 < len(data) <= fields[pk]:
            pk_entry = data
            break
        else:
            print(f"Input must have at least 1 and maximum {fields[pk]} characters!")
    if record_exists(db_name, table, data):
        return 0

    for field in fields:
        if field != pk:
            while True:
                data = input(f"{field}: ")
                if 0 < len(data) <= fields[field]:
                    record.append(data)
                    break
                else:
                    print(f"Input must have at least 1 and maximum {fields[field]} characters!")
        else:
            record.append(pk_entry)

    write_record(db_name, table, format_data(record))
    return 1

# Formatting record entries into a string to be written to the data files
def format_data(record):
    data_info = ""

    for field in record:
        data_info += field + ', '

    return data_info[:-2] + '\n'

# Edit a record
def edit_record(db_name, table):
    orig_record = search_record(db_name, table)
    record = orig_record.split(",")

    if record != ['']:
        record = []

        print(f"\nEnter data for respective fields in '{table}':")
        # Get fields and respective lengths
        fields = get_fields(db_name)[table]

        for field in fields:
            while True:
                data = input(f"{field}: ")
                if 0 < len(data) <= fields[field]:
                    record.append(data)
                    break
                else:
                    print(f"Input must have at least 1 and maximum {fields[field]} characters!")

        update_records(db_name, table, orig_record, format_data(record))
    else:
        print("\nRecord with this primary key entry does not exist.")

# Delete a record using the primary key input by the user
def delete_record(db_name, table, record):
    if record:
        update_records(db_name, table, record)
        return 1
    else:
        return 0

# Searching whether a record with the primary key input exists in the database or not
def search_record(db_name, table):
    pk = get_primary_keys(db_name)[table]

    pk_data = input(f"\nEnter the value for '{pk}' to get the record: ")
    return record_exists(db_name, table, pk_data)