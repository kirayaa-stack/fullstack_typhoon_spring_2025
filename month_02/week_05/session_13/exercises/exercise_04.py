with open('students.csv', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        print(values)
    

average_grades = ("")