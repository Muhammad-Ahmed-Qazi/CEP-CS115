
# Dislay All Data Bases:

databases = open("DataBases.txt")
i = 1   #Line number
for line in databases:
    print(f'{i}.', line.strip())
    i += 1
# - For printing in list

databases.seek(0)
text = databases.read()
lines = text.split("\n")
print(lines)
databases.close()


# For allotting numbers to each database:

no_databases = []
for num in range(1, len(lines)+1):
    no_databases.append(num)
print("No. of database:", no_databases)

# Access a Data Base:

open_database = int(input("Enter the number of database you want to open: "))

open_db = lines[open_database - 1]
print(open_db)

with open(f"{open_db}",'w') as file:
    file.write("I exist!")  # User Input in file
