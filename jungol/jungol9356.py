nums = [1, 2, 3, 4, 5]  # 1번

last_val = nums.pop()
print(f"last: {last_val}")  # 2번

print(nums)
print(f"len: {len(nums)}")  # 3번

second_val = nums.pop(1)
print(f"second: {second_val}")  # 4번

print(nums)
print(f"len: {len(nums)}")  # 5번

################################################################(방법01)

nums = [1, 2, 3, 4, 5]

last_val = nums[-1]
nums = nums[:-1]
print(f"last: {last_val}\n{nums}\nlen: {len(nums)}\n")

second_val = nums[1]
nums = nums[:1] + nums[2:]
print(f"second: {second_val}\n{nums}\nlen: {len(nums)}")

################################################################(방법02)

nums = [1, 2, 3, 4, 5]

last_val = nums[len(nums)-1]
temp = []
for i in range(len(nums) - 1):
    temp.append(nums[i])
nums = temp
print(f"last: {last_val}\n{nums}\nlen: {len(nums)}\n")

second_val = nums[1]
temp = []
for i in range(len(nums)):
    if i != 1:
        temp.append(nums[i])
nums = temp
print(f"second: {second_val}\n{nums}\nlen: {len(nums)}")

################################################################(방법03)

nums = [1, 2, 3, 4, 5]

last_val = nums[len(nums)-1]
nums = nums[:len(nums)-1]
print(f"last: {last_val}\n{nums}\nlen: {len(nums)}\n")

second_val = nums[1]
for i in range(1, len(nums) - 1):
    nums[i] = nums[i+1]
nums = nums[:len(nums)-1]
print(f"second: {second_val}\n{nums}\nlen: {len(nums)}")

################################################################(방법04)

nums = [1, 2, 3, 4, 5]

last_val = nums[-1]
nums = [val for i, val in enumerate(nums) if i != len(nums)-1]
print(f"last: {last_val}\n{nums}\nlen: {len(nums)}\n")

second_val = nums[1]
nums = [val for i, val in enumerate(nums) if i != 1]
print(f"second: {second_val}\n{nums}\nlen: {len(nums)}")

################################################################(방법05)

