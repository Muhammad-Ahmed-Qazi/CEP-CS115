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
from file_handler import get_fields, write_record

def add_record(db_name, table):
    record = list()

    # Get fields and respective lengths
    fields = get_fields('Sample')[table]

    # Getting input for each field of the table
    print(f"\nEnter data for respective fields in '{table}':")
    for field in fields:
        while True:
            data = input(f"{field}: ")
            if 0 < len(data) <= fields[field]:
                record.append(data)
                break
            else:
                print(f"Input must have at least 1 and maximum {fields[field]} characters!")

    write_record(db_name, table, format_data(record))

def format_data(record):
    data_info = ""

    for field in record:
        data_info += field + ', '

    return data_info[:-2] + '\n'