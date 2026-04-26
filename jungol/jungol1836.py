import sys

def solve_v1():
    # N이 크므로 빠른 입력을 사용합니다.
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    arr = list(map(int, input[1:]))
    
    max_so_far = 0  # 전체 최댓값
    current_max = 0 # 현재 위치까지의 최댓값
    
    for x in arr:
        # 현재 숫자를 더했을 때 0보다 작아지면, 
        # 거기서부터는 새로 시작하는 게(0) 이득입니다.
        current_max = max(0, current_max + x)
        # 지금까지 발견한 가장 큰 값을 갱신합니다.
        max_so_far = max(max_so_far, current_max)
        
    print(max_so_far)

solve_v1()

##############################################################

def solve_v2():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # dp[i]는 i번째 원소를 마지막으로 포함하는 부분합 중 최댓값
    dp = [0] * n
    dp[0] = max(0, arr[0])
    
    for i in range(1, n):
        # (이전까지의 최적합 + 현재값) vs (그냥 현재값) 중 큰 것 선택
        # 문제 조건에 따라 0보다 작으면 0을 선택
        dp[i] = max(0, dp[i-1] + arr[i], arr[i])
        
    print(max(max(dp), 0))

solve_v2()

##############################################################

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr = data[1:]
    
    prefix_sum = 0
    min_prefix = 0 # 지금까지 나온 누적합 중 가장 작은 값
    max_sub = 0
    
    for x in arr:
        prefix_sum += x
        # 현재 누적합에서 과거의 최솟값을 뺀 것이 현재 구간의 최대합 후보
        max_sub = max(max_sub, prefix_sum - min_prefix)
        # 다음에 빼줄 최솟값을 갱신
        min_prefix = min(min_prefix, prefix_sum)
        
    print(max_sub)

solve_v3()

##############################################################

from itertools import accumulate

def solve_v4():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    arr = data[1:]
    
    # 누적하면서 만약 값이 음수가 되면 0으로 리셋하는 제너레이터
    def kadane_gen(nums):
        cur = 0
        for x in nums:
            cur = max(0, cur + x)
            yield cur
            
    print(max(kadane_gen(arr), default=0))

solve_v4()

##############################################################

def get_cross_max(arr, low, mid, high):
    # 중간 지점(mid)을 포함하는 최대 구간합 계산
    left_sum = 0
    cur = 0
    for i in range(mid, low - 1, -1):
        cur += arr[i]
        left_sum = max(left_sum, cur)
        
    right_sum = 0
    cur = 0
    for i in range(mid + 1, high + 1):
        cur += arr[i]
        right_sum = max(right_sum, cur)
        
    return left_sum + right_sum

def dac_max_sum(arr, low, high):
    if low == high:
        return max(0, arr[low])
        
    mid = (low + high) // 2
    
    # 1. 왼쪽 절반의 최대 2. 오른쪽 절반의 최대 3. 중간을 걸친 최대
    return max(dac_max_sum(arr, low, mid),
               dac_max_sum(arr, mid + 1, high),
               get_cross_max(arr, low, mid, high))

def solve_v5():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    if data[0] == 0:
        print(0); return
    print(dac_max_sum(data[1:], 0, data[0]-1))

solve_v5()

##############################################################

