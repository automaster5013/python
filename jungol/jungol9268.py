n = int(input())
# print(n)
for i in range(n, 4, -1):
    print(i)

##############################################(방법01)

n = int(input())
# print(n)
i = n
while i >= 5:
    print(i)
    i -= 1

##############################################(방법02)

n = int(input())
# print(n)
print('\n'.join(map(str, range(n, 4, -1))))

##############################################(방법03)

N = int(input())
# print(N)

for x in range(N, 4, -1):
    print(x)

##############################################(방법04)

N = int(input())
# print(N)

while 5 <= N:
    print(N)
    N -= 1      # (N = N - 1)과 동일

##############################################(방법05)

