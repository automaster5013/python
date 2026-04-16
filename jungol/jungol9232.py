weight = float(input())
# print(weight)

classes = [
    (50.80, "Flyweight"),
    (61.23, "Lightweight"),
    (72.57, "Middleweight"),
    (88.45, "Cruiserweight")
]

res = "Heavyweight"
for limit, name in classes:
    if weight <= limit:
        res = name
        break
print(res)

######################################################################################################(방법01)

weight = float(input())
# print(weight)

if weight <= 50.80:
    print("Flyweight")
elif weight <= 61.23:
    print("Lightweight")
elif weight <= 72.57:
    print("Middleweight")
elif weight <= 88.45:
    print("Cruiserweight")
else:
    print("Heavyweight")

######################################################################################################(방법02)

# match ~ case문으로도 변환 시도!!

######################################################################################################(방법03)

weight = float(input())
# print(weight)

if weight <= 50.80: 
    print("Flyweight")
elif weight <= 61.23: 
    print("Lightweight")
elif weight <= 72.57: 
    print("Middleweight")
elif weight <= 88.45: 
    print("Cruiserweight")
else: 
    print("Heavyweight")

######################################################################################################(방법04)

weight = float(input())

limits = [(50.80, "Flyweight"), (61.23, "Lightweight"), (72.57, "Middleweight"), (88.45, "Cruiserweight")]
result = next((name for limit, name in limits if weight <= limit), "Heavyweight")
print(result)

######################################################################################################(방법05)

