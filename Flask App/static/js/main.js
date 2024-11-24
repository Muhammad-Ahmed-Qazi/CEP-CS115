// Function to add a new table input
function addTable() {
    const tableContainer = document.getElementById("tables");
    const tableIndex = tableContainer.children.length;

    const newTable = document.createElement("div");
    newTable.className = "mb-3";
    newTable.id = `table_${tableIndex}_wrapper`; // Unique ID for the wrapper
    newTable.innerHTML = `
        <div class="row mb-5">
            <label for="table_${tableIndex}" class="form-label"><b>Table Name</b> *</label>
            <div class="col-8">
                <input type="text" class="form-control border-secondary" id="table_${tableIndex}" name="tables[${tableIndex}][name]"
                    required>
            </div>
            <div class="col">
                <button class="btn btn-outline-secondary" type="button" onclick="addField(${tableIndex})">
                    <i class="bi bi-plus"></i>Fields
                </button>
                <button class="btn btn-outline-danger" type="button" onclick="removeTable(${tableIndex})">
                    <i class="bi bi-dash"></i>Table
                </button>
            </div>
            <div class="g-3" id="fields_${tableIndex}">
                <div class="row g-3">
                    <div class="col-6">
                        <label class="form-label">Field Name *</label>
                        <input type="text" class="form-control border-secondary"
                            name="tables[${tableIndex}][fields][0][name]" required>
                        <div id="db_help" class="form-text pb-4">This field will be primary key for the table.
                        </div>
                    </div>
                    <div class="col-6 mb-3">
                        <div class="row">
                            <div class="col-10">
                                <label class="form-label">Max. chr. Length *</label>
                                <input type="number" class="form-control border-secondary"
                                    name="tables[${tableIndex}][fields][0][length]" placeholder="0" required>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    tableContainer.appendChild(newTable);
}

// Function to remove a table
function removeTable(tableIndex) {
    const tableToRemove = document.getElementById(`table_${tableIndex}_wrapper`);
    tableToRemove.remove();
}

// Function to add a new field input for a specific table
function addField(tableIndex) {
    const fieldContainer = document.getElementById(`fields_${tableIndex}`);
    const fieldIndex = fieldContainer.children.length;

    const newField = document.createElement("div");
    newField.className = "row g-3";
    newField.id = `field_${tableIndex}_${fieldIndex}`; // Unique ID for the field
    newField.innerHTML = `
            <div class="col-6">
                <label class="form-label">Field Name *</label>
                <input type="text" class="form-control border-secondary"
                    name="tables[${tableIndex}][fields][${fieldIndex}][name]" required>
            </div>
            <div class="col-6 mb-3">
                <div class="row">
                    <div class="col-10">
                        <label class="form-label">Max. chr. Length *</label>
                        <input type="number" class="form-control border-secondary"
                            name="tables[${tableIndex}][fields][${fieldIndex}][length]" placeholder="0" required>
                    </div>
                    <div class="col position-relative">
                        <button type="button" class="btn btn-outline-danger position-absolute bottom-0 end-0"
                            onclick="removeField(${tableIndex}, ${fieldIndex})"><i class="bi bi-dash"></i></button>
                    </div>
                </div>
            </div>
    `;
    fieldContainer.appendChild(newField);
}

// Function to remove a field
function removeField(tableIndex, fieldIndex) {
    const fieldToRemove = document.getElementById(`field_${tableIndex}_${fieldIndex}`);
    fieldToRemove.remove();
}

function submit_db() {
    const dbName = document.getElementById('db_name').value;
    const form = document.getElementById('db_form');
    form.action = `/opendb/${dbName}`;
    form.method = "POST";
    form.submit();
}

function submit_table(dbName) {
    const tableName = document.getElementById('table_name').value;
    const form = document.getElementById('table_form');
    form.action = `/opendb/${dbName}/${tableName}`;
    form.method = "POST";
    form.submit();
}

function openModal(db, table, operation) {
    const modalContent = document.getElementById('modalContent');
    // Fetch dynamic fields for the selected operation
    fetch(`/opendb/${db}/${table}/${operation}`)
        .then(response => response.text())
        .then(html => {
            modalContent.innerHTML = html; // Update the modal with form fields
            const modal = new bootstrap.Modal(document.getElementById('operationModal'));
            modal.show(); // Open the modal
        })
        .catch(error => console.error('Error fetching fields:', error));
}

/**
 * Submit form data via AJAX and update the UI with the response.
 * @param {string} formId - The ID of the form to be submitted.
 * @param {string} targetUrl - The URL to send the form data to.
 * @param {string} resultContainerId - The ID of the element to display the response.
 */
function submitFormViaAjax(formId, targetUrl, resultContainerId) {
    const form = document.getElementById(formId);
    const resultContainer = document.getElementById(resultContainerId);

    // Prevent default form submission
    const formData = new FormData(form); // Collect form data

    // Send the form data via AJAX
    fetch(targetUrl, {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text(); // Expect JSON response
        })
        .then(data => {
            console.log(data)
            // Display the response in the target container
            // resultContainer.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
            resultContainer.innerHTML = `${data}`
        })
        .catch(error => {
            console.error('Error:', error);
            resultContainer.innerHTML = `
                <div class="alert alert-danger">An error occurred: ${error.message}</div>
            `;
        });
}
