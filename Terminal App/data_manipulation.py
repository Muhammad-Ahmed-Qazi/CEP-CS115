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
        data = input(f"{pk}: ")      # Input for primary key
        if 0 < len(data) <= fields[pk]: # Ensure the data length is within the defined limit
            pk_entry = data     # Assign the input as the primary key entry
            break
        else:
            print(f"Input must have at least 1 and maximum {fields[pk]} characters!")   # Prompt for valid input instruction
    if record_exists(db_name, table, data):     # Check if a record with the primary key already exists
        return 0    # if the record already exists

    # Getting input for each field (except the primary key) of the table
    for field in fields:
        if field != pk:     #Skip the primary key
            while True:
                data = input(f"{field}: ")      # Input for other fields
                if 0 < len(data) <= fields[field]:  # Ensure the data length is within the defined limit
                    record.append(data)
                    break
                else:
                    print(f"Input must have at least 1 and maximum {fields[field]} characters!")
        else:
            record.append(pk_entry)

    write_record(db_name, table, format_data(record))   # Write the formatted record to the table file
    return 1

# Formatting record entries into a string to be written to the data files
def format_data(record):
    data_info = ""      # Initialize a  empty string to hold formatted data

    # Concatenate each field
    for field in record:
        data_info += field + ', '

    return data_info[:-2] + '\n'

# Edit a record - Muhammad Ahmed Qazi
# def edit_record(db_name, table):
#     orig_record = search_record(db_name, table)
#     record = orig_record.split(",")

#     if record != ['']:
#         record = []

#         print(f"\nEnter data for respective fields in '{table}':")
#         # Get fields and respective lengths
#         fields = get_fields(db_name)[table]

#         for field in fields:
#             while True:
#                 data = input(f"{field}: ")
#                 if 0 < len(data) <= fields[field]:
#                     record.append(data)
#                     break
#                 else:
#                     print(f"Input must have at least 1 and maximum {fields[field]} characters!")

#         update_records(db_name, table, orig_record, format_data(record))
#     else:
#         print("\nRecord with this primary key entry does not exist.")

# Edit a record - Usman Rasheed Siddiqui
def edit_record(db_name, table):
    '''This function enables user to edit a record in selected database user entered.'''

    fields = get_fields(db_name)[table]  # Getting fields for the table
    field_names = list(fields.keys())  # Getting field names list
    fetch_record = search_record(db_name, table)    # Search for the record to be edited

    record = fetch_record.strip().split(",")    # Split the record into individual field values

     # Ensure that the record has the correct number of fields
    if len(record) != len(field_names):
        print(f"Error: Following Record does not exist!")    # Record does not exist or has an incorrect format
        return

    if record:           # Verifying that the record is not an empty list
        for i, field in zip(range(len(field_names)), field_names):        # Proceed to editing the record

            while True:
                edit_record = input(f"Edit new record for {field}: ")      # Entering new value for the field
                print()
                print(f"Editing field '{field}' with value: {edit_record}")     # Show the editing action
                print()
                # Ensure the length of the new value is valid for the field
                if 0 < len(edit_record) <= fields[field]:
                    record[i] = edit_record                    # Update the record at the correct index
                    break

                else:
                    print(f"The length of the input must be from 1 character to {fields[field]} characters")    # Prompt for valid input instruction

    else:
        print("Following record does not exist")    # If no record is found, display error message
        return


    # Format the edited record for writing
    formatted_edit = format_data(record)

    # Update the record in the table file
    update_records(db_name, table, fetch_record, formatted_edit)

    print("Record successfully updated")    # Confirmation message

# Delete a record using the primary key input by the user
def delete_record(db_name, table, record):
    if record:
        update_records(db_name, table, record)  # Remove the record from the table
        return 1    # Indicates the record was successfully deleted
    else:
        return 0    # If the record does not exist

# Searching whether a record with the primary key input exists in the database or not
def search_record(db_name, table):
    pk = get_primary_keys(db_name)[table]   # Get the primary key for the table

    pk_data = input(f"\nEnter the value for '{pk}' to get the record: ")    # primary key value from the user
    return record_exists(db_name, table, pk_data)   # Check if a record with the given primary key exists