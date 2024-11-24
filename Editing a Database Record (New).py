from file_handler import get_db_names, get_fields, get_records, get_tables, update_records

from data_manipulation import search_record, format_data

db_names = get_db_names()  # Getting database names

i = 1
for db in db_names:  # Viewing all databases
    print(f'{i}. {db}')
    i += 1

db_name = input("Enter database name: ")  # Entering desired database name

tables = get_tables(db_name)  # Getting Tables in database

j = 1
for tble in tables:
    print(f'{j}. {tble}')
    j += 1

table = input("Enter table name: ")  # Entering table name

records = get_records(db_name, table)  # Getting records

def editing_record(db_name, table):
    '''This function enables user to edit a record in selected database user entered.'''

    fields = get_fields(db_name)[table]  # Getting fields

    field_names = list(fields.keys())  # Getting field names

    fetch_record = search_record(db_name, table)

    record = fetch_record.strip().split(",")

     #Ensure that the record has the correct number of fields
    if len(record) != len(field_names):
        print(f"Error: Following Record does not exist!")
        return


    if record:                                                                  # Verifying that the record is not an empty list
        for i, field in zip(range(len(field_names)), field_names):              # Proceed to editing the record

            while True:
                edit_record = input(f"Edit new record for {field}: ")               # Entering new value for the field
                print()
                print(f"Editing field '{field}' with value: {edit_record}")
                print()
                if 0 < len(edit_record) <= fields[field]:                       # Checking length of the input
                    record[i] = edit_record                                     # Update the record at the correct index
                    break

                else:
                    print(f"The length of the input must be from 1 character to {fields[field]} characters")

    else:
        print("Following record does not exist")
        return


    # Format the edited record for writing
    formatted_edit = format_data(record)

    update_records(db_name, table, fetch_record, formatted_edit)

    print("Record successfully updated")

#  Call the function to start the process
editing_record(db_name, table)


