import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    ptr = 2
    for _ in range(M):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].append(v)
        ptr += 2
        
    # 타잔 알고리즘 변수
    dfn = [-1] * (N + 1)
    low = [-1] * (N + 1)
    stack = []
    in_stack = [False] * (N + 1)
    scc_id = [-1] * (N + 1)
    scc_count = 0
    timer = 0
    
    scc_members = [] # 각 SCC에 속한 소들의 수 저장

    def tarjan(u):
        nonlocal timer, scc_count
        dfn[u] = low[u] = timer
        timer += 1
        stack.append(u)
        in_stack[u] = True
        
        for v in adj[u]:
            if dfn[v] == -1:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])
                
        if low[u] == dfn[u]:
            count = 0
            while True:
                node = stack.pop()
                in_stack[node] = False
                scc_id[node] = scc_count
                count += 1
                if node == u:
                    break
            scc_members.append(count)
            scc_count += 1

    # 1. 모든 정점에 대해 SCC 탐색
    for i in range(1, N + 1):
        if dfn[i] == -1:
            tarjan(i)
            
    # 2. 각 SCC의 진출 차수 계산
    out_degree = [0] * scc_count
    for u in range(1, N + 1):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                out_degree[scc_id[u]] += 1
                
    # 3. 진출 차수가 0인 SCC 찾기
    sink_scc = []
    for i in range(scc_count):
        if out_degree[i] == 0:
            sink_scc.append(i)
            
    # 4. 결과 출력
    if len(sink_scc) == 1:
        # 진출 차수가 0인 SCC가 단 하나일 때, 그 안의 소 마릿수 출력
        print(scc_members[sink_scc[0]])
    else:
        # 진출 차수가 0인 곳이 없거나(불가능) 여러 개면 유명한 소는 없음
        print(0)

if __name__ == "__main__":
    solve()

#####################################################################

