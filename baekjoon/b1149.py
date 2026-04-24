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

