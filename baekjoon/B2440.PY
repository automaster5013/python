# 문제

# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5
# 예제 출력 1 
# *****
# ****
# ***
# **
# *

#######################################################(방법01)

N = int(input())
# print(N)
for i in range(N, 0, -1):
    print('*' * i)

#######################################################(방법01)

N = int(input())
# print(N)
for i in range(N):
    for j in range(N - i):
        print("*", end="")
    
    print()

#######################################################(방법02)

def print_stars(count):
    if count <= 0:
        return
    
    print('*' * count)
    
    print_stars(count - 1)

N_val = int(input())
# print(N_val)
print_stars(N_val)

#######################################################(방법03)

N = int(input())
# print(N)
print("\n".join("*" * i for i in range(N, 0, -1)))

#######################################################(방법04)

N = int(input())
# print(N)
stars = "*" * N

for i in range(N):
    print(stars[:N - i])

#######################################################(방법05)

N = int(input())
# print(N)
def print_stars(n):
    if n > 0:
        print("*" * n)
        print_stars(n - 1)

print_stars(N)

#######################################################(방법06)

N = int(input())
# print(N)

for x in range(N):
    for y in range(0, N - x):
        print("*", end="")
    print()

#######################################################(방법07)

n = int(input())
for i in range(n,0,-1):
    print('*'*i)

#######################################################(방법08)

