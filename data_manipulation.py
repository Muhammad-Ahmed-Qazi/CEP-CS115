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
def editing_record(db_name, table):

    fields = get_fields(db_name)[table]  # Getting fields

    field_names = list(fields.keys())  # Getting field names

    fetch_record = search_record(db_name, table)
    record = fetch_record.strip().split(",")

    # Ensure that the record has the correct number of fields
    if len(record) != len(field_names):
        print(
            f"Error: The number of fields in the record does not match the expected number of fields ({len(field_names)}).")
        return

    if record:  # Verifying that the record is not an empty list
        for i, field in zip(range(len(field_names)), field_names):  # Proceed to editing the record

            while True:
                edit_record = input(f"Edit new record for {field}: ")  # Entering new value for the field
                print()
                print(f"Editing field '{field}' with value: {edit_record}")
                print()
                if 0 < len(edit_record) <= fields[field]:  # Checking length of the input
                    record[i] = edit_record  # Update the record at the correct index
                    break

                else:
                    print(f"The length of the input must be from 1 character to {fields[field]} characters")

    else:
        print("Following record does not exist")
        return

    # Format the edited record for writing
    formatted_edit = format_data(record)
    # print(f"Formatted updated record: {formatted_edit}")

    update_records(db_name, table, fetch_record, formatted_edit)

    print("Record successfully updated")

    #  Call the function to start the process
#editing_record(db_name, table)

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