# 테스트 케이스 개수 입력
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    
    # 1. N x N 크기의 0으로 채워진 빈 배열 생성
    snail = [[0] * N for _ in range(N)]
    
    # 2. 이동 방향 정의 (우, 하, 좌, 상 순서)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    # 초기 위치 및 방향 설정
    r, c = 0, 0  # 시작 좌표
    dist = 0     # 시작 방향 (0: 우)
    
    # 3. 1부터 N*N까지 숫자 채우기
    for i in range(1, N * N + 1):
        snail[r][c] = i
        
        # 다음 이동할 좌표 계산
        nr = r + dr[dist]
        nc = c + dc[dist]
        
        # 4. 범위를 벗어나거나 이미 숫자가 채워져 있다면 방향 전환
        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            dist = (dist + 1) % 4  # 방향 90도 회전
            nr = r + dr[dist]
            nc = c + dc[dist]
            
        # 좌표 업데이트
        r, c = nr, nc

    # 5. 결과 출력
    print(f"#{t}")
    for row in snail:
        print(*(row))


