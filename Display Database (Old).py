


# For Displaying DataBase:

display_database = input("Enter name of database you want to open: ")  # DataBase .txt file name

    #   Fetching System Files:
with open(f"System Files/{display_database}.txt") as system_database:
    for line in system_database:
        if line.strip() == "Tables":        # Tables
            tables = eval(system_database.readline())
            print("Tables:", tables)
        elif line.strip() == "Fields & Lengths":    # Fields & Lengths
            fields_lengths = eval(system_database.readline())
            print("Fields & Lengths:", fields_lengths)
        elif line.strip() == "Primary Keys":        # Primary Keys
            primary_keys = eval(system_database.readline())
            print("Primary Keys:", primary_keys)

name_record = input("Enter name of record: ")
    #   Fetching Data Files:
with open(f"Data Files/{display_database}/{name_record}.txt") as existing_database:
        #name_record = input("Enter name of record: ")  # Enter Record Name

        if name_record not in tables:  # Checking For Record
            print("Table Not Found")
        else:
            database_dict = existing_database.readline().strip()  # Access String Line
            database_dict = database_dict.split(', ')  # Converting to List
            print(f"{name_record}:", database_dict)


#   Displaying Records:

def display(name_record, field_lengths, primary_keys):
    if name_record not in fields_lengths:
        print(f"Tables {name_record} not found")
        return

    # Fetching Field_Lengths

    field_lengths = field_lengths[name_record]
    field_names = list(field_lengths.keys())

    # Display the field names as headings:

    header =''
    for field in field_names:
        header += f"{field:{field_lengths[field]}} |"
    print(header.strip())
    '''
    # Display Records (values of each field):
    for record_key in range(len(database_dict)):
        record_values = database_dict[record_key]
        row=''
    '''
    # j = 0
    row = ''
    for values, field in zip(database_dict, field_names):
        if len(field) > field_lengths[field]:
            col_length = len(field)
        else:
            col_length = field_lengths[field]
        #print(record_values)
        row += f'{str(values):{col_length}} |'
            
           # j += 1
    print(row.strip())

display(name_record, fields_lengths, primary_keys)















