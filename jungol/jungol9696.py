class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def get_category(self):
        if self.age >= 18:
            return "adult"
        else:
            return "child"

    def display(self):
        category = self.get_category()
        print(f"{self.name}({self.age}) : {category}")

for _ in range(2):
    name, age = input().split()
    p = Person(name, age)
    p.display()

###############################################################(방법01)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.category = "adult" if self.age >= 18 else "child"

    def __str__(self):
        return f"{self.name}({self.age}) : {self.category}"

p1_data = input().split()
p2_data = input().split()

person1 = Person(*p1_data)
person2 = Person(*p2_data)

print(person1)
print(person2)

###############################################################(방법02)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

people = []

for _ in range(2):
    n, a = input().split()
    # print(n, a)
    people.append(Person(n, a))

for p in people:
    category = "adult" if p.age >= 18 else "child"
    print(f"{p.name}({p.age}) : {category}")

###############################################################(방법03)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        isOld = 'child'
        if age >= 18:
            isOld = 'adult'
        else:
            isOld = 'child'

        print(f"{name}({age}) : {isOld}")

for x in range(2):
    name, age = input().split()
    obj = Person(name, age)
    obj.print()

###############################################################(방법04)

