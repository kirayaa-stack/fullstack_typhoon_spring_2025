class Cat:
    def hi(self):
        return f"{self.name} is a {self.color} cat"

    def __init__(self,name, color):
        self.name = name
        self.color = name
    def __repr__(self):
        return f"Cat(name={self.name} , color = {self.color})"


mittens = Cat("Mittens", "white")
luna = Cat("Luna", "black")

print(mittens)
print(repr(mittens))
print(mittens.hi())

print(luna)
print(repr(luna))
print(luna.hi())