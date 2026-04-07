PI = 3.14
r = int(input())
area = r * r * PI
print("PI = {:.2f}".format(PI))
print("Area = {0} * {0} * {1} = {2:.1f}".format(r, PI, area))

#############################################################(방법01)

PI = 3.14
r = int(input())
area = r * r * PI
print("PI =", PI)
print(f"Area = {r} * {r} * {PI} = {round(area, 1)}")

#############################################################(방법02)

PI = 3.14
r = int(input())
area = r * r * PI
print(f"PI = {PI:.2f}")
print(f"Area = {r} * {r} * {PI} = {area:.1f}")

#############################################################(방법03)

r = int(input())
PI = 3.14
print("PI = ", PI)
print(f"Area = {r} * {r} * {PI} = {r * r * PI:.1f}")

#############################################################(방법04)

def Pi():
    return 3.14

def circle(N, pi):
    return round(N**2*pi, 1)

def OP(N, pi):
    return f"Area = {N} * {N} * {pi} ="

A = int(input())
pi = Pi()
area = circle(A, pi)

print(f"PI = {pi:.2f}")
print(OP(A, pi), area)

#############################################################(방법05)

