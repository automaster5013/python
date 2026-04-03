name1, age1 = input().split()
name2, age2 = input().split()
# print(name1, age1)
# print(name2, age2)
diff = int(age1) - int(age2)

print(f"{name1}'s age - {name2}'s age = {diff}")

#################################################################(방법01)

data = [input().split() for _ in range(2)]
# print(data)
names = [d[0] for d in data]
ages = [int(d[1]) for d in data]
diff = ages[0] - ages[1]

print(f"{names[0]}'s age - {names[1]}'s age = {diff}")

#################################################################(방법02)

p1 = input().split()
p2 = input().split()
# print(p1)
# print(p2)
diff = int(p1[1]) - int(p2[1])

print("{0}'s age - {1}'s age = {2}".format(p1[0], p2[0], diff))

#################################################################(방법03)

name1, age1 = input().split()
name2, age2 = input().split()
# print(name1, age1)
# print(name2, age2)
print(f"{name1}'s age - {name2}'s age = {int(age1) - int(age2)}")

#################################################################(방법04)

# input ----->
# Minsu 15 
# Kayoung 13

# output ----->
# Minsu's age - Kayoung's age = 2









