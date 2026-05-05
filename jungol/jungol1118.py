import sys

# 재귀 한도 설정
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    is_obstacle = [[False] * (n + 1) for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        r = int(input_data[idx])
        c = int(input_data[idx+1])
        is_obstacle[r][c] = True
        idx += 2
        
    # 1. ↘ 방향 대각선 조각 번호 매기기
    diag1 = [[0] * (n + 1) for _ in range(n + 1)]
    d1_cnt = 0
    # 대각선 시작점들 (1행의 모든 열, 2~n행의 1열)
    starts1 = [(1, j) for j in range(1, n + 1)] + [(i, 1) for i in range(2, n + 1)]
    
    for r, c in starts1:
        new_segment = True
        while 1 <= r <= n and 1 <= c <= n:
            if is_obstacle[r][c]:
                new_segment = True
            else:
                if new_segment:
                    d1_cnt += 1
                    new_segment = False
                diag1[r][c] = d1_cnt
            r += 1
            c += 1

    # 2. ↙ 방향 대각선 조각 번호 매기기
    diag2 = [[0] * (n + 1) for _ in range(n + 1)]
    d2_cnt = 0
    # 대각선 시작점들 (1행의 모든 열, 2~n행의 n열)
    starts2 = [(1, j) for j in range(1, n + 1)] + [(i, n) for i in range(2, n + 1)]
    
    for r, c in starts2:
        new_segment = True
        while 1 <= r <= n and 1 <= c <= n:
            if is_obstacle[r][c]:
                new_segment = True
            else:
                if new_segment:
                    d2_cnt += 1
                    new_segment = False
                diag2[r][c] = d2_cnt
            r += 1
            c -= 1

    # 3. 이분 그래프 구성 (diag1 조각 -> diag2 조각)
    adj = [[] for _ in range(d1_cnt + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not is_obstacle[i][j]:
                adj[diag1[i][j]].append(diag2[i][j])
                
    # 4. 이분 매칭 수행
    match = [0] * (d2_cnt + 1)
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == 0 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False
    
    ans = 0
    for i in range(1, d1_cnt + 1):
        visited = [False] * (d2_cnt + 1)
        if dfs(i, visited):
            ans += 1
            
    print(ans)

if __name__ == "__main__":
    solve()

#####################################################################


