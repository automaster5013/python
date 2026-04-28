import sys

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m = int(input_data[0]), int(input_data[1])
    grid = []
    ptr = 2
    for _ in range(n):
        grid.append(list(map(int, input_data[ptr:ptr+m])))
        ptr += m

    # 1. DP 테이블 초기화 (-1은 도달 불가능을 의미)
    dp = [[-1] * m for _ in range(n)]

    # 2. 출발지 예외 처리
    if grid[0][0] == 1:
        print(0)
        return
    
    # 출발지 황금 체크
    dp[0][0] = 1 if grid[0][0] == 2 else 0

    # 3. DP 수행
    for i in range(n):
        for j in range(m):
            # 출발지는 이미 계산했으므로 건너뜀
            if i == 0 and j == 0:
                continue
            
            # 바위인 경우 도달 불가능(-1) 유지
            if grid[i][j] == 1:
                continue
            
            # 위쪽과 왼쪽에서 오는 값 확인
            from_top = dp[i-1][j] if i > 0 else -1
            from_left = dp[i][j-1] if j > 0 else -1
            
            # 둘 중 하나라도 도달 가능한 경로가 있다면
            max_prev = max(from_top, from_left)
            if max_prev != -1:
                # 현재 칸이 황금(2)이면 1을 더하고, 아니면 0을 더함
                gold = 1 if grid[i][j] == 2 else 0
                dp[i][j] = max_prev + gold

    # 4. 결과 출력
    # 도착지가 도달 불가능(-1)이면 0 출력, 아니면 최대값 출력
    result = dp[n-1][m-1]
    print(result if result != -1 else 0)

if __name__ == "__main__":
    solve()

########################################################################
