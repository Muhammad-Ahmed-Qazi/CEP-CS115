l(db_name, table):
    fields = get_fields(db_name)[table]
    records = get_records(db_name, table)

    header = "|"
    data = "|"

    for field in fields:
        header += f" \033[1m\033[3m{field:{fields[field]}}\033[0m |"

    print("\n" + header)

    field_names = list(fields.keys())
    field_lengths = list(fields.values())
    for record in records:
        record = record.split(",")
        for i in range(len(record)):
            if len(field_names[i]) > field_lengths[i]:
                col_length = len(field_names[i])
            else:
                col_length = field_lengths[i]
            data += f" {record[i].strip():{col_length}} |"
        print(data)
        data =