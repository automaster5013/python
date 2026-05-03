import sys

# 유니온-파인드(Union-Find)를 위한 부모 배열 초기화
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

def solve():
    # 입력 처리
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])  # 목초지 수
    
    edges = []
    
    # 1. 우물 파는 비용을 0번 노드와의 간선으로 추가
    for i in range(1, n + 1):
        w_i = int(input[i])
        edges.append((w_i, 0, i))
    
    # 2. 파이프 연결 비용을 간선으로 추가
    # 파이프 비용 행렬은 n+1번째 데이터부터 시작함
    matrix_start = n + 1
    for i in range(1, n + 1):
        row = input[matrix_start + (i-1)*n : matrix_start + i*n]
        for j in range(1, n + 1):
            p_ij = int(row[j-1])
            if i < j:  # 무방향 그래프이므로 중복 방지
                edges.append((p_ij, i, j))
    
    # 3. 크루스칼 알고리즘 적용
    # 간선 비용 기준 오름차순 정렬
    edges.sort()
    
    parent = list(range(n + 1))
    total_cost = 0
    edges_count = 0
    
    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_cost += cost
            edges_count += 1
            # 모든 노드(N+1개)가 연결되려면 간선은 N개 필요
            if edges_count == n:
                break
                
    print(total_cost)

if __name__ == "__main__":
    solve()

########################################################################


