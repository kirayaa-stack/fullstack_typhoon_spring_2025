#random = duriin utga

import random

roll_dice = random.randint(1, 6)
print(roll_dice)

is_heads = random.choice([True, False])
print("You flipped heads: " + str(is_heads))

menu =['sausage', 'ham', 'ramen', 'sushi']
is_food = random.choice(menu)
print('Your food is ' + is_food)

min = 1
max = 5

sum = 0 
for i in range(min, max):
    sum += i
print("The sum is" + str(sum))



number = 5
greater_than_zero = number > 0

if greater_than_zero:
   if number > 5:
        print(number)




num_sums = 20
print("We have 20 items in inventory")

while num_sums > 0:
    amount = int(input("How many would you like to buy? "))
    
    
    if amount <= num_sums:
        num_sums -= amount
        print("Now we have", num_sums, "left")
    else:
        print("There is not enough in inventory for that purchase")

print("All out!")