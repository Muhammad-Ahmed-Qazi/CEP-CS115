
from file_handler import get_db_names, get_fields, get_records, get_tables, update_records


db_names = get_db_names()  # Fetching database names

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

def editing_database(db_name, table):

    fields = get_fields(db_name)[table]         # Fetching fields
    print("field:",fields)

    records = get_records(db_name, table)       # Fetching records
    records = records[0].strip().split(', ')
    print("record:",records)

    field_names = list(fields.keys())           # Fetching field names
    print("field_names:",field_names)

    look_record = input("For which record are you working for?: ")



    for field in field_names:
        while True:
            edit_record = input(f"Edit record for {field}: ")       # Entering new value for the field
            if 0 < len(edit_record) <= fields[field]:               # Checking length of the input
                records.append(edit_record)                         # Editing Record
                break
            else:
                print(f"The length of the input must be from 1 character to {fields[field]} characters")

    update_records(db_name, table, records)

editing_database(db_name, table)