# 문제

# 매일 매일 일곱 난쟁이는 광산으로 일을 하러 간다. 난쟁이가 일을 하는 동안 백설공주는 그들을 위해 저녁 식사를 준비한다. 
# 백설공주는 의자 일곱개, 접시 일곱개, 나이프 일곱개를 준비한다.

# 어느 날 광산에서 아홉 난쟁이가 돌아왔다. (왜 그리고 어떻게 아홉 난쟁이가 돌아왔는지는 아무도 모른다) 
# 아홉 난쟁이는 각각 자신이 백설공주의 일곱 난쟁이라고 우기고 있다.

# 백설공주는 이런 일이 생길 것을 대비해서, 난쟁이가 쓰고 다니는 모자에 100보다 작은 양의 정수를 적어 놓았다. 
# 사실 백설 공주는 공주가 되기 전에 매우 유명한 수학자였다. 따라서, 일곱 난쟁이의 모자에 쓰여 있는 숫자의 합이 100이 되도록 적어 놓았다.

# 아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오. 
# (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)

# 입력
# 총 아홉개 줄에 1보다 크거나 같고 99보다 작거나 같은 자연수가 주어진다. 모든 숫자는 서로 다르다. 
# 또, 항상 답이 유일한 경우만 입력으로 주어진다.

# 출력
# 일곱 난쟁이가 쓴 모자에 쓰여 있는 수를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 7
# 8
# 10
# 13
# 15
# 19
# 20
# 23
# 25
# 예제 출력 1 
# 7
# 8
# 10
# 13
# 19
# 20
# 23
# 예제 입력 2 
# 8
# 6
# 5
# 1
# 37
# 30
# 28
# 22
# 36
# 예제 출력 2 
# 8
# 6
# 5
# 1
# 30
# 28
# 22
##################################################################################################

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

