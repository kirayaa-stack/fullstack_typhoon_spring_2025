# python loops

fruits = ["apples", "banana", "strawberry"]

# Problem -- olon shirheg zuil bvl yah ve?
# SOlution -- Loop

# 1, FOR loop
for fruit in fruits:
    print(fruit)

# Range
# 0-5hurtel (5orohgui)
for i in range(5):
    print(i)      # 0 1 2 3 4

# 2-8hutel (8orohgui)
for i in range(2, 8):
    print(i)      # 2 3 4 5 6 7

# 1- 10 hurtel 2 alhamar
for i in range(1, 10, 2):
    print(i)      #1 3 5  7 9

# string buyu text
message = "Python"

# temdegt bureer davtalt
for char in message:
    print(char)

#enumarate
fruits = ["apples", "banana", "strawberry"]

# index and element in avah
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Tdorohoi index-s ehleh
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

#break
for i in range(10):
    if i == 5:
        break
    print(i)      #0, 1, 2, 3, 4

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)      #1, 3, 5, 7, 9

# break hereglegui uyd else ajillana
for i in range(5):
    print(i)
else:
    print("Successfull")

# breal hereglesen uyd else ajillahgui
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Failed")


#double loop Urjuuleh husnegt
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-----")

#Engiin davtalt
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)      # 1 4 9 16 25

# Jagsaltin oilgolt
squares = [i ** 2 for i in range(1, 6)]
print(squares)      # 1 4 9 16 25

# Nuhtsultei jagsaltin oilgolt
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)   # 4 16 36 64 100