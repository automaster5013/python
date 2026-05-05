import sys

# 재귀 깊이 제한 확장 (도시 개수 N이 최대 1,000이므로 넉넉하게 설정)
sys.setrecursionlimit(100000)

def solve():
    # 모든 입력을 한꺼번에 읽어와 처리 속도 최적화
    raw_input = sys.stdin.read().split()
    if not raw_input:
        return
    
    n = int(raw_input[0])
    b = int(raw_input[1])
    
    adj = [[] for _ in range(n + 1)]
    pos = 2
    for _ in range(b):
        if pos + 1 >= len(raw_input):
            break
        u, v = int(raw_input[pos]), int(raw_input[pos+1])
        adj[u].append(v)
        adj[v].append(u)
        pos += 2
        
    # Tarjan의 다리(Bridge) 찾기 알고리즘 변수
    dfn = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = 0
    bridges = []
    
    def find_bridges(u, p):
        nonlocal timer
        dfn[u] = low[u] = timer
        timer += 1
        for v in adj[u]:
            if v == p: 
                continue
            if dfn[v] == -1:
                find_bridges(v, u)
                low[u] = min(low[u], low[v])
                # 자식의 low값이 자신의 dfn보다 크면 해당 간선은 다리(Bridge)
                if low[v] > dfn[u]:
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], dfn[v])
                
    # 그래프 내의 모든 다리 탐색
    for i in range(1, n + 1):
        if dfn[i] == -1:
            find_bridges(i, -1)
            
    # 다리를 제외하고 이중 연결 성분(ECC)으로 노드 그룹화
    is_bridge = set()
    for u, v in bridges:
        is_bridge.add(tuple(sorted((u, v))))
        
    comp_id = [-1] * (n + 1)
    comp_cnt = 0
    for i in range(1, n + 1):
        if comp_id[i] == -1:
            queue = [i]
            comp_id[i] = comp_cnt
            while queue:
                u = queue.pop()
                for v in adj[u]:
                    if comp_id[v] == -1 and tuple(sorted((u, v))) not in is_bridge:
                        comp_id[v] = comp_cnt
                        queue.append(v)
            comp_cnt += 1
            
    # 압축된 트리에서의 차수(degree) 계산
    comp_degree = [0] * comp_cnt
    for u, v in bridges:
        u_comp = comp_id[u]
        v_comp = comp_id[v]
        comp_degree[u_comp] += 1
        comp_degree[v_comp] += 1
        
    # 차수가 1인 성분(단말 노드)의 개수 파악
    leaf_count = 0
    for d in comp_degree:
        if d == 1:
            leaf_count += 1
            
    # 결과 출력: (단말 노드 개수 + 1) // 2
    print((leaf_count + 1) // 2)

if __name__ == "__main__":
    solve()

########################################################################################################



