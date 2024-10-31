file = open("Hello.txt", "r")

for line in file:
    print(line)
    print(type(line))
    line = eval(line)
    print(type(line))
    print(line.keys())
