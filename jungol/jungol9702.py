class PersonAge:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

N = int(input())
# print(N)
people = []
for i in range(N):
    name, age = input().split()
    people.append(PersonAge(name, age))

for i in range(N):
    max_idx = i
    for j in range(i + 1, N):
        if people[j].age > people[max_idx].age:
            max_idx = j
    
    people[i], people[max_idx] = people[max_idx], people[i]

for p in people:
    print(f"Name:{p.name}, Age:{p.age}")

##################################################################(방법01)

class PersonAge:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    
    def output(self):
        print(f"Name:{self.name}, Age:{self.age}")

N = int(input())
# print(N)
people = [PersonAge(*input().split()) for i in range(N)]

for i in range(N - 1):
    for j in range(N - 1 - i):
        if people[j].age < people[j + 1].age:
            people[j], people[j + 1] = people[j + 1], people[j]

for p in people:
    p.output()

##################################################################(방법02)

class PersonAge:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

N = int(input())
# print(N)
people = [PersonAge(*input().split()) for i in range(N)]

people.sort(key=lambda x: x.age, reverse=True)

for p in people:
    print(f"Name:{p.name}, Age:{p.age}")

##################################################################(방법03)

