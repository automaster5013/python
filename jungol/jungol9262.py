N = int(input())
# print(N)
for i in list(range(N + 1))[5:]:
    print(i)

######################################################(방법01)

N = int(input())
# print(N)
comp = 5
while True:
    print(comp)
    if comp == N:
        break
    comp += 1

######################################################(방법02)

# N = int(input())

# result = filter(lambda x: x >= 5, range(1, N + 1))

# for num in result:
#     print(num)

######################################################(방법03)

N = int(input())
# print(N)

for i in range(5, N+1):
    print(i)

######################################################(방법04)
# 무한 루프의 예제

# N = 1
# while True:
#     print(N)
#     N += 1

######################################################(방법05)




