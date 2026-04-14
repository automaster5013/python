N = int(input())
# print(N)

total = 0
i = 1

while i <= N:
    total += i
    i += 1

print(total)

####################################################(방법01)

N = int(input())
# print(N)
nums = list(range(1, N + 1))

total = 0
while nums:
    total += nums.pop()

print(total)

####################################################(방법02)

N = int(input())
# print(N)
total = i = 0

while True:
    i += 1
    if i > N:
        break
    total += i

print(total)

####################################################(방법03)

N = int(input())
# print(N)
total = 0

while N > 0:
    total += N
    N -= 1

print(total)

####################################################(방법04)

N = int(input())
# print(N)
sum = 0
for i in range(1, N+1):
    # print(i)
    sum += i

print(sum)

####################################################(방법05)

N = int(input())
# print(N)
sum = 0
i = 1
while i <= N:
    sum += i
    i += 1
print(sum)

####################################################(방법06)

