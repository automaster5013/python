X = int(input())
# print(X)
N = int(input())
# print(N)

total_price = 0
for _ in range(N):
    a, b = map(int, input().split())
    total_price += (a * b)

if total_price == X:
    print("Yes")
else:
    print("No")

#####################################################################################################(방법01)

X = int(input())
# print(X)
N = int(input())
# print(N)

total_price = sum(a * b for _ in range(N) for a, b in [map(int, input().split())])
print("Yes" if total_price == X else "No")

#####################################################################################################(방법02)

X = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    X -= a * b

print("Yes" if X == 0 else "No")

#####################################################################################################(방법03)

X = int(input())
print("Yes" if sum((it := list(map(int, input().split())))[0] * it[1] for _ in range(int(input()))) == X else "No")

#####################################################################################################(방법04)

X=int(input())
A=[]
B=[]
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
for t in range(len(A)):
    total += A[t] * B[t]

if X == total:
    print('yes')
else:
    print('no')

#####################################################################################################(방법05)

X = int(input())
N = int(input())
c = []
for i in range(N):
    a, b = map(int, input().split())
    c.append(a * b)

if X == sum(c):
    print("Yes")
else:
    print("No")

#####################################################################################################(방법06)

