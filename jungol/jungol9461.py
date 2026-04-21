a, b = map(int, input().split())
# print(a, b)
def globals_modify():
    global a, b
    if a > b:
        a //= 2
        b *= 2
    else:
        a *= 2
        b //= 2

globals_modify()
print(a, b)

###########################################(방법01)

a, b = map(int, input().split())
# print(a, b)
def calc():
    global a, b
    if a > b:
        a //= 2
        b *= 2
    else:
        b //= 2
        a * 2

calc()
print(a, b)

###########################################(방법02)

def cal(n1, n2):
    n1, n2 = map(int, input().split())
    return max(n1, n2) // 2, min(n1, n2) * 2

print(cal())

###########################################(방법03)












