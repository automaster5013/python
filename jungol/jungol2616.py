import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 앱의 개수
    m_target = int(input_data[1]) # 필요한 메모리
    
    # 메모리 리스트와 비용 리스트
    memories = list(map(int, input_data[2:2+n]))
    costs = list(map(int, input_data[2+n:2+2*n]))
    
    max_cost = sum(costs)
    
    # 2. DP 테이블 초기화
    # dp[j]: 비용 j로 확보 가능한 최대 메모리
    dp = [0] * (max_cost + 1)
    
    # 3. 배낭 문제 로직 수행 (0/1 Knapsack)
    for i in range(n):
        mem = memories[i]
        cost = costs[i]
        
        # 비용 j를 뒤에서부터 순회하여 중복 방지
        for j in range(max_cost, cost - 1, -1):
            if dp[j - cost] + mem > dp[j]:
                dp[j] = dp[j - cost] + mem
                
    # 4. 목표 메모리 M 이상을 확보하는 최소 비용 찾기
    for j in range(max_cost + 1):
        if dp[j] >= m_target:
            print(j)
            break

if __name__ == "__main__":
    solve()

##################################################################

