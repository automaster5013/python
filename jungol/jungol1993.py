import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    # 모판을 하나의 문자열로 합친 뒤 등급별 인덱스 부여
    grid_str = "".join(input_data[1:])
    
    # 등급 매핑 (A=0, B=1, C=2, F=5)
    char_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    grid = [char_map.get(c, 5) for c in grid_str]
    
    # 가격 행렬 정의 (A-F 조합)
    costs = [[0] * 6 for _ in range(6)]
    costs[0][0] = 100 # [A,A]
    costs[0][1] = costs[1][0] = 70  # [A,B]
    costs[0][2] = costs[2][0] = 40  # [A,C]
    costs[1][1] = 50  # [B,B]
    costs[1][2] = costs[2][1] = 30  # [B,C]
    costs[2][2] = 20  # [C,C]
    # F가 포함된 나머지는 모두 0
    
    m_size = 1 << N
    dp = [-1] * m_size
    dp[0] = 0  # 초기 상태: 0번 칸 시작, 덮인 곳 없음
    
    # 칸 하나씩 이동하며 DP 갱신
    for i in range(N * N):
        nxt_dp = [-1] * m_size
        for mask in range(m_size):
            curr_val = dp[mask]
            if curr_val == -1:
                continue
            
            # 1. 현재 칸 i가 이미 덮여 있는 경우 (mask의 0번 비트)
            if mask & 1:
                target = mask >> 1
                if curr_val > nxt_dp[target]:
                    nxt_dp[target] = curr_val
            else:
                # 2. 현재 칸을 버리고 건너뛰기
                target = mask >> 1
                if curr_val > nxt_dp[target]:
                    nxt_dp[target] = curr_val
                
                # 3. 가로로 자르기 (i, i+1)
                if (i % N != N - 1) and not (mask & 2):
                    score = costs[grid[i]][grid[i+1]]
                    target = (mask >> 1) | 1 # i+1 칸을 덮음 처리
                    if curr_val + score > nxt_dp[target]:
                        nxt_dp[target] = curr_val + score
                
                # 4. 세로로 자르기 (i, i+N)
                if i + N < N * N:
                    score = costs[grid[i]][grid[i+N]]
                    target = (mask >> 1) | (1 << (N - 1)) # i+N 칸을 덮음 처리
                    if curr_val + score > nxt_dp[target]:
                        nxt_dp[target] = curr_val + score
        dp = nxt_dp
        
    # 모든 칸을 순회한 후의 결과값 출력
    print(dp[0])

if __name__ == "__main__":
    solve()

##################################################################################

