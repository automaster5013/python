import sys

def solve():
    # 입력 처리 (2n과 색상 문자열)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m = int(input_data[0]) # 전체 점의 개수 (2n)
    s = input_data[1]      # 색상 정보
    
    # dp[i][j]: i~j 구간의 최소 거리 합
    # height[i][j]: i~j 구간 최적 연결 시의 최대 높이
    # split[i][j]: 경로 복원을 위한 기록 (-1은 페어링, k는 분할 지점)
    dp = [[float('inf')] * m for _ in range(m)]
    height = [[0] * m for _ in range(m)]
    split = [[-2] * m for _ in range(m)]
    
    # 구간 DP: 길이가 짧은 구간부터 계산
    for length in range(2, m + 1, 2):
        for i in range(m - length + 1):
            j = i + length - 1
            
            # 1. 양 끝점 (i, j)를 하나의 쌍으로 연결하는 경우
            if s[i] != s[j]:
                if length == 2:
                    d_inner, h_inner = 0, 0
                else:
                    d_inner, h_inner = dp[i+1][j-1], height[i+1][j-1]
                
                if d_inner != float('inf'):
                    d_total = d_inner + (j - i) + 2 * (h_inner + 1)
                    h_total = h_inner + 1
                    if d_total < dp[i][j]:
                        dp[i][j], height[i][j], split[i][j] = d_total, h_total, -1
                    elif d_total == dp[i][j] and h_total < height[i][j]:
                        height[i][j], split[i][j] = h_total, -1
            
            # 2. 구간을 [i, k]와 [k+1, j] 두 부분으로 나누는 경우
            for k in range(i + 1, j, 2):
                d1, d2 = dp[i][k], dp[k+1][j]
                if d1 != float('inf') and d2 != float('inf'):
                    d_total = d1 + d2
                    h_total = max(height[i][k], height[k+1][j])
                    if d_total < dp[i][j]:
                        dp[i][j], height[i][j], split[i][j] = d_total, h_total, k
                    elif d_total == dp[i][j] and h_total < height[i][j]:
                        height[i][j], split[i][j] = h_total, k
                            
    # 결과 출력
    print(int(dp[0][m-1]))
    
    # 경로 복원
    res_pairs = []
    def reconstruct(i, j):
        if i > j: return
        sp = split[i][j]
        if sp == -1:
            res_pairs.append((i + 1, j + 1))
            reconstruct(i + 1, j - 1)
        else:
            reconstruct(i, sp)
            reconstruct(sp + 1, j)
            
    reconstruct(0, m - 1)
    res_pairs.sort() # 시작 좌표 기준 정렬
    for p in res_pairs:
        print(f"{p[0]} {p[1]}")

if __name__ == "__main__":
    solve()

########################################################################################

