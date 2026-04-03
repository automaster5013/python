elements = [int(input()) for i in range(5)]
# print(elements)
print(*elements)

##############################################(방법01)

nums = []

for i in range(5):
    n = int(input())
    # print(n)
    nums.append(n)

for i in nums:
    print(i, end=" ")

##############################################(방법02)

lst = []

for i in range(5):
    x= int(input())
    lst.append(x)

for j in range(len(lst)):
    print(lst[j], end=' ')

##############################################(방법03)

class S:
    def __init__(self, N):
        self.N = N
    def I(self):
        if self.N >= 0:
            Q.append(str(self.N))

Q=[]
for i in range(5):
    N = int(input())
    P = S(N)
    P.I()

print(f"{' '.join(Q)}")

##############################################(방법04)

