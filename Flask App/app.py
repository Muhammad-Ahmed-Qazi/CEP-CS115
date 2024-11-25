from flask import Flask, flash, render_template, request

# Importing functions from other modules for database setup, file handling, data manipulation, and display.
from other_modules.database_setup import create_database
from other_modules.file_handler import get_db_names, get_tables, get_fields
from other_modules.data_manipulation import search_record, delete_record, add_record, edit_record
from other_modules.display import *

# Initialize the Flask application
app = Flask(__name__)

# Route: Home page
@app.route('/')
def index():
    # Render the main page template
    return render_template('main.html')

# Route: Create a new database
@app.route('/createdb', methods=['GET', 'POST'])
def createdb():
    if request.method == 'POST':
        # Handle form submission to create a new database
        data = request.form
        create_database(data)  # Call the function to create the database
        return render_template('main.html')  # Redirect to the main page after creation
    
    # Render the database creation form template
    return render_template('createdb.html')

# Route: Open database selection
@app.route('/opendb', methods=['GET', 'POST'])
def opendb():
    # Retrieve the list of available database names
    db_names = get_db_names()
    select_options = ""

    # Generate HTML options for the database dropdown menu
    for db_name in db_names:
        if select_options == "":
            select_options = f'<option value="{db_name}" selected>{db_name}</option>'
        else:
            select_options += f'<option value="{db_name}">{db_name}</option>'

    # Render the database selection template with dropdown options
    return render_template('opendb.html', select_options=select_options)

# Route: View tables in the selected database
@app.route('/opendb/<db_name>', methods=['GET', 'POST'])
def tables(db_name):
    # Retrieve the list of tables in the selected database
    tables = get_tables(db_name)
    select_options = ""

    # Generate HTML options for the tables dropdown menu
    for table in tables:
        if select_options == "":
            select_options = f'<option value="{table}" selected>{table}</option>'
        else:
            select_options += f'<option value="{table}">{table}</option>'

    # Render the table selection template with dropdown options
    return render_template('opentable.html', db_name=db_name, select_options=select_options)

# Route: Editing operations for a specific table
@app.route('/opendb/<db_name>/<table>', methods=['GET', 'POST'])
def editing(db_name, table):
    # Render the editing page for the specified table
    return render_template('editing.html', db_name=db_name, table=table)

# Route: Perform operations (add, edit, delete, search) on table fields
@app.route('/opendb/<db_name>/<table>/<operation>', methods=['GET', 'POST'])
def operation_fields(db_name, table, operation):
    # Determine which operation to perform based on the URL
    if operation == 'add':
        return add_fields(db_name, table)  # Render the form to add a new record
    elif operation == 'edit_check':
        return edit_check_fields(db_name, table)  # Render the form to check/edit a record
    elif operation == 'edit_save':
        # Save the edited record
        return edit_save_fields(db_name, table, list(request.form.values())[0])
    elif operation == 'delete':
        return delete_fields(db_name, table)  # Render the form to delete a record
    elif operation == 'search':
        return search_fields(db_name, table)  # Render the form to search records
    return "Invalid operation", 400  # Handle invalid operations

# Route: Process operations (e.g., add, edit, delete, search) on table data
@app.route('/process/<db_name>/<table>/<operation>', methods=['GET', 'POST'])
def process(db_name, table, operation):
    # Determine which data manipulation operation to perform
    if operation == 'add':
        return add_record(db_name, table, request.form)  # Add a new record to the table
    elif operation == 'edit_save':
        return edit_record(db_name, table, request.form)  # Save edited record
    elif operation == 'delete':
        # Delete a record based on search criteria
        return delete_record(db_name, table, search_record(db_name, table, request.form))
    elif operation == 'search':
        return display_selected(db_name, table, request.form)  # Display search results
    elif operation == 'display':
        return display_all(db_name, table)  # Display all records in the table
    return "Invalid operation", 400  # Handle invalid operations

# Main entry point of the application
if __name__ == '__main__':
    # Start the Flask development server on localhost and port 5000
    app.run(host="127.0.0.1", port=5000)
