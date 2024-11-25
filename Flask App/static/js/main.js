// Function to add a new table input section to the form
function addTable() {
    const tableContainer = document.getElementById("tables");  // Get the container where tables will be added
    const tableIndex = tableContainer.children.length;  // Get the current number of tables to create a unique index

    // Create a new div for the table input
    const newTable = document.createElement("div");
    newTable.className = "mb-3";  // Apply margin-bottom for spacing
    newTable.id = `table_${tableIndex}_wrapper`;  // Unique ID for the wrapper div
    newTable.innerHTML = `
        <div class="row mb-5">
            <label for="table_${tableIndex}" class="form-label"><b>Table Name</b> *</label>
            <div class="col-8">
                <input type="text" class="form-control border-secondary" id="table_${tableIndex}" name="tables[${tableIndex}][name]"
                    required>  <!-- Input for table name -->
            </div>
            <div class="col">
                <button class="btn btn-outline-secondary" type="button" onclick="addField(${tableIndex})">
                    <i class="bi bi-plus"></i>Fields  <!-- Button to add fields to the table -->
                </button>
                <button class="btn btn-outline-danger" type="button" onclick="removeTable(${tableIndex})">
                    <i class="bi bi-dash"></i>Table  <!-- Button to remove the table -->
                </button>
            </div>
            <div class="g-3" id="fields_${tableIndex}">
                <!-- Container for the fields of this table -->
                <div class="row g-3">
                    <div class="col-6">
                        <label class="form-label">Field Name *</label>
                        <input type="text" class="form-control border-secondary"
                            name="tables[${tableIndex}][fields][0][name]" required>  <!-- Field name input -->
                        <div id="db_help" class="form-text pb-4">This field will be primary key for the table.
                        </div>
                    </div>
                    <div class="col-6 mb-3">
                        <div class="row">
                            <div class="col-10">
                                <label class="form-label">Max. chr. Length *</label>
                                <input type="number" class="form-control border-secondary"
                                    name="tables[${tableIndex}][fields][0][length]" placeholder="0" required>  <!-- Max. character length input -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    tableContainer.appendChild(newTable);  // Append the new table to the container
}

// Function to remove a table input section
function removeTable(tableIndex) {
    const tableToRemove = document.getElementById(`table_${tableIndex}_wrapper`);  // Get the table wrapper by ID
    tableToRemove.remove();  // Remove the table from the DOM
}

// Function to add a new field input for a specific table
function addField(tableIndex) {
    const fieldContainer = document.getElementById(`fields_${tableIndex}`);  // Get the field container for the specific table
    const fieldIndex = fieldContainer.children.length;  // Get the current number of fields to create a unique index

    // Create a new div for the field input
    const newField = document.createElement("div");
    newField.className = "row g-3";  // Apply grid layout for spacing
    newField.id = `field_${tableIndex}_${fieldIndex}`;  // Unique ID for the field div
    newField.innerHTML = `
        <div class="col-6">
            <label class="form-label">Field Name *</label>
            <input type="text" class="form-control border-secondary"
                name="tables[${tableIndex}][fields][${fieldIndex}][name]" required>  <!-- Field name input -->
        </div>
        <div class="col-6 mb-3">
            <div class="row">
                <div class="col-10">
                    <label class="form-label">Max. chr. Length *</label>
                    <input type="number" class="form-control border-secondary"
                        name="tables[${tableIndex}][fields][${fieldIndex}][length]" placeholder="0" required>  <!-- Max. character length input -->
                </div>
                <div class="col position-relative">
                    <button type="button" class="btn btn-outline-danger position-absolute bottom-0 end-0"
                        onclick="removeField(${tableIndex}, ${fieldIndex})"><i class="bi bi-dash"></i></button>  <!-- Button to remove the field -->
                </div>
            </div>
        </div>
    `;
    fieldContainer.appendChild(newField);  // Append the new field to the container
}

// Function to remove a specific field input
function removeField(tableIndex, fieldIndex) {
    const fieldToRemove = document.getElementById(`field_${tableIndex}_${fieldIndex}`);  // Get the field div by ID
    fieldToRemove.remove();  // Remove the field from the DOM
}

// Function to submit the database form to the server
function submit_db() {
    const dbName = document.getElementById('db_name').value;  // Get the database name input value
    const form = document.getElementById('db_form');  // Get the database form
    form.action = `/opendb/${dbName}`;  // Set the action URL for the form
    form.method = "POST";  // Set the form method to POST
    form.submit();  // Submit the form
}

// Function to submit a table form to the server
function submit_table(dbName) {
    const tableName = document.getElementById('table_name').value;  // Get the table name input value
    const form = document.getElementById('table_form');  // Get the table form
    form.action = `/opendb/${dbName}/${tableName}`;  // Set the action URL for the form
    form.method = "POST";  // Set the form method to POST
    form.submit();  // Submit the form
}

// Function to open a modal and fetch dynamic fields for an operation (e.g., insert, update)
function openModal(db, table, operation) {
    const modalContent = document.getElementById('modalContent');  // Get the modal content area
    // Fetch dynamic fields for the selected operation
    fetch(`/opendb/${db}/${table}/${operation}`)
        .then(response => response.text())  // Parse the response as text
        .then(html => {
            modalContent.innerHTML = html;  // Update the modal content with the received HTML
            const modal = new bootstrap.Modal(document.getElementById('operationModal'));
            modal.show();  // Show the modal
        })
        .catch(error => console.error('Error fetching fields:', error));  // Log any errors
}

/**
 * Submit form data via AJAX and update the UI with the response.
 * @param {string} formId - The ID of the form to be submitted.
 * @param {string} targetUrl - The URL to send the form data to.
 * @param {string} resultContainerId - The ID of the element to display the response.
 */
function submitFormViaAjax(formId, targetUrl, resultContainerId) {
    const form = document.getElementById(formId);  // Get the form by ID
    const resultContainer = document.getElementById(resultContainerId);  // Get the result container by ID

    // Prevent default form submission
    const formData = new FormData(form);  // Collect form data

    // Send the form data via AJAX
    fetch(targetUrl, {
        method: 'POST',
        body: formData  // Send the form data in the request body
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');  // Handle any network errors
            }
            return response.text();  // Expect JSON or HTML response
        })
        .then(data => {
            // Display the response in the target container
            resultContainer.innerHTML = `${data}`
        })
        .catch(error => {
            console.error('Error:', error);  // Log errors
            resultContainer.innerHTML = `
                <div class="alert alert-danger">An error occurred: ${error.message}</div>
            `;
        });
}

/**
 * Fetch and display the whole table from Flask.
 * @param {string} apiUrl - The URL endpoint to fetch the table data from.
 */
function displayTable(apiUrl) {
    const tableContainer = document.getElementById('modalContent');  // Get the container for the table data

    // Fetch the table data from Flask
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch table data.');  // Handle fetch errors
            }
            return response.text();  // Expect HTML response
        })
        .then(html => {
            // Update the table container with the received HTML
            tableContainer.innerHTML = html;
        })
        .catch(error => {
            console.error('Error:', error);  // Log errors
            tableContainer.innerHTML = `
                <div class="alert alert-danger">An error occurred: ${error.message}</div>`;
        }
    );
}
