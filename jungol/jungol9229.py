age = int(input())
# print(age)

if age >= 13:
    print("Middle Scoole")
else:
    print("Elementary Scoole")

#############################################(방법01)

age = int(input())
# print(age)
schools = ["Elementary School", "Middle School"]
print(schools[age >= 13])

#############################################(방법02)

age = int(input())
# print(age)
print("Middle School" if age >= 13 else "Elementary School")

#############################################(방법03)

age = int(input())
# print(age)
is_middle = int(age >= 13)
print(["Elementary School", "Middle School"][is_middle])

#############################################(방법04)

