X, Y = map(float, input().split())
# print(X, Y)
if X >= 4.0 and Y >= 4.0:
    print("A grade")
elif X >= 3.0 and Y >= 3.0:
    print("B grade")
else:
    print("F grade")

##############################################(방법01)

X, Y = map(float, input().split())
# print(X, Y)
lowest = min(X, Y)

if lowest >= 4.0:
    print("A grade")
elif lowest >= 3.0:
    print("B grade")
else:
    print("F grade")

##############################################(방법02)

X, Y = map(float, input().split())
# print(X, Y)
match (X, Y):
    case (X, Y) if X >= 4.0 and Y >= 4.0:
        print("A grade")
    case (X, Y) if X >= 3.0 and Y >= 3.0:
        print("B grade")
    case _: 
        print("F grade")

##############################################(방법03)

X, Y = map(float, input().split())
# print(X, Y)
out = ""
if X >= 4.0 and Y >= 4.0:
    out = "A grade"
elif X >= 3.0 and Y >= 3.0:
    out = "B grade"
else:
    out = "F grade"

print(out)

##############################################(방법04)

