# set()은 중복을 허용하지 않고 순서가 없는 집합 자료형!!
remainders = set()

for x in range(10):
    num = int(input())
    remainders.add(num % 42)

print(len(remainders))

##############################################################(방법01)

unique_lst = []

for x in range(10):
    rem = int(input()) % 42
    if rem not in unique_lst:
        unique_lst.append(rem)

print(len(unique_lst))

##############################################################(방법02)

lockers = [False] * 42

for x in range(10):
    rem = int(input()) % 42
    lockers[rem] = True

count = 0
for used in lockers:
    if used:
        count += 1

print(count)

##############################################################(방법03)

all_rems = []
for x in range(10):
    all_rems.append(int(input()) % 42)

all_rems.sort()

count = 1
for i in range(1, 10):
    if all_rems[i] != all_rems[i-1]:
        count += 1

print(count)

##############################################################(방법04)

bit_status = 0

for x in range(10):
    rem = int(input()) % 42
    bit_status |= (1 << rem)

unique_count = 0
while bit_status > 0:
    unique_count += (bit_status & 1)
    bit_status >>= 1

print(unique_count)

##############################################################(방법05)

