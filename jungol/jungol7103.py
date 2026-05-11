A = []
for _ in range(5):
    A.append(int(input()))

B = list(A)
C = list(reversed(A))
print(C)

for _ in range(3):
    B.append(int(input()))
print(B)
print(A)

##############################################(방법01)

A = [int(input()) for _ in range(5)]
B = A[:]
C = A[::-1]
print(C)

B.extend([int(input()) for _ in range(3)])
print(B)
print(A)

##############################################(방법02)

A = [int(input()) for _ in range(5)]
B = A.copy()
C = A.copy()
C.reverse()
print(C)

for _ in range(3):
    B.append(int(input()))
print(B)
print(A)

############################################(방법03)

def get_nums(count):
    return [int(input()) for _ in range(count)]

A = get_nums(5)
C = list(reversed(A))
print(C)

B = A + get_nums(3)

print(B)
print(A)

############################################(방법04)

lst = []
lst2 = []
lst3 = []

for i in range(8):
    a = int(input())
    lst.append(a)
    lst2 = lst[0:5]
    lst3 = list(reversed(lst2))
    
print(lst3)
print(lst)
print(lst2)

############################################(방법05)






























