dict = {1:"one", 2:"two", 3:"three"}
while True:
    inp = int(input())
    if inp in dict:
        print(dict[inp])
    else:
        break

#############################################(방법01)

while True:
    inp = int(input())
    match inp:
        case 1: print("one")
        case 2: print("two")
        case 3: print("three")
        case _: break

#############################################(방법02)

lst = ["", "one", "two", "three"]
while (inp := int(input())) in [1, 2, 3]:
    print(lst[inp])

#############################################(방법03)

dict = {1:"one", 2:"two", 3:"three"}
while (word := dict.get(int(input()))):
    print(word)

#############################################(방법04)

dict = {1: "one", 2: "two", 3: "three"}

input_func = lambda: dict.get(int(input()))

for nums in iter(input_func, None):
    print(nums)

#############################################(방법05)

while True:
    num = int(input())
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    else:
        break

#############################################(방법06)

