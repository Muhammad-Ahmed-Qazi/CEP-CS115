from other_modules.file_handler import get_fields, get_primary_keys, record_exists, get_records
from other_modules.data_manipulation import search_record

# Function to generate an "Add Record" form with fields dynamically populated from the table schema
def add_fields(db_name, table):
    # Retrieve the schema for the specified table
    fields = get_fields(db_name)[table]

    # Initialize the form with a header and description
    form = '<div class="container p-2"><h3 class="">Add Fields</h3><p class="text-muted">Enter the data for respective fields.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    # Loop through each field in the table schema and create an input element for it
    for field, length in fields.items():
        form += f"""<div class="row g-3">
                    <div class="col-8 mb-1">
                        <label for="{field}_name" class="form-label">{field}</label>
                        <input type="text" class="form-control border-secondary" id="{field}_name" name="{field}" maxLength="{length}" required>
                    </div>
                </div>"""

    # Add a submit button to the form with AJAX functionality
    form += f"""<div class="clearfix mt-3">
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/process/{ db_name }/{ table }/add', 'modalContent')">
                        Add Record
                    </button>
                </div>
            </form>
            """
    return form

# Function to generate a form for checking an existing record for editing
def edit_check_fields(db_name, table):
    # Retrieve the primary key and schema for the specified table
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    # Initialize the form with a header and description
    form = '<div class="container p-2"><h3 class="">Edit an existing Record</h3><p class="text-muted">Enter the primary key to search for edit an existing record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    # Add an input field for the primary key
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

    # Add a button for checking the record with AJAX functionality
    form += f"""<div class="clearfix mt-3">
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/opendb/{ db_name }/{ table }/edit_save', 'modalContent')">
                        Check Record
                    </button>
                </div>
            </form>
            """
    return form

# Function to generate a form for editing an existing record
def edit_save_fields(db_name, table, pk):
    # Retrieve the schema and existing record for the specified primary key
    fields = get_fields(db_name)[table]
    lengths = list(fields.values())
    record = record_exists(db_name, table, pk).split(', ')

    # Return an alert if no record is found
    if record == ['']:
        return '<div class="alert alert-danger">No record with this primary key!</div>'

    # Initialize the form with a header and description
    form = '<div class="container p-2"><h3 class="">Edit an existing Record</h3><p class="text-muted">Enter the primary key to search for edit an existing record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    # Loop through each field to create input elements, making the primary key read-only
    for i, field in zip(range(len(fields)), fields):
        if i != 0:  # Non-primary key fields
            form += f"""<div class="row g-3">
                    <div class="col-8 mb-1">
                        <label for="{field}_name" class="form-label">{field}</label>
                        <input type="text" class="form-control border-secondary" id="{field}_name" name="{field}" maxLength="{lengths[i]}" value="{record[i].strip()}" required>
                    </div>
                </div>"""
        else:  # Primary key field
            form += f"""<div class="row g-3">
                    <div class="col-8 mb-1">
                        <label for="{field}_name" class="form-label">{field}</label>
                        <input type="text" class="form-control border-secondary" id="{field}_name" name="{field}" maxLength="{lengths[i]}" value="{record[i].strip()}" readonly="true">
                    </div>
                </div>"""

    # Add a button for saving the edited record
    form += f"""<div class="clearfix mt-3">
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/process/{ db_name }/{ table }/edit_save', 'modalContent')">
                        Edit Record
                    </button>
            </form>
            """
    return form

# Function to generate a form for deleting a record
def delete_fields(db_name, table):
    # Retrieve the primary key for the specified table
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    # Initialize the form with a header and description
    form = '<div class="container p-2"><h3 class="">Delete a Record</h3><p class="text-muted">Enter the primary key to search for delete a record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    # Add an input field for the primary key
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

    # Add a button for deleting the record
    form += f"""<div class="clearfix mt-3">
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/process/{ db_name }/{ table }/delete', 'modalContent')">
                        Delete Record
                    </button>
                </div>
            </form>
            """
    return form

# Function to generate a form for searching and displaying a record
def search_fields(db_name, table):
    # Retrieve the primary key for the specified table
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    # Initialize the form with a header and description
    form = '<div class="container p-2"><h3 class="">Search and Display a Record</h3><p class="text-muted">Enter the primary key to search for and display the record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    # Add an input field for the primary key
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

    # Add a button for searching the record
    form += f"""<div class="clearfix mt-3">
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/process/{ db_name }/{ table }/search', 'modalContent')">
                        Search
                    </button>
                </div>
            </form>
            """
    return form

# Function to display a selected record as a table
def display_selected(db_name, table, data):
    # Retrieve the schema and record based on the primary key
    fields = get_fields(db_name)[table]
    record = search_record(db_name, table, data).split(", ")

    # Return an alert if no record is found
    if record == ['']:
        return '<div class="alert alert-warning">No record with this primary key!</div>'

    # Initialize the table with headers
    table = """<div class="table-responsive">
                    <table class="table ">
                        <thead class="table-dark">
                        <tr>"""
    
    # Add column headers based on the schema
    for field in fields:
        table += f'<th scope="col">{field}</th>'
    table += """</tr>
                </thead>
                <tbody class="table-group-divider">
                    <tr>"""
    for value in record:
        table += f'<td>{value}</td>'
    table += """</tr>
            </tbody>
        </table>
    </div>"""

    return table

def display_all(db_name, table):
    # Get the field names for the specified table in the database
    fields = get_fields(db_name)[table]
    
    # Get all records for the specified table in the database
    records = get_records(db_name, table)
    
    # Print the records for debugging purposes
    # print("Records:", records)
    
    # If no records are found, return a warning message
    if records == []:
        return '<div class="alert alert-warning">Table is empty!</div>'
    
    # Start the HTML for displaying the table
    table = """<div class="table-responsive">
                    <table class="table ">
                        <thead class="table-dark">
                        <tr>"""
    
    # Create the table headers from the field names
    for field in fields:
        table += f'<th scope="col">{field}</th>'
    
    # Close the table header section
    table += """</tr>
                </thead>
                <tbody class="table-group-divider">"""
    
    # Loop through each record and create a row in the table
    for record in records:
        table += """<tr>"""
        
        # Split each record by ", " and insert the values into table cells
        for value in record.split(", "):
            table += f'<td>{value}</td>'
        
        # Close the row
        table += """</tr>"""
    
    # Close the table and div container
    table += """</tbody>
            </table>
        </div>"""
    
    # Return the generated table HTML
    return table