# python variables
name = "John"
age = 25
height = 1.75
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

x = y = z = 0
print( x, y, z)
a, b, c = 1, 2, 3
print(a, b, c)
coordinates = (3, 4)
x, y = coordinates
print(x,y) # 3 4

a, b = 5, 10
a,b = b,a  
print(a,b) #10 5

x = 10



float_number = float(10)  #10.0
integer = int(3.14) 
string_number = str(42)

print(type(float_number))
print(type(integer))
print(type(string_number)) 

is_active = True
is_completed = False

# AND logic - 2 utga 2la unen
print(False and False) #false
print(False and True) #false
print(True and False) #false
print(True and True) #True
#OR logic ali neg utga ni unen baival unenig ni
print(False or False) #False
print(True or False) #True
print(False or True) #True
print(True or False) #True
#NOT logic boolean ii esreg
print(not False) #true
print(not True) #False


first_fruit = fruits [0]
last_fruit = fruits[-1]

#jagsalt uurchluh
fruits.append("ulaan looli") #tugsguld nemeh
fruits.insert(1, "mango") #td bairlald orulah
fruits.remove("banana") #utgar ni hasah
popped_fruit = fruits.pop() #suulin elementig hasaj butsah

#jagsalt hesegclel
numbers = [0, 1, 2, 3, 4, 5]
subset = numbers[1:4] #[1,2 ,3]


#hyzgaar uusgeh
numbers = range(5)  # 0, 1, 2, 3, 4, 5,
print(numbers)
#range (ehleh,tugsguh)
numbers = range(2, 7)
print(numbers)
#range(ehlel, tugsgul, alham)
even_numbers = range(0, 10, 2)  # [0, 2, 4, 6,  8]
print(even_numbers)
#hyzgarin jagsaltbolgoh
numbers_list = list(range(5)) # [0, 1, 2, 3, 4]
print(numbers_list)


x = 10 #undsen onoolt
x += 5     # x = x + 5 15
x -= 3     # x = x - 3 12
x *= 2     # x = x * 2 24
x /= 4     # x = x / 4 6.0
x //= 2    # x = x // 2 3.0
x %= 2     # x = x % 2 1.0
x **= 3    # x = x ** 3 1.0

a = 10
b = 5
equal = a ==b      #false
not_equal = a !=b    #true
greater_than = a > b   #true
less_than = a < b    #false
greater_equal = a >= b   #true
less_equal = a <= b     #false
print(equal = a ==b)