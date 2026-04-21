a, b = map(int, input().split())
# print(a, b)
def swap_local(a, b):
    a, b = b, a
    print(f"함수 내부: a = {a}, b = {b}")

def swap_global():
    global a, b
    a, b = b, a
    print(f"함수 내부: a = {a}, b = {b}")

swap_local(a, b)
print(f"함수 외부: a = {a}, b = {b}")

swap_global()
print(f"함수 외부: a = {a}, b = {b}")

####################################################(방법01)

a, b = input().split()
print(a, b)

def change_loc(pa, pb):
    a, b = pb, pa
    print(f"함수 내부: a = {a}, b = {b}")

change_loc(a, b)
print(f"함수 외부: a = {a}, b = {b}")

change_loc()
print(f"함수 외부: a = {a}, b = {b}")

####################################################(방법02)

def change(x, y):
    x, y = y, x
    print(f'함수 내부: a = {x}, b = {y}')

a, b = map(int, input().split())

change(a, b)
print(f'함수 외부: a = {a}, b = {b}')

change(a, b)
a, b = b, a
print(f'함수 외부: a = {a}, b = {b}')

####################################################(방법03)

def change(x, y):
    x, y = y, x
    print(f'함수 내부: a = {x}, b = {y}')

a, b = map(int, input().split())

change(a, b)
print(f'함수 외부: a = {a}, b = {b}')

change(a, b)
a, b = b, a
print(f'함수 외부: a = {a}, b = {b}')

####################################################(방법04)


