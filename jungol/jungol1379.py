import sys

# 재귀 깊이 제한 해제 (N이 30만 이므로 넉넉하게 설정)
sys.setrecursionlimit(500000)

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    m = int(input[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input[ptr])
        v = int(input[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    dfn = [0] * (n + 1) # 방문 순서
    low = [0] * (n + 1) # 해당 노드에서 도달 가능한 가장 높은 조상의 dfn
    is_cut = [False] * (n + 1) # 절점 여부
    timer = 0

    def find_cut_vertex(u, is_root):
        nonlocal timer
        timer += 1
        dfn[u] = low[u] = timer
        child_count = 0
        
        for v in adj[u]:
            if dfn[v] == 0: # 방문하지 않은 자식 노드
                child_count += 1
                find_cut_vertex(v, False)
                low[u] = min(low[u], low[v])
                
                # 루트가 아니고, 자식이 u의 조상으로 갈 수 없는 경우
                if not is_root and low[v] >= dfn[u]:
                    is_cut[u] = True
            else:
                # 이미 방문한 노드 (역방향 에지)
                low[u] = min(low[u], dfn[v])
        
        # 루트인 경우 자식이 2개 이상이면 절점
        if is_root and child_count >= 2:
            is_cut[u] = True

    # 그래프가 모두 연결되어 있으므로 1번 노드부터 시작
    find_cut_vertex(1, True)
    
    # 절점 번호를 오름차순으로 정리
    result = [i for i in range(1, n + 1) if is_cut[i]]
    
    if not result:
        print("-1")
    else:
        print(*(result))

if __name__ == "__main__":
    solve()

#######################################################################


