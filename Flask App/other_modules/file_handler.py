import os
import linecache

def create_path(name, table_opt="s"):
    if table_opt == 's':
        # return os.path.join(app.root_path, 'static', 'data', f'System Files/{name}.txt')
        return f"static/data/System Files/{name}.txt"
    else:
        # return os.path.join(app.root_path, 'static', 'data', f'Data Files/{name}.txt')
        return f"static/data/Data Files/{name}/{table_opt}.txt"

def setup_database(db_name, info):
    try:
        os.mkdir(f"static/data/Data Files/{db_name}")
    except FileExistsError:
        return 0

    with open(create_path('db_names'), 'a+') as file:
        file.write(db_name + '\n')

    # Writing formatted data for system file
    with open(create_path(db_name), "w") as file:
        file.write(info[0])

    for table in info[1]:
        print("Table:", table)
        with open(create_path(db_name, table), "w"):
            pass

    return 1

def get_db_names():
    with open(create_path("db_names"), "r") as file:
        db_names = file.readlines()
        return [db_name.strip() for db_name in db_names]

def get_tables(db_name):
    tables = linecache.getline(create_path(db_name), 2)
    return eval(tables)

def get_fields(db_name):
    fields = linecache.getline(create_path(db_name), 5)
    return eval(fields)

def get_primary_keys(db_name):
    pk = linecache.getline(create_path(db_name), 8)
    return eval(pk)

def write_record(db_name, table, info):
    with open(create_path(db_name, table), "a") as file:
        file.write(info)

def record_exists(db_name, table, pk):
    with open(create_path(db_name, table), "r") as file:
        for line in file:
            if pk in line:
                return line
    return ""

def get_records(db_name, table):
    with open(create_path(db_name, table), "r") as file:
        return file.readlines()

def update_records(db_name, table, record, edit=""):
    records = get_records(db_name, table)
    with open(create_path(db_name, table), "w") as file:
        for line in records:
            if not edit:
                if record != line:
                    file.write(line)
            else:
                if record == line:
                    file.write(edit)
                else:
                    file.write(line)