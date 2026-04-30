for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end="")
        else:
            print("+", end="")
    print()

##############################################(방법01)

for i in range(5):
    print("+" * i + "#" + "+" * (4 - i))

##############################################(방법02)

for i in range(5):
    row = ["#" if i == j else "+" for j in range(5)]
    print("".join(row))

##############################################(방법03)

for i in range(5):
    row = ["+"] * 5
    row[i] = "#" 
    print("".join(row))

##############################################(방법04)

for k in range(25):
    if k % 6 == 0:
        print("#", end="")
    else:
        print("+", end="")
        
    if k % 5 == 4:
        print()

##############################################(방법05)


