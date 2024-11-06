import os
import linecache

def create_path(directory, file_name):
    if directory == 's':
        return f"{os.getcwd()}/System Files/{file_name}.txt"
    elif directory == 'd':
        return f"{os.getcwd()}/Data Files/{file_name}.txt"

def setup_database(db_name, info):
    with open(create_path('s', 'db_names'), 'a+') as file:
        file.write(db_name + '\n')

    # Writing formatted data for system file
    with open(create_path('s', db_name), "w") as file:
        file.write(info[0])

    with open(create_path('d', db_name), "w") as file:
        file.write(info[1])

def get_fields(db_name):
    # fields = linecache.getlines(create_path('s', db_name), )
    pass