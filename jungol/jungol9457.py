K = 0
def GetDiff(x):
    global K
    return abs(x - K)

K = int(input())
venus = list(map(int, input().split()))

for x in venus:
    print(GetDiff(x))

#################################################################(방법01)

class SuperStar:
    K = 0

def GetDiff(n):
    return abs(n - SuperStar.K)

SuperStar.K = int(input())
venus = map(int, input().split())

print(*(GetDiff(x) for x in venus), sep='\n')

#################################################################(방법02)

K = int(input())
# print(K)
lst = map(int, input().split())

# for i in range(len(lst)):
#     print(lst[i])

def k_diff(param):
    d = abs(K - param)
    return d

for i in range(3):
    ret = k_diff(lst[i])
    print(ret)

#################################################################(방법03)

K = int(input())
def gap(n):
    global K
    return abs(K-n)

a, b, c = (map(int, input().split()))

print(gap(a))
print(gap(b))
print(gap(c))

#################################################################(방법04)








