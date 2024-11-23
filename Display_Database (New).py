
#Extracting Files from file_handler
from file_handler import get_fields, get_records

db_name = input("Enter name of database you want to open: ")   # Entering Name of database
table = input("Enter name of the table you want to view: ")             #Entering name of the table to view

#   Displaying Records:
print(f'{table}: ')         # Printing record name

def display(db_name, table):
    '''This function is being used to fetch fields, their lengths and the respective records from the table
    in order to view them when the user gives the appropriate prompt'''


    fields = get_fields(db_name)[table]        # Fetching fields
    records = get_records(db_name, table)      # Fetching records

    #Iterating on record:
    for i in records:
        element = i.strip()
        element = element.split(', ')     # Converting the string present in the list to separate list separated by commas

    #print(element)

    # Fetching Field Lengths And Names

    field_lengths = list(fields.values())               # Fetching field lengths
    field_names = list(fields.keys())                   # Fetching field names

    # Display the field names as headings:

    header = ''
    for field in range(len(field_lengths)):
        header += f"{field_names[field]:{field_lengths[field]}} |"    # Displaying each heading separated by pipelines
    print(header.strip())                                             #   Removing whitespaces and newline commands

    '''
    # Display Records (values of each field):
    for record_key in range(len(records)):
        record_values = records[record_key]
        row=''
    '''

    #   Fetching Each record one by one:
    row = ''
    for values, field in zip(element, range(len(field_names))):

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





