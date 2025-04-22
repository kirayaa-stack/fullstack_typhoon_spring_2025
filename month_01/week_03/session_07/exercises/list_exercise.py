# exercise 1
fav_food = ["curry", "ysnii shul", "spagetti", "sausage roll", "tsuivan"]
print(fav_food[0])
print(fav_food[4])
print(fav_food[3])

#exercise 2
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[3] = "7"
print(numbers)
numbers.insert(-4, 8)
print(numbers)
numbers.insert(0, 9)
print(numbers)
numbers.remove(3)
print(numbers)

#exercise 3
number = [2, 3, 4, 5, 6, 7, 8, 9]
print(number[2:])
print(number[:9])
number_copy = number.copy()
print(number_copy)
print(len(number))

#exercise 4
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:3])
print(numbers[-3:])
print(numbers[2:7])
print(numbers[1:9:2])

#exercise 5
lists = ["plant", "desk", "mouse", "tv"]
for list in lists:
    print(list)
for index, list in enumerate(lists):
    print(f"{index}: {list}")

#exercise 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [x**2 for x in range(1, 11)]
print(numbers)
numbers = [x**2 for x in range(6 , 11)]
print(numbers)

#exercise 7
i = 1
while i <= 10:
    print(i)
    i += 1

#exercise 8
for i in range(2, 20, 2):
    print(i)

#exercise 9
names = ["Bold", "Saraa","Dorj", "Nara"]
for i in names:
    print(i)

#exercise 10
for i in range(1, 10):
    if i // 7 == 1:
        break
    print(i)