nums = []

for i in range(5):
    nums.append(int(input()))
print(nums)

for n in nums:
    print(n, end=' ')

#######################################(방법01)

nums = [int(input()) for i in range(5)]
print(nums)
print(*nums)

#######################################(방법02)

lst = []
for i in range(5):
    inp = int(input())
    lst.append(inp)

print(lst)
for i in lst:
    print(i, end=' ')

#######################################(방법03)

nums = []

i = 0  # 초기값 설정
while i < 5:  # 조건식
    nums.append(int(input()))
    i += 1  # 증감식 (이걸 빼먹으면 무한 루프!)

print(nums)

idx = 0  # 리스트 인덱스용 초기값
while idx < len(nums):  # 리스트 길이만큼 반복
    print(nums[idx], end=' ')
    idx += 1  # 다음 인덱스로 이동

#######################################(방법04)



