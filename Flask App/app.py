from flask import Flask, flash, render_template, request

from other_modules.database_setup import create_database
from other_modules.file_handler import get_db_names, get_tables, get_fields
from other_modules.data_manipulation import search_record, delete_record, add_record, edit_record
from other_modules.display import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/createdb', methods=['GET', 'POST'])
def createdb():
    if request.method == 'POST':
        # Handle form data here
        data = request.form
        create_database(data)
        return render_template('main.html')
    
    return render_template('createdb.html')

@app.route('/opendb', methods=['GET', 'POST'])
def opendb():
    db_names = get_db_names()
    select_options = ""

    for db_name in db_names:
        if select_options == "":
            select_options = f'<option value="{db_name}" selected>{db_name}</option>'
        else:
            select_options += f'<option value="{db_name}">{db_name}</option>'

    return render_template('opendb.html', select_options=select_options)

@app.route('/opendb/<db_name>', methods=['GET', 'POST'])
def tables(db_name):
    tables = get_tables(db_name)
    select_options = ""

    for table in tables:
        if select_options == "":
            select_options = f'<option value="{table}" selected>{table}</option>'
        else:
            select_options += f'<option value="{table}">{table}</option>'

    return render_template('opentable.html', db_name=db_name, select_options=select_options)

@app.route('/opendb/<db_name>/<table>', methods=['GET', 'POST'])
def editing(db_name, table):
    return render_template('editing.html', db_name=db_name, table=table)

@app.route('/opendb/<db_name>/<table>/<operation>', methods=['GET', 'POST'])
def operation_fields(db_name, table, operation):
    if operation == 'add':
        return add_fields(db_name, table)
    elif operation == 'edit_check':
        return edit_check_fields(db_name, table)
    elif operation == 'edit_save':
        return edit_save_fields(db_name, table, list(request.form.values())[0])
    elif operation == 'delete':
        return delete_fields(db_name, table)
    elif operation == 'search':
        return search_fields(db_name, table)
    return "Invalid operation", 400

@app.route('/process/<db_name>/<table>/<operation>', methods=['GET', 'POST'])
def process(db_name, table, operation):
    if operation == 'add':
        return add_record(db_name, table, request.form)
    elif operation == 'edit_save':
        return edit_record(db_name, table, request.form)
    elif operation == 'delete':
        return delete_record(db_name, table, search_record(db_name, table, request.form))
    elif operation == 'search':
        return display_selected(db_name, table, request.form)
    elif operation == 'display':
        return display_all(db_name, table)
    return "Invalid operation", 400

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="127.0.0.1", port=5000)
