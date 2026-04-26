def solve_v1():
    try:
        n = int(input())
        paper = [[0] * 101 for _ in range(101)]
        
        # 색종이 붙이기
        for _ in range(n):
            x, y = map(int, input().split())
            for i in range(x, x + 10):
                for j in range(y, y + 10):
                    paper[i][j] = 1
        
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        perimeter = 0
        
        for i in range(1, 101):
            for j in range(1, 101):
                if paper[i][j] == 1:
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]
                        # 주변이 도화지 밖이거나 흰색(0)이면 둘레임
                        if nx < 1 or nx > 100 or ny < 1 or ny > 100 or paper[nx][ny] == 0:
                            perimeter += 1
        print(perimeter)
    except: pass

solve_v1()

#############################################################################################

def solve_v2():
    try:
        n = int(input())
        grid = [[0] * 101 for _ in range(101)]
        for _ in range(n):
            x, y = map(int, input().split())
            for i in range(x, x + 10):
                for j in range(y, y + 10):
                    grid[i][j] = 1
        
        total = 0
        # 모든 칸을 돌며 오른쪽과 아래쪽 칸과의 차이(색이 변하는지)를 확인
        for i in range(101):
            for j in range(101):
                # 가로 경계: 현재 칸과 다음 칸의 상태가 다르면 둘레 1 추가
                if i < 100 and grid[i][j] != grid[i+1][j]:
                    total += 1
                # 세로 경계: 현재 칸과 아래 칸의 상태가 다르면 둘레 1 추가
                if j < 100 and grid[i][j] != grid[i][j+1]:
                    total += 1
                    
        # 도화지 가장자리 경계 처리를 위해 패딩된 영역까지 계산됨
        print(total)
    except: pass

solve_v2()

#############################################################################################

import sys

def solve_v3():
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    
    # 1. 고유한 검은색 칸(1x1)들을 먼저 집합으로 모음
    squares = set()
    for k in range(n):
        x, y = int(data[2*k+1]), int(data[2*k+2])
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                squares.add((i, j))
    
    # 2. 에지 패리티(XOR) 로직 적용
    # 한 번 나타나면 추가, 두 번 나타나면(겹치면) 제거
    edges = set()
    for x, y in squares:
        # 1x1 칸의 4개 변 정의
        current_edges = [
            (x, y, x+1, y), (x, y+1, x+1, y+1), # 가로변
            (x, y, x, y+1), (x+1, y, x+1, y+1)  # 세로변
        ]
        for e in current_edges:
            if e in edges:
                edges.remove(e) # 공유되는 변은 둘레가 아니므로 제거
            else:
                edges.add(e) # 처음 나타나는 변은 일단 둘레 후보
                
    print(len(edges))

solve_v3()

#############################################################################################

def solve_v4():
    try:
        n = int(input())
        # 0으로 감싸진 102x102 공간
        grid = [[0]*102 for _ in range(102)]
        for _ in range(n):
            x, y = map(int, input().split())
            for i in range(x+1, x+11): # 패딩 때문에 1씩 밀림
                for j in range(y+1, y+11):
                    grid[i][j] = 1
                    
        ans = 0
        for i in range(1, 101):
            for j in range(1, 101):
                if grid[i][j]:
                    # 네 방향 중 0인 곳의 개수만큼 둘레 추가
                    ans += 4 - (grid[i-1][j] + grid[i+1][j] + grid[i][j-1] + grid[i][j+1])
        print(ans)
    except: pass

solve_v4()

#############################################################################################

def solve_v5():
    try:
        n = int(input())
        grid = [[0]*102 for _ in range(102)]
        for _ in range(n):
            x, y = map(int, input().split())
            for i in range(x+1, x+11):
                for j in range(y+1, y+11):
                    grid[i][j] = 1
        
        row_diff = sum(abs(grid[i][j] - grid[i-1][j]) for i in range(1, 102) for j in range(102))
        col_diff = sum(abs(grid[i][j] - grid[i][j-1]) for i in range(102) for j in range(1, 102))
        
        print(row_diff + col_diff)
    except: pass

solve_v5()

#############################################################################################

