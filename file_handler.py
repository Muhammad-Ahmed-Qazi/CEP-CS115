import os

def create_path(directory, file_name):
    if directory == 's':
        return f"{os.getcwd()}/System Files/{file_name}.txt"
    elif directory == 'd':
        return f"{os.getcwd()}/Data Files/{file_name}.txt"

def setup_database(name, info):
    with open(create_path('s', 'db_names'), 'a+') as file:
        file.write(name + '\n')

    # Writing formatted data for system file
    with open(create_path('s', name), "w") as file:
        file.write(info[0])

    with open(create_path('d', name), "w") as file:
        file.write(info[1])

