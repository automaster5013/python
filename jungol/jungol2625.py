import sys

# 빠른 입력을 위한 설정
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    
    # 세그먼트 트리 크기 설정
    size = 1
    while size < N:
        size *= 2
    tree = [0] * (2 * size)
    lazy = [0] * (2 * size)

    # Lazy 값을 자식으로 전파하는 함수
    def push(node, node_l, node_r):
        if lazy[node] == 0:
            return
        
        if node < size:
            mid = (node_l + node_r) // 2
            # 왼쪽 자식 반전
            tree[2 * node] = (mid - node_l + 1) - tree[2 * node]
            lazy[2 * node] ^= 1
            # 오른쪽 자식 반전
            tree[2 * node + 1] = (node_r - mid) - tree[2 * node + 1]
            lazy[2 * node + 1] ^= 1
        
        lazy[node] = 0

    # 구간 반전 업데이트 함수
    def update(l, r, node, node_l, node_r):
        if r < node_l or node_r < l:
            return
        if l <= node_l and node_r <= r:
            tree[node] = (node_r - node_l + 1) - tree[node]
            lazy[node] ^= 1
            return
        
        push(node, node_l, node_r)
        mid = (node_l + node_r) // 2
        update(l, r, 2 * node, node_l, mid)
        update(l, r, 2 * node + 1, mid + 1, node_r)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    # 구간 합 쿼리 함수
    def query(l, r, node, node_l, node_r):
        if r < node_l or node_r < l:
            return 0
        if l <= node_l and node_r <= r:
            return tree[node]
        
        push(node, node_l, node_r)
        mid = (node_l + node_r) // 2
        return query(l, r, 2 * node, node_l, mid) + \
               query(l, r, 2 * node + 1, mid + 1, node_r)

    ptr = 2
    results = []
    for _ in range(M):
        q = int(data[ptr])
        s = int(data[ptr+1])
        e = int(data[ptr+2])
        ptr += 3
        
        if q == 0:
            update(s, e, 1, 1, size)
        else:
            results.append(str(query(s, e, 1, 1, size)))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

#############################################################

