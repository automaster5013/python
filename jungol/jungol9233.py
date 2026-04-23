a = int(input())
b = int(input())
# print(a, b)
if a >= 3 and b >= 3:
    print("High")
elif a >= 3 or b >= 3:
    print("Mid")
else:
    print("Low")

########################################(방법01)

a = int(input())
b = int(input())
# print(a, b)
count = (a >= 3) + (b >= 3)
if count == 2:
    print("High")
elif count == 1:
    print("Mid")
else:
    print("Low")

########################################(방법02)

a = int(input())
b = int(input())
# print(a, b)
results = ["Low", "Mid", "High"]
print(results[(a >= 3) + (b >= 3)])

########################################(방법03)

lst = [int(input()), int(input())]

high_lst = [x for x in lst if x >= 3]

dict = {2:"High", 1:"Mid", 0:"Low"}
print(dict[len(high_lst)])

########################################(방법04)

a = int(input())
b = int(input())
# print(a, b)
match (a >= 3, b >= 3):
    case (True, True):
        print("High")
    case (True, False) | (False, True):
        print("Mid")
    case _:
        print("Low")

########################################(방법05)

a = int(input())
b = int(input())
# print(a, b)
condition = {
    (True, True): "High",
    (True, False): "Mid",
    (False, True): "Mid",
    (False, False): "Low"
}

print(condition[(a >= 3, b >= 3)])

########################################(방법06)

a = int(input())
b = int(input())
# print(a, b)
score = (a >= 3) + (b >= 3) # 결과는 0, 1, 2 중 하나
results = ["Low", "Mid", "High"]

print(results[score])

########################################(방법07)

a = int(input())
b = int(input())
# print(a, b)
if a >= 3:
    if b >= 3:
        print("High")
    else:
        print("Mid")
else:
    if b >= 3:
        print("Mid")
    else:
        print("Low")

########################################(방법08)

