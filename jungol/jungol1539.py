import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    bricks = []
    
    idx = 1
    for i in range(1, n + 1):
        area = int(input_data[idx])
        height = int(input_data[idx+1])
        weight = int(input_data[idx+2])
        # (ID, 넓이, 높이, 무게) 형태로 저장
        bricks.append((i, area, height, weight))
        idx += 3
        
    # 2. 밑면 넓이 기준 내림차순 정렬 (넓은 게 아래로 가야 하므로)
    bricks.sort(key=lambda x: x[1], reverse=True)
    
    # 3. DP 배열 및 경로 추적 배열 초기화
    # dp[i] : i번째 벽돌을 가장 위에 두었을 때 얻을 수 있는 최대 높이
    dp = [0] * n
    parent = [-1] * n
    
    for i in range(n):
        dp[i] = bricks[i][2] # 초기값은 현재 벽돌의 높이
        for j in range(i):
            # 정렬 덕분에 넓이는 이미 bricks[j]가 더 넓음
            # 무게 조건만 확인: 아래 벽돌(j)이 위 벽돌(i)보다 무거워야 함
            if bricks[j][3] > bricks[i][3]:
                if dp[j] + bricks[i][2] > dp[i]:
                    dp[i] = dp[j] + bricks[i][2]
                    parent[i] = j
                    
    # 4. 최대 높이를 가지는 마지막 벽돌 인덱스 찾기
    max_height = 0
    max_idx = -1
    for i in range(n):
        if dp[i] > max_height:
            max_height = dp[i]
            max_idx = i
            
    # 5. 경로 역추적 (가장 위 벽돌부터 아래로)
    path = []
    curr = max_idx
    while curr != -1:
        path.append(bricks[curr][0])
        curr = parent[curr]
        
    # 6. 결과 출력
    print(len(path))
    for brick_id in path:
        print(brick_id)

if __name__ == "__main__":
    solve()

#########################################################################

