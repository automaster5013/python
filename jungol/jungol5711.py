import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m, a, b = map(int, input_data[:4])
    ptr = 4
    
    # 조약돌 위치 입력 및 정렬
    stones = []
    for _ in range(a):
        stones.append((int(input_data[ptr]), int(input_data[ptr+1])))
        ptr += 2
    stones.sort()
    
    # 장애물 위치 입력
    obstacles = set()
    for _ in range(b):
        obstacles.add((int(input_data[ptr]), int(input_data[ptr+1])))
        ptr += 2
        
    # 경로 포인트: 시작점 + 조약돌들 + 도착점
    path_points = [(1, 1)] + stones + [(n, m)]
    
    # 유효성 검사: 조약돌을 순서대로 방문할 수 있는지 확인
    for i in range(len(path_points) - 1):
        r1, c1 = path_points[i]
        r2, c2 = path_points[i+1]
        if r1 > r2 or c1 > c2:
            print(0)
            return

    # 두 지점 사이의 경우의 수를 구하는 DP 함수
    def count_paths(start, end):
        r1, c1 = start
        r2, c2 = end
        
        # 시작점이나 끝점이 장애물인 경우
        if (r1, c1) in obstacles or (r2, c2) in obstacles:
            return 0
            
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0: continue
                
                # 실제 좌표 계산
                curr_r, curr_c = r1 + i, c1 + j
                
                if (curr_r, curr_c) in obstacles:
                    dp[i][j] = 0
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left
                    
        return dp[rows-1][cols-1]

    # 각 구간의 경우의 수를 곱함
    total_ans = 1
    for i in range(len(path_points) - 1):
        total_ans *= count_paths(path_points[i], path_points[i+1])
        
    print(total_ans)

if __name__ == "__main__":
    solve()

#########################################################################


