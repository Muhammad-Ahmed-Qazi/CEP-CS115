"""
- The user should be able to create a new database by specifying field names and their corresponding
  maximum lengths.
- Two files will be created for each database:
    - System file: Stores the names of fields and their lengths.
    - Data file: Stores the actual records in a structured format.
"""
from file_handler import setup_database, get_db_names

def create_database(data):
    # Name of database
    name = data['db_name']
    db_names = get_db_names()
    db_names = [db_name.upper() for db_name in db_names]
    if name.upper() in db_names:
        print("Database already exists!")
        return 0
    
    keys = list(data.keys())
    keys.pop(0)
    tables = 1
    fields = list()
    
    table_dict = {}
    
    for key in keys:
        parts = key.split('[')
        table_index = int(parts[1][0])
        if table_index not in table_dict:
            table_dict[table_index] = {'name': '', 'fields': []}
        
        if 'name' in parts[2]:
            table_dict[table_index]['name'] = data[key]
        elif 'fields' in parts[2]:
            field_index = int(parts[3][0])
            if field_index >= len(table_dict[table_index]['fields']):
                table_dict[table_index]['fields'].append(['', 0])
            if 'name' in parts[4]:
                table_dict[table_index]['fields'][field_index][0] = data[key]
            elif 'length' in parts[4]:
                table_dict[table_index]['fields'][field_index][1] = int(data[key])
    
    master_dict = {}
    for table in table_dict.values():
        table_name = table['name']
        fields = {field[0]: field[1] for field in table['fields']}
        primary_key = list(fields.keys())[0] if fields else None
        master_dict[table_name] = {'fields': fields, 'primary_key': primary_key}
    
    data = master_dict

    return setup_database(name, format_data(data))

def format_data(data):
    sys_info = ""

    # List of tables
    sys_info += "Tables\n"
    tables = list(data.keys())
    sys_info += str(tables) + ('\n' * 2)

    # Dictionary of fields & lengths
    sys_info += "Fields & Lengths\n"
    fields = dict()
    for table in data:
        print(table, data[table])
        fields[table] = data[table]['fields']
    sys_info += str(fields) + ('\n' * 2)

    # Dictionary of primary keys
    sys_info += "Primary Keys\n"
    primary_keys = dict()
    for table in data:
        primary_keys[table] = data[table]['primary_key']
    sys_info += str(primary_keys) + '\n'

    return sys_info, tables