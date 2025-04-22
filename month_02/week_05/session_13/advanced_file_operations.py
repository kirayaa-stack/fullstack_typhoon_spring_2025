# Advanced File operations

with open('advanced.txt', 'r') as file:
    position = file.tell()
    content = file.read(5)
    file.seek(10)

    content = file.read()
    print(content)

    # iterate with line numbers
    with open('output.txt', 'r') as file:
        for i, line in enumerate(file, 1):
            print(f"Line: {i}: {line}")

# open binary image


#CSV files handling
with open('data.csv', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        print(values)

with open('output.csv', 'w') as file:
    file.write('Name,Age,City\n')
    file.write('John,25,New York\n')
    file.write('Alice,30,Boston\n')