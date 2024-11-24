from other_modules.file_handler import get_fields, get_primary_keys, record_exists, get_records
from other_modules.data_manipulation import search_record

def add_fields(db_name, table):
    fields = get_fields(db_name)[table]

    form = '<div class="container p-2"><h3 class="">Add Fields</h3><p class="text-muted">Enter the data for respective fields.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    for field, length in fields.items():
        form += f"""<div class="row g-3">
                    <div class="col-8 mb-1">
                        <label for="{field}_name" class="form-label">{field}</label>
                        <input type="text" class="form-control border-secondary" id="{field}_name" name="{field}" maxLength="{length}" required>
                    </div>
                </div>"""

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

def edit_check_fields(db_name, table):
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    form = '<div class="container p-2"><h3 class="">Edit an existing Record</h3><p class="text-muted">Enter the primary key to search for edit an existing record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

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

def edit_save_fields(db_name, table, pk):
    fields = get_fields(db_name)[table]
    lengths = list(fields.values())
    record = record_exists(db_name, table, pk).split(', ')

    if record == ['']:
        return '<div class="alert alert-danger">No record with this primary key!</div>'

    form = '<div class="container p-2"><h3 class="">Edit an existing Record</h3><p class="text-muted">Enter the primary key to search for edit an existing record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    for i, field in zip(range(len(fields)), fields):
        if i != 0:
            form += f"""<div class="row g-3">
                    <div class="col-8 mb-1">
                        <label for="{field}_name" class="form-label">{field}</label>
                        <input type="text" class="form-control border-secondary" id="{field}_name" name="{field}" maxLength="{lengths[i]}" value="{record[i].strip()}" required>
                    </div>
                </div>"""
        else:
            form += f"""<div class="row g-3">
                    <div class="col-8 mb-1">
                        <label for="{field}_name" class="form-label">{field}</label>
                        <input type="text" class="form-control border-secondary" id="{field}_name" name="{field}" maxLength="{lengths[i]}" value="{record[i].strip()}" readonly="true">
                    </div>
                </div>"""

    form += f"""<div class="clearfix mt-3">
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/process/{ db_name }/{ table }/edit_save', 'modalContent')">
                        Edit Record
                    </button>
            </form>
            """

    return form

def delete_fields(db_name, table):
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    form = '<div class="container p-2"><h3 class="">Delete a Record</h3><p class="text-muted">Enter the primary key to search for delete a record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

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

def search_fields(db_name, table):
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    form = '<div class="container p-2"><h3 class="">Search and Display a Record</h3><p class="text-muted">Enter the primary key to search for and display the record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

    form += f"""<div class="clearfix mt-3">
                    <!-- Button to trigger form submission -->
                    <button type="button" 
                            class="btn btn-primary" 
                            onclick="submitFormViaAjax('edit_form', '/process/{ db_name }/{ table }/search', 'modalContent')">
                        Search
                    </button>
                </div>
            </form>
            """

    return form

def display_selected(db_name, table, data):
    fields = get_fields(db_name)[table]
    record = search_record(db_name, table, data).split(", ")

    if record == ['']:
        return '<div class="alert alert-warning">No record with this primary key!</div>'

    table = """<div class="table-responsive">
                    <table class="table ">
                        <thead class="table-dark">
                        <tr>"""
    
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
    fields = get_fields(db_name)[table]
    records = get_records(db_name, table)
    
    print("Records:", records)

    if records == []:
        return '<div class="alert alert-warning">Table is empty!</div>'

    table = """<div class="table-responsive">
                    <table class="table ">
                        <thead class="table-dark">
                        <tr>"""
    
    for field in fields:
        table += f'<th scope="col">{field}</th>'
    table += """</tr>
                </thead>
                <tbody class="table-group-divider">"""

    for record in records:
        table += """<tr>"""
        for value in record.split(", "):
            table += f'<td>{value}</td>'
        table += """</tr>"""

    table += """</tbody>
            </table>
        </div>"""


    return table