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

