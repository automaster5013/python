country = input().strip()
capital = input().strip()
print(f"Capital of {country} is {capital}")

###########################################################(방법01)

country = input().strip()
capital = input().strip()
print("Capital of " + country + " is " + capital)

###########################################################(방법02)

inp1 = input()
inp2 = input()
print("Capital of", inp1, " is", inp2)

###########################################################(방법03)

A = []
for _ in range(2):
    A.append(input())

print(f"Capital of {A[0]} is {A[1]}")

###########################################################(방법04)

