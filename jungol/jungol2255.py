# 방법 1: 반복문 기반 사이클 탐색 + 수동 LCM 연산
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    if a == 0 or b == 0: return 0
    return (a * b) // get_gcd(a, b)

# 입력 처리
n = int(input())
shuffle = list(map(int, input().split()))
# 1-indexed를 0-indexed로 보정
p = [x - 1 for x in shuffle]

visited = [False] * n
total_lcm = 1

for i in range(n):
    if not visited[i]:
        # 새로운 사이클 발견 및 길이 측정
        curr = i
        count = 0
        while not visited[curr]:
            visited[curr] = True
            curr = p[curr]
            count += 1
        
        # 전체 궤적(LCM) 갱신
        total_lcm = get_lcm(total_lcm, count)

print(total_lcm)

###########################################################

import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 섞기 수열 (1-indexed를 0-indexed로 보정)
    p = [int(x) - 1 for x in input_data[1:]]
    
    visited = [False] * n
    ans = 1
    
    for i in range(n):
        if not visited[i]:
            # 새로운 사이클 발견
            curr = i
            count = 0
            while not visited[curr]:
                visited[curr] = True
                curr = p[curr] # 다음 위치로 이동
                count += 1
            
            # 현재까지의 최소공배수와 새로운 사이클 길이의 LCM 계산
            # Python 3.9+ 라면 math.lcm(ans, count) 사용 가능
            ans = lcm(ans, count)
            
    print(ans)

if __name__ == "__main__":
    solve()

###########################################################

# 방법 3: 소인수 분해 지수 맵 방식 (Prime Power Mapping)
n = int(input())
p = [int(x) - 1 for x in input().split()]

visited = [False] * n
prime_max_counts = {} # 각 소수별 최대 등장 횟수 저장

for i in range(n):
    if not visited[i]:
        curr, count = i, 0
        while not visited[curr]:
            visited[curr] = True
            curr = p[curr]
            count += 1
        
        # 사이클 길이(count)를 소인수 분해
        temp_n = count
        d = 2
        while d * d <= temp_n:
            if temp_n % d == 0:
                p_cnt = 0
                while temp_n % d == 0:
                    p_cnt += 1
                    temp_n //= d
                # 해당 소수의 지수 중 최댓값만 유지
                if d not in prime_max_counts or p_cnt > prime_max_counts[d]:
                    prime_max_counts[d] = p_cnt
            d += 1
        if temp_n > 1:
            if temp_n not in prime_max_counts or 1 > prime_max_counts[temp_n]:
                prime_max_counts[temp_n] = 1

# 수집된 소수 지수들을 모두 곱함
final_ans = 1
for prime, exponent in prime_max_counts.items():
    final_ans *= (prime ** exponent)

print(final_ans)

###########################################################

# 방법 2: 음수 변환 마킹 (추가 공간 0)
def get_gcd(a, b):
    while b: a, b = b, a % b
    return a

n = int(input())
p = [int(x) for x in input().split()] # 1-indexed 그대로 사용

ans = 1
for i in range(n):
    if p[i] > 0: # 양수라면 아직 방문하지 않음
        curr_idx = i + 1
        count = 0
        while p[curr_idx - 1] > 0:
            next_idx = p[curr_idx - 1]
            p[curr_idx - 1] = -next_idx # 음수로 바꿔서 방문 표시
            curr_idx = next_idx
            count += 1
        
        # LCM 연산 ( (a*b)//gcd )
        ans = (ans * count) // get_gcd(ans, count)

print(ans)

###########################################################

