name = "Kirayaa"
age = 22
height = 164
is_programming = True
languages = ["Python", "Javascrpit", "Java"]
person = {"name": "Kirayuu", "age": 22}
coordinates = (10, 20)
unique_numbers = {1, 2, 3, 4, 5,}

print(type(name))
print(type(age))
print(type(height))
print(type(is_programming))
print(type(languages))
print(type(person))
print(type(coordinates))
print(type(unique_numbers))

num = 42
float_number = float
integer = int(42.6)
string_number = str(42)
print(float_number)
print(integer)
print(string_number)
print(10 > 42)

a = 15
b = 7
addition_result = a + b
substraction_result = a - b
multiplication_result = a * b
division_result = a / b
remainder_result = a % b
exponentiation_result = a ** b
print(f"{a} + {b} = {addition_result}")
print(f"{type(addition_result)}")
print(f"{a} - {b} = {substraction_result}")
print(f"{type(substraction_result)}")
print(f"{a} * {b} = {multiplication_result}")
print(f"{type(multiplication_result)}")

import math
sqrt_result = math.sqrt(25)
print(f"25n yzguur = {sqrt_result}")
x = 4.3
towards_minus_infinity = math.nextafter(x, -math.inf)
print(f" hasah hyzgarlu = {towards_minus_infinity}")
y = 4.7
towards_positive_infinity = math.nextafter(y, math.inf)
print(f"eyreg hyzgarlu = {towards_positive_infinity}")