import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n, m = map(int, input_data)
    
    # 전체 넓이가 홀수이면 채우기 불가능
    if (n * m) % 2:
        print(0)
        return
        
    # 비트마스크 크기를 최소화하기 위해 작은 값을 n으로 설정
    if n > m:
        n, m = m, n
        
    # dp[col][mask] 초기화
    dp = [[0] * (1 << n) for _ in range(m + 1)]
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(1 << n):
            if dp[i][j] == 0:
                continue
            
            # 현재 열 i에서 다음 열 i+1로 넘어가는 상태 탐색
            def dfs(row, current_mask, next_mask):
                if row == n:
                    # 현재 열을 다 채웠으면 다음 열 상태에 경우의 수 합산
                    dp[i + 1][next_mask] += dp[i][current_mask]
                    return
                
                # 현재 칸이 이전 열에서 넘어온 도미노로 채워져 있는 경우
                if (current_mask >> row) & 1:
                    dfs(row + 1, current_mask, next_mask)
                else:
                    # 1. 가로 도미노 배치 (다음 열로 튀어나감)
                    dfs(row + 1, current_mask, next_mask | (1 << row))
                    
                    # 2. 세로 도미노 배치 (현재 열의 다음 칸과 함께 채움)
                    if row + 1 < n and not ((current_mask >> (row + 1)) & 1):
                        dfs(row + 2, current_mask, next_mask)
            
            dfs(0, j, 0)
            
    # 모든 열을 채우고 다음 열로 튀어나온 도미노가 없는 상태(0)가 정답
    print(dp[m][0])

if __name__ == "__main__":
    solve()

#################################################################################

