#exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1

#exercise 2
for i in range(2, 20, 2):
    print(i)

#exercise 3
names = ["Bold", "Saraa","Dorj", "Nara"]
for i in names:
    print(i)

#exercise 4
for i in range(1, 10):
    if i // 7 == 1:
        break
    print(i)

# exercise 5
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# exercise 6
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-----")

#exercie 8
squares = [i **2 for i in range(1,6)]
print(squares)

#exercise 9
fruits = ["apple","banana","strawberry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}: {fruit}")

#exercie 10
person = {"name": "Bold", "age": "30","lives in": "Ulaanbaatar"}
for key, value in person.items():
    print(f"{key}: {value}")    