# intro into python list

#Problems = Variables

b = 7
print(b)

#Solution = Lists

fruits = ["apple", "banana", "strawberry"]
numbers = [1, 2, 3, 4, 5]
mixed= [1, "two", 3.0, True]
empty_list = []

print(type(fruits))
print(fruits)

# list index
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # strawberry

#negative index
print(fruits[-1]) #strawberry
print(fruits[-2]) # banana
print(fruits[-3]) # apple

# Change list
fruits[0] = "dragon_fruit"
print(fruits)

# element nemeh
fruits.append("kiwi")
print(fruits)

# Td bairlald elemnt orulah

fruits.insert(1, "mango")
print(fruits)

#element ustgah
fruits.remove("banana")
print(fruits)

#index-r element ustgah
removed_fruit = fruits.pop(1) #mangog ustgaj huvsagcid hadgalna
print(removed_fruit)
print(fruits)

#delete all elements
fruits.clear()
print(fruits)

# List methods
fruits = ["apple", "banana", "strawberry"]

# Lenght
print(len(fruits))

#Jagsaltig erembleh a-b-c
fruits.sort()
print(fruits)

#Jagsaltig urvuu erembleh c-b-a
fruits.reverse()
print(fruits)

#Find the element's index
print(fruits.index("banana"))

#Find the element's number
print(fruits.count("banana"))

#Copy the list
fruits_copy = fruits.copy()
print(fruits_copy)

#Negtgeh
more_fruits = ["kiwi", "mango"]
fruits.extend(more_fruits)
print(fruits)

#List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ehleh;tugsgul
print(numbers[2:5]) #[2 3 4]

# Ehleles tugsul hurtel
print(numbers[:5]) # {0, 1, 2, 3, 4}

# Ehleles jagsaltin tugsgul hurtel
print(numbers[5:]) # [5, 6, 7, 8, 9]

# Alham td:
print(numbers[1:9:2]) # 1, 3, 5, 7