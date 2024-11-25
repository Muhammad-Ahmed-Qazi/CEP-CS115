from re import search

#Extracting Files from file_handler
from file_handler import get_fields, get_records
from data_manipulation import search_record

db_name = input("Enter name of database you want to open: ")   # Entering Name of database
table = input("Enter name of the table you want to view: ")             #Entering name of the table to view

#   Displaying Records:

def display(db_name, table):
    '''This function is being used to fetch fields, their lengths and the respective records from the table
    in order to view them when the user gives the appropriate prompt'''


    fields = get_fields(db_name)[table]        # Fetching fields
    records = get_records(db_name, table)      # Fetching records


    # Fetching Field Lengths And Names

    field_lengths = list(fields.values())               # Fetching field lengths
    field_names = list(fields.keys())                   # Fetching field names

    # Display the field names as headings:
    # For headings to be Bold And Italic
    bold_italic = '\033[1m\033[3m'
    reset = '\033[0m'

    header = ''
    for field in range(len(field_lengths)):
        header += f"{bold_italic}{field_names[field]:{field_lengths[field]}}{reset} |"    # Displaying each heading separated by pipelines
    print(header.strip())                                             #   Removing whitespaces and newline commands

    #Iterating on record:
    # Display Records (values of each field)
    for record in records:  # Loop through all records
        record = record.strip()  # Remove any leading/trailing whitespace/newline characters
        if not record:  # Skip empty lines if any
            continue
        record_values = record.split(', ')  # Split the record into its individual values

    #   Fetching Each record one by one:
        row = ''
        for values, field in zip(record_values, range(len(field_names))):

        # To determine appropriate spaces and alignment of pipes from top to bottom
            if len(field_names[field]) > field_lengths[field]:
                col_length = len(field_names[field])
            else:
                col_length = field_lengths[field]

            row += f'{str(values):{col_length}} |'      # To display each record separated by pipes

        print(row.strip())

# Calling function to display records:
display(db_name, table)

#help(display_database)

def selected_database(db_name, table):

    record = search_record(db_name, table).strip().split(",")
    fields = get_fields(db_name)[table]

    field_lengths = list(fields.values())               # Fetching field lengths
    field_names = list(fields.keys())                   # Fetching field names

    bold_italic = '\033[1m\033[3m'      # ANSI escape code for bold and italics
    reset = '\033[0m'               # ANSI escape code to reset the formatting

    # Creating a header string to display field names (column titles)
    header = ''
    for field in range(len(field_lengths)):
        # Adjusting the width of the display of respective fields based on the lengths and formatting using bold_italics
        header += f"| {bold_italic}{field_names[field]:{field_lengths[field]}}{reset} |"    # Displaying each heading separated by pipelines
    print(header.strip())                                             #   Removing whitespaces and newline commands

    if record:
        # Creating a row to display record's values in a neat and formatted way
        row = ''
        for values, field in zip(record, range(len(field_names))):

        # To determine appropriate spaces and alignment of pipes from top to bottom
            if len(field_names[field]) > field_lengths[field]:
                col_length = len(field_names[field])        # If field length is longer, use that length
            else:
                col_length = field_lengths[field]           # Otherwise, use the provided length


            row += f'| {str(values):{col_length}} |'      # To display each record separated by pipes

        # Display the formatted row for the record
        print(row.strip())

selected_database(db_name, table)

