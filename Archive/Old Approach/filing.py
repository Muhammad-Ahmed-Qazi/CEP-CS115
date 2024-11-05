# Getting names of all databases in the DBMS
def get_db_names():
    with open("./System Files/db_names.txt", "r") as file:
        return eval(file.readline())

# Creating path for required file
def create_path(folder, db_name):
    if folder == "s":
        return f"./System Files/{db_name}.txt"
    elif folder == "d":
        return f"./Data Files/{db_name}.txt"


# Getting dictionary containing fields and lengths of tables from system file of the opened database
def get_fields(db_name):
    with open(create_path("s", db_name), "r") as file:
        for line in file:
            if line.strip() == "Fields & Lengths":
                return file.readline()

    return ""

# Getting complete data of a specific table from data file of the opened database
def get_table(table, db_name):
    with open(create_path("d", db_name), "r") as file:
        for line in file:
            if table in line:
                return file.readline()

# Writing a modified line over an original line in a file
def write_table(original_line, new_line, db_name):
    with open(create_path("d", db_name), "r") as file_read: # Reading complete file
        data = file_read.readlines()

    with open(create_path("d", db_name), "w") as file_write: # Opening file for writing modified text
        for line in data:
            if line == original_line:
                line = new_line + '\n'

            file_write.write(line)

get_db_names()