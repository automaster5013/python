# 아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오. 
# (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오.) : 무차별 대입(부루트포스)
##################################################################################################

BruteForce = []
for _ in range(9):
    BruteForce.append(int(input()))

total_sum = sum(BruteForce)
fake_sum = total_sum - 100

fake_a, fake_b = -1, -1

for i in range(9):
    for j in range(i + 1, 9):
        if BruteForce[i] + BruteForce[j] == fake_sum:
            fake_a = BruteForce[i]
            fake_b = BruteForce[j]
            break
    if fake_a != -1:
        break

for d in BruteForce:
    if d == fake_a or d == fake_b:
        continue
    print(d)

##################################################################################################(방법01)

# for i in range(1, 10):
#     for j in range(1, 10):
#         # for k in range(1, 10):
#             # print(i, j, k)
#             print(i, j)

lst = []
for x in range(9):
    lst.append(int(input()))

# for i in lst:
#     print(i, end=' ')

# print('\nsum :', sum(lst))

nsum = sum(lst)
reali = 0
realj = 0

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        nsum -= (int(lst[i]) + int(lst[j]))
        # print(lst[i], lst[j], nsum)
        if nsum ==100:
            reali = i
            realj = j
            break
        nsum += (int(lst[i]) + int(lst[j]))

# print(reali, realj)

for i in range(len(lst)):
    if i == reali or i == realj:
        continue
    print(lst[i])

##################################################################################################(방법02)

import random

M = []
for t in range(9):
    M.append(int(input()))
R = random.sample(M, 7) 

while sum(R) != 100:
    R = random.sample(M, 7)
    if sum(R)==100 :
        for T in R:
            print(T)

##################################################################################################(방법03)

