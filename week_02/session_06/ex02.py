#logical operators

x = 5
y = 10

print(x > 0 and y > 0)  #true
print(x > 7 or y > 7)  #true
print(not x > 7) #true


#
i_was_born_in_mongolia = False
i_have_mongolian_passport = True

if i_was_born_in_mongolia and i_have_mongolian_passport:
    print("I'm mongolian")
else:
    print("I'm not mongolian")
