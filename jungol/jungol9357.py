nums = []
for x in range(5):
    nums.append(int(input()))

print(nums)

nums.pop()
nums.pop()

print(nums)

##############################################################(방법01)

nums = [int(input()) for x in range(5)]
print(nums)

nums = nums[:-2]

print(nums)

##############################################################(방법02)

nums = [int(input()) for x in range(5)]
print(nums)

del nums[-2:]

print(nums)

##############################################################(방법03)

lst = list()
for i in range(5):
    inp = int(input())
    lst.append(inp)

print(lst)

for i in range(2):
    lst.pop()

print(lst)

##############################################################(방법04)


