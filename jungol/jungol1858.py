import sys

def solve():
    # 데이터 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s1 = input_data[1]
    m = int(input_data[2])
    s2 = input_data[3]

    # DP 테이블 초기화 (n+1 x m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_score = 0
    max_pos = (0, 0)

    # 1. DP 테이블 채우기 (Smith-Waterman)
    for i in range(1, n + 1):
        char1 = s1[i-1]
        dp_prev = dp[i-1]
        dp_curr = dp[i]
        for j in range(1, m + 1):
            # 대각선 (Match/Mismatch)
            match_score = 3 if char1 == s2[j-1] else -2
            score = dp_prev[j-1] + match_score
            
            # 위쪽 (Gap in s1)
            up = dp_prev[j] - 2
            if up > score: score = up
            
            # 왼쪽 (Gap in s2)
            left = dp_curr[j-1] - 2
            if left > score: score = left
            
            # 음수면 0으로 리셋 (Local Alignment의 특징)
            if score < 0: score = 0
            
            dp_curr[j] = score
            
            if score > max_score:
                max_score = score
                max_pos = (i, j)

    # 2. 역추적 (Traceback)하여 부분 서열 범위 찾기
    curr_i, curr_j = max_pos
    min_i, min_j = curr_i, curr_j
    
    while curr_i > 0 and curr_j > 0 and dp[curr_i][curr_j] > 0:
        min_i, min_j = curr_i, curr_j
        
        score = dp[curr_i][curr_j]
        match_val = 3 if s1[curr_i-1] == s2[curr_j-1] else -2
        
        # 어느 방향에서 왔는지 확인하여 이동
        if score == dp[curr_i-1][curr_j-1] + match_val:
            curr_i -= 1
            curr_j -= 1
        elif score == dp[curr_i-1][curr_j] - 2:
            curr_i -= 1
        elif score == dp[curr_i][curr_j-1] - 2:
            curr_j -= 1
        else:
            break

    # 3. 결과 출력
    print(max_score)
    # 인덱스 범위를 이용해 원본 서열에서 추출
    print(s1[min_i-1 : max_pos[0]])
    print(s2[min_j-1 : max_pos[1]])

if __name__ == "__main__":
    solve()

###################################################################3

