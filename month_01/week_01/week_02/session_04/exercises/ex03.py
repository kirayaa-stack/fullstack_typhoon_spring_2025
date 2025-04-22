import math

a = abs(-15)
print(f"a= {abs(-15)}")
sqrt_result = math.sqrt(25)
print(f"25n yzguur = {sqrt_result}")
x = 4.3
towards_minus_infinity = math.nextafter(x, -math.inf)
print(f" hasah hyzgarlu = {towards_minus_infinity}")
y = 4.7
towards_positive_infinity = math.nextafter(y, math.inf)
print(f"eyreg hyzgarlu = {towards_positive_infinity}")

c = math.ceil(4.3)
print(f"c= {math.ceil(4.3)}")

math.floor(4.7)
print(f"d= {math.floor(4.7)}")
math.factorial(5)
print(f"f= {math.factorial(5)}")
math.sin(90)
print(f"sin90= {math.sin(90)}°")
math.sqrt(99)
print(f"99n yzgur = {math.sqrt(99)}")


a = 4.56867 
print(f"Result with ceil: {math.ceil(a)}")
print(f"Result with floor: {math.floor(a)}")



decimal_num = 42
print(f" decimal number 1 is : {str(decimal_num)}")
print(f" octal number 1 is : {oct(decimal_num)}")
print(f" hexadecimal number 1 is : {hex(decimal_num)}")


binary_num = bin(decimal_num)
print(f" octal number 2 is : {oct(decimal_num)}")
print(f" hexadecimal  number 2 is : {hex(decimal_num)}")

binary_num = "1010101"
print(f" octal system is : {str(binary_num)}")
octal_num = "52"
print(f" octal system 3 is : {str(octal_num)}")
hex_num = "2A"
print(f" hexadecimal number 3 is: {str(hex_num)}")