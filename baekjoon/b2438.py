# 문제

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5
# 예제 출력 1 
# *
# **
# ***
# ****
# *****

############################################(방법01)

n = int(input())
# print(n)

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

############################################(방법01)

n = int(input())
# print(n)

for i in range(1, n + 1):
    print('*' * i)

############################################(방법02)

def print_stars(limit, current):        # 재귀함수 사용
    if current > limit:
        return
    
    print('*' * current)
    
    print_stars(limit, current + 1)

n = int(input())
# print(n)
print_stars(n, 1)

############################################(방법03)

N = int(input())
print(N)

for i in range(N):
    for j in range(N):
        if i >= j:
            print("*", end='')
    print()

############################################(방법04)

N = int(input())
for i in range(1, N+1):
    print('*'*i)

############################################(방법05)

n = int(input())

i = 1
while i <= n:
    print("*" * i)
    i += 1

############################################(방법06)

