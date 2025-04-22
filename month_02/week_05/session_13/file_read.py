# File Read

# open file

file = open('file_intro.md', 'r')
content = file.read()
print(content)
file.close()


 # File read line by line
file = open('file_intro.md', 'r')
for i in range(8):
    content = file.readline() #mur muruuur ni unshdag
    print(content)
file.close()

# File read all lines
file = open('file_intro.md', 'r')
content = file.readlines()
print(content)
file.close()

