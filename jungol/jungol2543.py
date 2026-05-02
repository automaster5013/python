import sys

# 재귀 깊이 설정 (N=512일 때 최대 깊이는 9로 충분함)
sys.setrecursionlimit(10000)

def solve():
    # 모든 입력을 한 번에 읽어와 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    hr = int(input_data[1])  # 배수구 행 위치 (X)
    hc = int(input_data[2])  # 배수구 열 위치 (Y)
    
    # 바닥 초기화 (0은 구멍 또는 아직 채워지지 않은 상태)
    grid = [[0] * n for _ in range(n)]
    
    def fill(sz, r, c, hr, hc):
        # 기저 사례: 크기가 1이면 더 이상 채울 수 없음
        if sz == 1:
            return
        
        half = sz // 2
        # 현재 영역의 중심 경계선 좌표
        mid_r, mid_c = r + half, c + half
        
        # 구멍이 위치한 사분면 파악
        # 1: 왼쪽 위, 2: 오른쪽 위, 3: 왼쪽 아래, 4: 오른쪽 아래
        if hr < mid_r and hc < mid_c:
            hole_type = 1
        elif hr < mid_r and hc >= mid_c:
            hole_type = 2
        elif hr >= mid_r and hc < mid_c:
            hole_type = 3
        else:
            hole_type = 4
            
        # 구멍이 없는 3개의 사분면의 중심을 하나의 L-트리미노로 채움
        # 각 타일 번호는 예제의 규칙을 따름
        if hole_type != 1: grid[mid_r - 1][mid_c - 1] = hole_type
        if hole_type != 2: grid[mid_r - 1][mid_c] = hole_type
        if hole_type != 3: grid[mid_r][mid_c - 1] = hole_type
        if hole_type != 4: grid[mid_r][mid_c] = hole_type
        
        # 4개의 사분면에 대해 재귀적으로 수행
        # 구멍이 없었던 사분면은 중심부에 방금 채운 타일 위치가 새로운 구멍이 됨
        
        # 왼쪽 위 (Top-Left)
        fill(half, r, c, hr if hole_type == 1 else mid_r - 1, hc if hole_type == 1 else mid_c - 1)
        # 오른쪽 위 (Top-Right)
        fill(half, r, mid_c, hr if hole_type == 2 else mid_r - 1, hc if hole_type == 2 else mid_c)
        # 왼쪽 아래 (Bottom-Left)
        fill(half, mid_r, c, hr if hole_type == 3 else mid_r, hc if hole_type == 3 else mid_c - 1)
        # 오른쪽 아래 (Bottom-Right)
        fill(half, mid_r, mid_c, hr if hole_type == 4 else mid_r, hc if hole_type == 4 else mid_c)

    # 타일 채우기 시작
    fill(n, 0, 0, hr, hc)
    
    # 출력 형식에 맞춰 출력 (각 줄의 숫자를 공백으로 구분)
    for row in grid:
        print(*(row))

if __name__ == "__main__":
    solve()

####################################################################################################

