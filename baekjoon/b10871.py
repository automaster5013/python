N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < X:
        print(i, end=' ')

###################################################(방법01)

N, X = map(int, input().split())
A = list(map(int, input().split()))

result = [i for i in A if i < X]
print(*result)

###################################################(방법02)

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(len(A)):
    if int(A[i]) < X:
        print(A[i], end=' ')

###################################################(방법03)

a, b = map(int,input().split())
list1 = list(map(int, input().split()))

hap = []
for i in list1:
    if i < b:
        hap.append(i)

print(*hap)

###################################################(방법04)

