# 문제

# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 예제 입력 1 
# 5
# 예제 출력 1 
# *****
#  ****
#   ***
#    **
#     *

###########################################################(방법01)

N = int(input())
# print(N)
i = 0
while i < N:
    j = 0
    while j < i:
        print(" ", end="")
        j += 1
    k = 0
    while k < N - i:
        print("*", end="")
        k += 1

    print()
    i += 1

###########################################################(방법01)

N = int(input())
# print(n)
for i in range(N):
    print(' ' * i + '*' * (N - i))

###########################################################(방법02)

N = int(input())
# print(N)
for i in range(N):
    for j in range(i):
        print(" ", end="")
        
    for j in range(N - i):
        print("*", end="")
        
    print()

###########################################################(방법03)

def print_stars(total, current):
    # 기저 조건: 현재 줄 번호가 전체 줄 수와 같아지면 종료
    if current == total:
        return
    
    # 현재 줄 출력: 공백(current) + 별(total - current)
    print(' ' * current + '*' * (total - current))
    
    # 다음 줄을 위해 자기 자신 호출 (current를 1 증가)
    print_stars(total, current + 1)

# 실행부
n_val = int(input())
# 0번 줄부터 시작하도록 호출
print_stars(n_val, 0)

###########################################################(방법04)

N = int(input())
# print(N)
for x in range(N):
    # ? for문
    for y in range(x):
        print(" ", end="")
    # * for문
    for z in range(N-x, 0, -1):
        print("*", end="")
    print()

###########################################################(방법05)

n = int(input())
for i in range(n,0,-1):
    print(f"{'*'*i:>{n}}")

###########################################################(방법06)

