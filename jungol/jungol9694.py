class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

name, age = input().split()

p = Person(name, int(age))
p.introduce()

###################################################(방법01)

class Person:
    def __init__(self, name, age):  # 멤버변수 초기화!!
        self.name = name
        self.age = age

    def print(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

name, age = input().split()

p1 = Person(name, age)
p1.print()

###################################################(방법02)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}.\nI am {self.age} years old."

name, age = input().split()
p = Person(name, int(age))
print(p)

###################################################(방법03)

class Box:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a,b=input().split()
d=Box(a,b)
print(f"My name is {d.name}.")
print(f"I am {d.age} years old.")

###################################################(방법04)

class My_name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name, age = input().split()
person = My_name(name, age)

print(f"My name is {person.name}.")
print(f"I am {person.age} years old.")

###################################################(방법05)

