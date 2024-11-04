from filing import *

def add_record(db, table):
    fields = eval(get_fields(open(f"./System Files/{db}.txt", "r"))) # Static argument for database file
    fields = fields[table]
    record = get_record_input(fields)
    orig_table = get_table("Students", open("./Data Files/sample_db.txt", "r"))
    table = eval(orig_table)
    table[record[0]] = record
    write_table(orig_table, str(table), "./Data Files/sample_db.txt")

def get_record_input(fields):
    record = list()

    for field in fields:
        while True:
            max_length = fields[field]
            data = input(f"Enter value for {field} (max. {max_length} characters): ")

            # Add conditional statement structure to check whether primary key field is unique or not
            if len(data) > max_length:
                print(f"Input too long. Please enter a value with no more than {max_length} characters.")
            else:
                break

        record.append(data)

    return record

add_record("sample_db", "Students") # Static argument for database and table