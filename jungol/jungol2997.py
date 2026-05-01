import sys

# 대규모 데이터 처리를 위해 재귀 제한을 늘리고 빠른 입력을 사용합니다.
sys.setrecursionlimit(300000)
input = sys.stdin.read

def solve():
    # 모든 데이터를 한 번에 읽어와 처리 속도를 높입니다.
    data = input().split()
    if not data:
        return
    
    ptr = 0
    N = int(data[ptr]); ptr += 1 # 정점의 개수
    Q = int(data[ptr]); ptr += 1 # 질의의 개수
    
    # 각 정점의 부모 정보를 저장합니다. (1번은 루트)
    parent = [0] * (N + 1)
    for i in range(2, N + 1):
        parent[i] = int(data[ptr]); ptr += 1
        
    # (N-1)개의 에지 제거 정보와 Q개의 경로 질의를 모두 저장합니다.
    queries = []
    total_ops = (N - 1) + Q
    for _ in range(total_ops):
        op = list(map(int, data[ptr:ptr+3]))
        if op[0] == 0:
            queries.append((0, op[1]))
            ptr += 2
        else:
            queries.append((1, op[1], op[2]))
            ptr += 3
            
    # DSU(서로소 집합) 초기화
    dsu = list(range(N + 1))
    
    # 경로 압축(Path Compression)이 적용된 find 함수 (반복문 구현)
    def find(i):
        root = i
        while dsu[root] != root:
            root = dsu[root]
        while dsu[i] != root:
            next_node = dsu[i]
            dsu[i] = root
            i = next_node
        return root

    # 두 집합을 합치는 union 함수
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            dsu[root_i] = root_j

    # 결과를 저장할 리스트 (역순으로 처리하므로 나중에 뒤집어야 함)
    ans = []
    
    # 모든 쿼리를 역순(마지막 작업부터 첫 번째 작업까지)으로 순회합니다.
    for i in range(len(queries) - 1, -1, -1):
        q = queries[i]
        if q[0] == 1:
            # 경로 질의: c와 d를 연결하는 경로가 존재하는가?
            if find(q[1]) == find(q[2]):
                ans.append("YES")
            else:
                ans.append("NO")
        else:
            # 에지 복구: b의 부모와 b를 다시 연결합니다.
            union(q[1], parent[q[1]])
            
    # 역순으로 저장된 답을 다시 뒤집어 한꺼번에 출력합니다.
    sys.stdout.write('\n'.join(ans[::-1]) + '\n')

if __name__ == "__main__":
    solve()

###########################################################################

