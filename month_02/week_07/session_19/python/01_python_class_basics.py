class Dog:
    """Simple dog class"""
    pass

banhar = Dog()  #object = bodit zuil
print(banhar)
bulldog = Dog()
print(bulldog)

# __init__ gedeg class function
class Cat:
    def __init__(self, name, race):
        self.name = name # class attribute, class variables
        self.race = race 
     
     #class function/method
    def meow(self):
        return f"Meow! I'm a {self.name}"

    
    def __str__(self):
        return f"{self.name} is {self.race}"
    
    def __repr__(self):
        return f"Cat(name={self.name}, race={self.race})"
    
# cat gedeg class-s 2turlin object uusge
#object oriented programming buyu object handaltat programclal
kiki = Cat("Kiki", "british short hair")
print(kiki)
print(kiki.name)
print(kiki.race)
print(kiki.meow())
print(repr(kiki))
koko = Cat("Koko", "england royal")
print(koko)
print(koko.name)
print(koko.race)
# class function call
print(koko.meow())
print(repr(koko))

# class identities
class Horse:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
black_horse = Horse("Black horse" , 3)
print(black_horse)
print(black_horse.age)
print(black_horse.name)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"

    def bark(self, sound):
        return f"{self.name} says {sound}"

sisi = Dog(name="sisi", age = 4)
kai = Dog("kai", age = 3)
print(sisi.description())
print(sisi.bark("Hov hov"))
print(kai.description())
print(kai.bark('Wan wan'))

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__account_number = "123456"
    
    def balance(self, value):
        if value < 0:
            raise ValueError("Balanve cannot be negative")
        self.__balance = value

kira_account = BankAccount("Kira", 1000000)
kira_account.balance(1000)
print(kira_account.balance)


# class dotor buruu attribute ashiglah
class Dog:

    #tricks = [] mistaken use of class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy') 
d.add_trick("roll,over")
e.add_trick("play dead")
print(d.trick)
print(e.trick)       