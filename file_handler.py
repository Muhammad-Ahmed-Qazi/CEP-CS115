import os
import linecache

def create_path(name, table_opt="s"):
    if table_opt == 's':
        return f"{os.getcwd()}/System Files/{name}.txt"
    else:
        return f"{os.getcwd()}/Data Files/{name}/{table_opt}.txt"

def setup_database(db_name, info):
    try:
        os.mkdir(f"Data Files/{db_name}")
    except FileExistsError:
        return 0

    with open(create_path('db_names'), 'a+') as file:
        file.write(db_name + '\n')

    # Writing formatted data for system file
    with open(create_path(db_name), "w") as file:
        file.write(info[0])

    for table in info[1]:
        with open(create_path(db_name, table), "w"):
            pass

    return 1

def db_list():
    with open(create_path("db_names"), "r") as file:
        db_names = file.readlines()
        return [db_name.strip() for db_name in db_names]

def tables_list(db_name):
    tables = linecache.getline(create_path(db_name), 2)
    return eval(tables)

def get_fields(db_name):
    fields = linecache.getline(create_path(db_name), 5)
    return eval(fields)

def write_record(db_name, table, info, edit=""):
    with open(create_path(db_name, table), "a") as file:
        if not edit:
            file.write(info)
        else:
            pass
