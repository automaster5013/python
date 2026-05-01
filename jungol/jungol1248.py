import sys

# DFS를 이용한 이분 매칭 구현
def dfs(u, adj, visited, match):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            # 해당 열이 매칭되지 않았거나, 매칭된 행이 다른 열로 이동 가능하다면
            if match[v] < 0 or dfs(match[v], adj, visited, match):
                match[v] = u
                return True
    return False

def solve():
    # 고속 입력을 위해 전체 데이터를 읽어옴
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    ptr = 1
    
    results = []
    for _ in range(T):
        N = int(input_data[ptr])
        ptr += 1
        
        # 격자 정보 읽기
        grid = []
        for _ in range(N):
            grid.append(input_data[ptr])
            ptr += 1
            
        # 1. 인접 리스트 생성 (행 i에서 흰색 칸이 있는 열 j로 연결)
        adj = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 'W':
                    adj[i].append(j)
        
        # 2. 이분 매칭 수행
        match = [-1] * N
        count = 0
        for i in range(N):
            visited = [False] * N
            if dfs(i, adj, visited, match):
                count += 1
        
        # 3. 최대 매칭 수가 N이면 YES, 아니면 NO
        if count == N:
            results.append("YES")
        else:
            results.append("NO")
            
    # 최종 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

######################################################################

