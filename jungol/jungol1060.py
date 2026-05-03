import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    matrix = []
    idx = 1
    for i in range(n):
        matrix.append(list(map(int, input_data[idx : idx + n])))
        idx += n
        
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                edges.append((matrix[i][j], i, j))
                
    edges.sort()
    
    parent = list(range(n))
    total_cost = 0
    count = 0
    
    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_cost += cost
            count += 1
            if count == n - 1:
                break
                
    print(total_cost)

if __name__ == "__main__":
    solve()

##############################################################################



