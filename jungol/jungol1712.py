import sys

# 입력을 빠르게 읽기 위해 sys.stdin.read를 사용합니다.
def solve():
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    N = int(raw_data[0])
    M = int(raw_data[1])
    
    # 각 정점의 인접 리스트 (자기 자신 포함)
    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        adj[i].append(i)
        
    idx = 2
    for _ in range(M):
        if idx + 1 >= len(raw_data):
            break
        u = int(raw_data[idx])
        v = int(raw_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # 잎 노드들을 인접 리스트(정렬된 튜플) 기준으로 그룹화
    leaf_to_internal = [0] * (N + 1)
    groups = {} # (정렬된 인접 리스트 튜플) -> 내부 노드 번호
    group_representatives = {} # 내부 노드 번호 -> (정렬된 인접 리스트 튜플)
    
    curr_id = N + 1
    for i in range(1, N + 1):
        adj[i].sort()
        key = tuple(adj[i])
        if key not in groups:
            groups[key] = curr_id
            group_representatives[curr_id] = key
            curr_id += 1
        leaf_to_internal[i] = groups[key]
        
    tree_edges = []
    
    # 1. 잎 노드와 해당 내부 노드(부모) 연결
    for i in range(1, N + 1):
        tree_edges.append((i, leaf_to_internal[i]))
        
    # 2. 내부 노드 간의 스켈레톤 연결 (거리 3 관계)
    seen_internal_edges = set()
    for internal_id, neighbors in group_representatives.items():
        for neighbor_leaf in neighbors:
            neighbor_internal_id = leaf_to_internal[neighbor_leaf]
            if internal_id != neighbor_internal_id:
                # 중복 에지를 피하기 위해 정렬하여 저장
                u_id, v_id = (internal_id, neighbor_internal_id) if internal_id < neighbor_internal_id else (neighbor_internal_id, internal_id)
                if (u_id, v_id) not in seen_internal_edges:
                    seen_internal_edges.add((u_id, v_id))
                    tree_edges.append((u_id, v_id))
                    
    # 출력 형식에 맞춰 트리 에지 개수와 목록 출력
    sys.stdout.write(str(len(tree_edges)) + "\n")
    for u, v in tree_edges:
        sys.stdout.write(str(u) + " " + str(v) + "\n")

if __name__ == "__main__":
    solve()

######################################################################

