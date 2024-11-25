# CEP-CS115
A Python-based Simple Database Management System (DBMS) developed as part of the Complex Engineering Project (CEP) for the CS115 course. Includes features for database creation, record manipulation, and a command-line interface (CLI) for user interaction.

## Overview

This project was made as an assignment for the first-year CP-115 Computer Programming course at the Department of Computer & Information Systems, NEDUET.

This project is a **Simple Database Management System (DBMS)** built using **Flask** (Python web framework) and **Bootstrap 5** for the front-end. The application allows users to create, manage, and manipulate databases and tables through a browser-based interface. It supports functionalities like creating tables, adding fields, and performing basic operations on the data.

## Features

- Create and open databases
- Add/remove tables dynamically
- Add/remove fields for each table
- Configure field properties such as name and maximum character length
- Perform CRUD operations (Create, Read, Update, Delete) on tables
- User-friendly interface with modals for operations

## Requirements

Before you begin, ensure you have the following installed on your system:

- **Python 3.8+** (Recommended version)
- **pip** (Python's package installer)

### Install dependencies

This project requires several Python libraries. You can install them using `pip`. Run the following command in your terminal:

`pip install -r requirements.txt`

The `requirements.txt` file contains a list of all dependencies required for the project, including:

- Flask
- Flask-WTF (for handling forms)
- Flask-SQLAlchemy (for database management)
- Other necessary packages (e.g., Bootstrap for styling)

### Setting up the project

1. **Clone the repository (if not already done)**: You can clone this project using Git, or you can directly download the project files.

	`git clone <repository-url>`

2. **Navigate to the project directory**:

	`cd <project-directory>`

3. **Install the dependencies**:

	`pip install -r requirements.txt`

### Running the Flask App

1. **Ensure the database is set up**: If the project involves setting up a new database, ensure that the database configuration is correctly defined in the `config.py` file.

2. **Run the Flask development server**: Use the following command to run the Flask development server:

	`python app.py`
	
	The server will start, and you can access the application by opening your browser and navigating to:
	
	`http://127.0.0.1:5000/`

### Project Structure

Here is an overview of the project files and their purposes:

- **app.py**: The main Flask application file that contains routes and logic for interacting with the database and rendering HTML templates.
- **templates/**: Directory containing HTML templates (views) used for rendering the frontend interface.
- **static/**: Contains static files such as CSS, JavaScript, and images. The frontend is built with Bootstrap 5.
- **requirements.txt**: List of dependencies required to run the project.
- **README.txt**: This documentation file.

### Using the Application

1. **Creating a Database**:
    - To create a new database, you can enter the database name in the text field and click **Create Database**.
    - The system will create a database file and allow you to proceed with adding tables.

1. **Creating Tables**:
    - Click on the **Add Table** button to create a new table.
    - Provide a table name and click **Fields** to add fields to the table.
    - You will be required to provide a field name and its maximum character length.

2. **Adding/Removing Fields**:
    - After creating a table, you can click **Fields** to add multiple fields.
    - Fields are removed using the **Remove** button next to each field input.

3. **Removing Tables**:
    - Tables can be removed by clicking the **Remove Table** button next to each table.

4. **Performing Operations on Tables**:
    - Select a table and perform CRUD operations (such as inserting, viewing, updating, or deleting data) via modals that pop up.

### Troubleshooting

1. **Flask not running?**    
    - Ensure you have activated your virtual environment.
    - Double-check if Flask is installed (`pip install flask`).
    - If you are using a specific port, make sure it's available.

2. **Dependencies missing?**
    - Ensure you’ve installed all required dependencies using `pip install -r requirements.txt`.
    - If a package installation fails, check your Python version and try upgrading pip:
    
    `pip install --upgrade pip`
    

3. **Database Not Found?**
    - If the database file is not found or you're unable to open it, ensure you’ve created the database correctly using the application interface.
    - Make sure your app has appropriate permissions to read/write in the project directory.

4. **AJAX Requests Fail?**
    - If the AJAX operations are not working, ensure your server is running correctly and reachable. Check the browser console for any errors.
    - Verify that the URLs used for AJAX requests are correct and the routes exist in your Flask app.

5. **Page not loading or UI issues?**
    - Clear your browser cache and refresh the page.
    - Check the browser console for any JavaScript errors that might be affecting the frontend.