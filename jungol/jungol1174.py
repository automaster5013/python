import sys

# 이분 매칭을 위한 DFS 함수
def dfs(u, visited, adj, match):
    for v in adj[u]:
        if visited[v]:
            continue
        visited[v] = True
        # 피식자 v가 아직 매칭되지 않았거나, 매칭된 포식자가 다른 피식자를 찾을 수 있다면
        if match[v] == -1 or dfs(match[v], visited, adj, match):
            match[v] = u
            return True
    return False

def solve():
    # 고속 입력을 통해 데이터 로드
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    sharks = []
    ptr = 1
    for _ in range(n):
        sharks.append(list(map(int, input_data[ptr:ptr+3])))
        ptr += 3
        
    # 포식 관계 인접 리스트 생성
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            # 상어 i가 상어 j를 잡아먹을 수 있는지 체크
            if (sharks[i][0] >= sharks[j][0] and 
                sharks[i][1] >= sharks[j][1] and 
                sharks[i][2] >= sharks[j][2]):
                
                # 모든 능력치가 같다면 인덱스가 작은 쪽이 큰 쪽을 먹도록 고정 (무한 루프 방지)
                if (sharks[i][0] == sharks[j][0] and 
                    sharks[i][1] == sharks[j][1] and 
                    sharks[i][2] == sharks[j][2]):
                    if i > j:
                        continue
                
                adj[i].append(j)
                
    # match[i]: i번 상어를 잡아먹은 포식자의 번호
    match = [-1] * n
    total_eaten = 0
    
    # 각 상어는 최대 2마리까지 잡아먹을 수 있음
    for i in range(n):
        for _ in range(2):
            visited = [False] * n
            if dfs(i, visited, adj, match):
                total_eaten += 1
                
    # 살아남은 상어 = 전체 - 잡아먹힌 상어
    print(n - total_eaten)

if __name__ == "__main__":
    solve()

############################################################################################

