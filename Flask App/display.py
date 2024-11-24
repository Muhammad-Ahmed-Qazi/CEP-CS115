from file_handler import get_fields, get_primary_keys, record_exists

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
                    <button type="button" onclick="process('{ db_name }', '{ table }', 'edit_check')" class="btn btn-primary float-start">Submit</button>
                </div>
            </form>
            """

    return form

def edit_save_fields(db_name, table, pk):
    fields = get_fields(db_name)[table]
    record = record_exists(db_name, table, pk)

    form = '<div class="container p-2"><h3 class="">Edit an existing Record</h3><p class="text-muted">Enter the primary key to search for edit an existing record.</p></div>'
    form += f'<form class="p-3" method="POST" id="edit_form">'
    
    form += f"""<div class="row g-3">
                <div class="col-8 mb-1">
                    <label for="{pk}_name" class="form-label">{pk}</label>
                    <input type="text" class="form-control border-secondary" id="{pk}_name" name="{pk}" maxLength="{fields[pk]}" required>
                </div>
            </div>"""

    form += f"""<div class="clearfix mt-3">
                    <button type="button" onclick="process('{ db_name }', '{ table }', 'edit_check')" class="btn btn-primary float-start">Submit</button>
                </div>
            </form>
            """

    return form

def delete_fields(db_name, table):
    pk = get_primary_keys(db_name)[table]
    fields = get_fields(db_name)[table]

    form = '<div class="container p-2"><h3 class="">Delete a Record</h3><p class="text-muted">Enter the primary key to search for delete a record.</p></div>'
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