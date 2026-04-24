# 문제

# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

# 예제 입력 1 
# 3
# 26 40 83
# 49 60 57
# 13 89 99
# 예제 출력 1 
# 96
# 예제 입력 2 
# 3
# 1 100 100
# 100 1 100
# 100 100 1
# 예제 출력 2 
# 3
# 예제 입력 3 
# 3
# 1 100 100
# 100 100 100
# 1 100 100
# 예제 출력 3 
# 102
# 예제 입력 4 
# 6
# 30 19 5
# 64 77 64
# 15 19 97
# 4 71 57
# 90 86 84
# 93 32 91
# 예제 출력 4 
# 208
# 예제 입력 5 
# 8
# 71 39 44
# 32 83 55
# 51 37 63
# 89 29 100
# 83 58 11
# 65 13 15
# 47 25 29
# 60 66 19
# 예제 출력 5 
# 253

############################################################################################(방법01)

# n번째 집을 특정 색으로 칠할 때의 최소 비용은, 
# n-1번째 집을 다른 두 색으로 칠했을 때의 최소 누적합 중 작은 값을 더하는 것.
n = int(input())

r, g, b = map(int, input().split())

for _ in range(n - 1):
    nr, ng, nb = map(int, input().split())
    
    r, g, b = nr + min(g, b), ng + min(r, b), nb + min(r, g)

print(min(r, g, b))
# 마지막 집까지 모두 칠했을 때, 
# 최종적으로 저장된 r, g, b 중에서 가장 작은 값이 전체 거리의 최소 비용.

############################################################################################(방법01)

n = int(input())

lst = []
for x in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1, n):
    lst[i][0] += lst[i-1][1] if lst[i-1][1] < lst[i-1][2] else lst[i-1][2]
    
    lst[i][1] += lst[i-1][0] if lst[i-1][0] < lst[i-1][2] else lst[i-1][2]
    
    lst[i][2] += lst[i-1][0] if lst[i-1][0] < lst[i-1][1] else lst[i-1][1]

res = lst[n-1][0]
for val in lst[n-1]:
    if val < res:
        res = val

print(res)

############################################################################################(방법02)

n = int(input())

prev_r, prev_g, prev_b = map(int, input().split())

for x in range(n - 1):
    curr_r, curr_g, curr_b = map(int, input().split())
    
    next_r = curr_r + (prev_g if prev_g < prev_b else prev_b)
    next_g = curr_g + (prev_r if prev_r < prev_b else prev_b)
    next_b = curr_b + (prev_r if prev_r < prev_g else prev_g)
    
    prev_r, prev_g, prev_b = next_r, next_g, next_b

result = prev_r
if prev_g < result: result = prev_g
if prev_b < result: result = prev_b

print(result)

############################################################################################(방법03)

# 입력 개수 받기
n = int(input())

# 첫 번째 집의 비용을 초기값으로 설정
r_sum, g_sum, b_sum = map(int, input().split())

# 두 번째 집부터 n번째 집까지 반복
for _ in range(n - 1):
    # 현재 집의 비용 받기
    r, g, b = map(int, input().split())
    
    # [핵심] 이전까지의 최소합을 이용해 현재 합을 동시에 갱신
    # r_sum은 현재 집을 빨강으로 칠할 때의 최소 누적합
    r_sum, g_sum, b_sum = (
        r + (g_sum if g_sum < b_sum else b_sum),
        g + (r_sum if r_sum < b_sum else b_sum),
        b + (r_sum if r_sum < g_sum else g_sum)
    )

# 세 값 중 가장 작은 값 찾기 (min 함수도 배제한다면 아래와 같이)
res = r_sum
if g_sum < res: res = g_sum
if b_sum < res: res = b_sum

print(res)

############################################################################################(방법04)

n = int(input())
# 누적 비용을 담을 리스트
dp = [0, 0, 0]

for _ in range(n):
    cost = list(map(int, input().split()))
    
    # 각 색상을 선택했을 때의 새로운 누적합 계산
    # sorted()[:1][0]은 리스트에서 가장 작은 값을 가져오는 트릭입니다.
    dp = [
        cost[0] + sorted([dp[1], dp[2]])[0],
        cost[1] + sorted([dp[0], dp[2]])[0],
        cost[2] + sorted([dp[0], dp[1]])[0]
    ]

print(sorted(dp)[0])

############################################################################################(방법05)

import sys
# 재귀 깊이 제한만 수동으로 조절 (기본 라이브러리 없이 설정은 불가하므로 반복문 권장하지만 구조만 참조)
# 여기서는 반복문을 이용한 사전식 누적 방식을 보여줍니다.

n = int(input())
memo = {-1: [0, 0, 0]} # -1번 집(가상)의 누적 비용은 모두 0

for i in range(n):
    r, g, b = map(int, input().split())
    prev = memo[i-1]
    
    # i번째 집의 최소 비용을 사전에 기록
    memo[i] = [
        r + (prev[1] if prev[1] < prev[2] else prev[2]),
        g + (prev[0] if prev[0] < prev[2] else prev[2]),
        b + (prev[0] if prev[0] < prev[1] else prev[1])
    ]

print(sorted(memo[n-1])[0])

############################################################################################(방법06)

n = int(input())
# 초기 상태
total_costs = [0, 0, 0]

for _ in range(n):
    current_house = list(map(int, input().split()))
    
    # 이전 단계에서 현재 색상을 제외한 나머지 중 최소값을 더함
    # i는 현재 색상의 인덱스, c는 그 색상의 비용
    total_costs = [
        c + min(total_costs[:i] + total_costs[i+1:])
        for i, c in enumerate(current_house)
    ]

print(min(total_costs))

############################################################################################(방법07)

n = int(input())
# print(n)
r, g, b = map(int, input().split())

for x in range(n - 1):
    nr, ng, nb = map(int, input().split())
    
    r, g, b = nr + min(g, b), ng + min(r, b), nb + min(r, g)

print(min(r, g, b))

##############################################################################

n = int(input())
# print(n)
lst = []
for x in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1, n):
    lst[i][0] += lst[i-1][1] if lst[i-1][1] < lst[i-1][2] else lst[i-1][2]
    
    lst[i][1] += lst[i-1][0] if lst[i-1][0] < lst[i-1][2] else lst[i-1][2]
    
    lst[i][2] += lst[i-1][0] if lst[i-1][0] < lst[i-1][1] else lst[i-1][1]

res = lst[n-1][0]
for val in lst[n-1]:
    if val < res:
        res = val

print(res)

##############################################################################

import sys
N = int(sys.stdin.readline().strip())
R = G = B = 0

for t in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    if t == 0:
        R, G, B = r, g, b
    else:
        n_R = r + min(G, B)
        n_G = g + min(R, B)
        n_B = b + min(R, G)
        R, G, B = n_R, n_G, n_B

print(min(R, G, B))

##############################################################################

