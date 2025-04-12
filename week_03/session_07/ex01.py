#Python loop -FOR

#recapture

colors = ['red', 'yellow','blue', 'green', 'purple']  #list
print(colors)

#print our 'blue'
print(colors[2])   #blue
print(colors[3])
print(colors[4])

#Solution - LOOP
#FOR - LOOP
for i in colors:
    print(i)

#FOR- RANGE
for i in range(9):
    print(i)

for i in range(0, 10):
    print(i)
for i in range(3, 10, 3):
    print(i)

#WHILE- LOOP
i = 1
while i < 9:
    print(i)     #duusgahgui bol infinite loop ctrl+c gej garna
    i = i+ 1     #i +=1

i = 10
while i <= 100:
    print(i)
    i = i +1

i = 20
while i <= 60:
    print(i)
    i = i + 2
i = 20
while i <= 60:
    if i % 2 ==0:
        print(i)
    i = i + 1

#