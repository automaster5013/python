import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k_colors = int(input_data[1])
    bulbs = list(map(int, input_data[2:]))
    
    if n == 0:
        print(0)
        return

    # 1. 인접한 같은 색 전구 압축
    compressed = []
    if n > 0:
        compressed.append(bulbs[0])
        for i in range(1, n):
            if bulbs[i] != bulbs[i-1]:
                compressed.append(bulbs[i])
    
    m = len(compressed)
    # 2. DP 테이블 초기화 (S[i][j]는 절약 가능한 횟수)
    dp = [[0] * m for _ in range(m)]
    
    # 3. 구간 DP 수행 (구간의 길이를 늘려가며 계산)
    for length in range(2, m + 1): # 구간 길이
        for i in range(m - length + 1):
            j = i + length - 1
            
            # 기본값: i를 제외한 나머지 구간의 절약 횟수
            dp[i][j] = dp[i+1][j]
            
            # i와 색이 같은 k를 찾아 절약 횟수 갱신
            for k in range(i + 1, j + 1):
                if compressed[i] == compressed[k]:
                    # i+1부터 k-1까지의 절약 + k부터 j까지의 절약 + 현재 매칭으로 얻는 절약(1)
                    cost = dp[i+1][k-1] + 1 + dp[k][j]
                    if cost > dp[i][j]:
                        dp[i][j] = cost
                        
    # 최종 결과: (블록 개수 - 1) - 최대 절약 횟수
    print((m - 1) - dp[0][m-1])

if __name__ == "__main__":
    solve()

##############################################################################################

