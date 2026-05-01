import sys

# 입력을 한 번에 읽어와 처리 속도를 높입니다.
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    # 콜라와 피자의 맛 정보를 리스트로 저장
    cola = list(map(int, data[1:N+1]))
    pizza = list(map(int, data[N+1:2*N+1]))
    Q = int(data[2*N+1])
    queries = data[2*N+2:]

    # 세그먼트 트리 크기 설정 (2의 거듭제곱)
    size = 1
    while size < N:
        size *= 2
    
    # 각 노드: [max_cola, max_pizza, max_sum]
    # 맛은 자연수이므로 초기값을 0으로 설정해도 무방합니다.
    tree = [[0, 0, 0] for _ in range(2 * size)]

    def merge(l_node, r_node):
        # 새로운 노드의 콜라/피자 최댓값 계산
        max_c = l_node[0] if l_node[0] > r_node[0] else r_node[0]
        max_p = l_node[1] if l_node[1] > r_node[1] else r_node[1]
        
        # maxSum 후보:
        # 1. 왼쪽 자식의 maxSum
        # 2. 오른쪽 자식의 maxSum
        # 3. 왼쪽의 콜라 최댓값 + 오른쪽의 피자 최댓값 (i < j 조건 충족)
        cross_sum = l_node[0] + r_node[1]
        max_s = l_node[2]
        if r_node[2] > max_s: max_s = r_node[2]
        if cross_sum > max_s: max_s = cross_sum
        
        return [max_c, max_p, max_s]

    # 트리 초기 구축
    for i in range(N):
        tree[size + i] = [cola[i], pizza[i], 0]
    
    for i in range(size - 1, 0, -1):
        tree[i] = merge(tree[2 * i], tree[2 * i + 1])

    # 1, 2번 명령: 값 업데이트
    def update(idx, val, is_cola):
        node_idx = size + idx - 1
        if is_cola:
            tree[node_idx][0] = val
        else:
            tree[node_idx][1] = val
        
        node_idx //= 2
        while node_idx >= 1:
            tree[node_idx] = merge(tree[2 * node_idx], tree[2 * node_idx + 1])
            node_idx //= 2

    # 3번 명령: 구간 쿼리
    def query(l, r):
        l += size - 1
        r += size - 1
        l_res = None
        r_res = None
        
        while l <= r:
            if l % 2 == 1:
                if l_res is None:
                    l_res = tree[l][:] # 독립된 리스트 복사
                else:
                    l_res = merge(l_res, tree[l])
                l += 1
            if r % 2 == 0:
                if r_res is None:
                    r_res = tree[r][:]
                else:
                    r_res = merge(tree[r], r_res)
                r -= 1
            l //= 2
            r //= 2
            
        # l_res와 r_res의 존재 여부에 따른 안전한 병합
        if l_res is None: return r_res[2]
        if r_res is None: return l_res[2]
        return merge(l_res, r_res)[2]

    # 쿼리 순회
    ptr = 0
    results = []
    for _ in range(Q):
        q_type = int(queries[ptr])
        if q_type == 1:
            update(int(queries[ptr+1]), int(queries[ptr+2]), True)
            ptr += 3
        elif q_type == 2:
            update(int(queries[ptr+1]), int(queries[ptr+2]), False)
            ptr += 3
        else:
            results.append(str(query(int(queries[ptr+1]), int(queries[ptr+2]))))
            ptr += 3

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

#####################################################################################

