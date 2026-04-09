def check_number(n):
    if n > 0:
        return 'positive'
    elif n < 0:
        return 'negative'
    else:
        return 'zero'

num = int(input())
# print(num)
print(check_number(num))

#########################################################(방법01)

def check_number(n):
    status_idx = (n > 0) - (n < 0)
    return ['zero', 'positive', 'negative'][status_idx]

num = int(input())
# print(num)
print(check_number(num))

#########################################################(방법02)

def check_number(n):
    mapping = {
        (n > 0): 'positive',
        (n < 0): 'negative',
        (n == 0): 'zero'
    }
    return mapping[True]

num = int(input())
# print(num)
print(check_number(num))

#########################################################(방법03)

def check_number(n):
    return (n > 0 and 'positive') or (n < 0 and 'negative') or 'zero'

num = int(input())
# print(num)
print(check_number(num))

#########################################################(방법04)

def check_number(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

inp = int(input())
# print(inp)
print(check_number(inp))

#########################################################(방법05)

inp = input()
print(inp)

def get_integer(p):
    ret = ""
    if p >0:
        ret = "positive"
    elif p < 0:
        ret = "negative"
    else:
        ret = "zero"

    return ret

r = get_integer(inp)
print(r)

#########################################################(방법06)

