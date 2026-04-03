N = int(input())
# print(N)
i = 5
while i <= N:
    print(i)
    i += 2

#################################(방법01)

N = int(input())
# print(N)
for i in range(5, N + 1):
    if i & 1:   # & (:비트 연산자)
        print(i)

#################################(방법02)

N = int(input())
# print(N)
for i in range(5, N + 1, 2):
    print(i)

#################################(방법03)

N = input()
# print(N)
for i in range(5, int(N) + 1, 2):
    print(i)

#################################(방법04)

N = input()
# print(N)
start = 5
while start <= int(N):
    print(start)
    start += 2    # start = start + 2

#################################(방법05)

