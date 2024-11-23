from file_handler import get_db_names, get_fields, get_records, get_tables, update_records, get_primary_keys, record_exists

db_names = get_db_names()  # Fetching database names

def search_record(db_name, table):
    pk = get_primary_keys(db_name)[table]

    pk_data = input(f"\nEnter the value for '{pk}' to get the record: ")
    return record_exists(db_name, table, pk_data)

i = 1
for db in db_names:
    print(f'{i}. {db}')
    i += 1

db_name = input("Enter database name: ")

tables = get_tables(db_name)                    #   Fetching Respective Tables in database

j = 1
for tble in tables:
    print(f'{j}. {tble}')
    j += 1

table = input("Enter table name: ")             # Enter table name

fields = get_fields(db_name)[table]  # Fetching fields
print("field:", fields)


field_names = list(fields.keys())  # Fetching field names
print("field_names:", field_names)

# Formatting record entries into a string to be written to the data files
def format_data(records):
    data_info = ""

    for field in records:
        data_info += field + ', '

    return data_info[:-2] + '\n'

def editing_database(db_name, table):

    global original_record

    look_record = search_record(db_name, table)
    records = look_record.split(",")

    #look_record = input("For which record are you working for?: ")          #Looking for the required record
    record_found = False
    for record in records:
        if record.strip() == look_record.strip():
            record_found = True
            break

    if not record_found:
        print("Following record does not exist")
        return

    for i, field in zip(range(len(field_names)), field_names):
        while True:

            edit_record = input(f"Edit record for {field}: ")       # Entering new value for the field

            print(f"Editing field {field} with value: {edit_record}")

            if 0 < len(edit_record) <= fields[field]:               # Checking length of the input
                records[i] = edit_record                            # Update the record at the correct index
                break

            else:
                print(f"The length of the input must be from 1 character to {fields[field]} characters")

    # Format the edited record for writing
    formatted_edit = format_data(records)
    print(f"Formatted updated record: {formatted_edit}")

    update_records(db_name, table, look_record, formatted_edit)

    print("Record successfully updated")

#  Call the function to start the process
editing_database(db_name, table)