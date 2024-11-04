# Getting dictionary containing fields and lengths of tables from system file of the opened database
def get_fields(file_handle):
    for line in file_handle:
        if line.strip() == "Fields & Lengths":
            return file_handle.readline()

    return ""

# Getting complete data of a specific table from data file of the opened database
def get_table(table, file_handle):
    for line in file_handle:
        if table in line:
            return file_handle.readline()

# Writing a modified line over an original line in a file
def write_table(original_line, new_line, file):
    with open(file, "r") as file_read: # Reading complete file
        data = file_read.readlines()

    with open(file, "w") as file_write: # Opening file for writing modified text
        for line in data:
            if line == original_line:
                line = new_line + '\n'

            file_write.write(line)