import sys

# 재귀 한도 늘리기
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    R = int(input_data[0])
    C = int(input_data[1])
    grid = input_data[2:]
    
    # 1. 가로 판자 번호 매기기
    row_map = [[0] * C for _ in range(R)]
    row_cnt = 0
    for i in range(R):
        in_mud = False
        for j in range(C):
            if grid[i][j] == '*':
                if not in_mud:
                    row_cnt += 1
                    in_mud = True
                row_map[i][j] = row_cnt
            else:
                in_mud = False
                
    # 2. 세로 판자 번호 매기기
    col_map = [[0] * C for _ in range(R)]
    col_cnt = 0
    for j in range(C):
        in_mud = False
        for i in range(R):
            if grid[i][j] == '*':
                if not in_mud:
                    col_cnt += 1
                    in_mud = True
                col_map[i][j] = col_cnt
            else:
                in_mud = False
                
    # 3. 이분 그래프 인접 리스트 생성
    adj = [[] for _ in range(row_cnt + 1)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '*':
                adj[row_map[i][j]].append(col_map[i][j])
                
    # 4. 이분 매칭 (DFS)
    match = [0] * (col_cnt + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == 0 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False
    
    ans = 0
    for i in range(1, row_cnt + 1):
        visited = [False] * (col_cnt + 1)
        if dfs(i, visited):
            ans += 1
            
    print(ans)

if __name__ == "__main__":
    solve()

####################################################################

