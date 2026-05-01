import sys

def solve():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]

    if n == 1:
        print(0)
        return

    # 1. 좌표 압축: 값의 상대적 크기만 중요하므로 0 ~ V-1 범위로 변환합니다.
    coords = sorted(list(set(a)))
    v_map = {val: i for i, val in enumerate(coords)}
    ca = [v_map[x] for x in a]
    v_size = len(coords)

    # 2. 펜윅 트리(BIT)를 이용해 초기 전도수 및 각 원소의 기여도(inv_i)를 계산합니다.
    bit = [0] * (v_size + 1)
    inv_i = [0] * n
    total_inv = 0
    
    # Prefix 전도수 (내 앞에 나보다 큰 수)
    for i in range(n):
        val = ca[i]
        # bit_query(val)
        res, idx = 0, val + 1
        while idx > 0:
            res += bit[idx]
            idx -= idx & (-idx)
        greater = i - res
        inv_i[i] += greater
        total_inv += greater
        # bit_update(val, 1)
        idx = val + 1
        while idx <= v_size:
            bit[idx] += 1
            idx += idx & (-idx)
            
    # Suffix 전도수 (내 뒤에 나보다 작은 수)
    bit = [0] * (v_size + 1)
    for i in range(n - 1, -1, -1):
        val = ca[i]
        # bit_query(val - 1)
        res, idx = 0, val
        while idx > 0:
            res += bit[idx]
            idx -= idx & (-idx)
        inv_i[i] += res
        # bit_update(val, 1)
        idx = val + 1
        while idx <= v_size:
            bit[idx] += 1
            idx += idx & (-idx)

    # 3. 비재귀 레이지 세그먼트 트리 최적화
    # f_i(X) = i + h_i(X) 에서 h_i(X) = (Suffix 중 < X 개수) - (Prefix 중 <= X 개수)를 관리합니다.
    size = 1 << (v_size - 1).bit_length()
    tree = [0] * (2 * size)
    lazy = [0] * (2 * size)

    # 초기 상태 (i=0) 설정: 모든 원소(A_1~A_N-1)가 Suffix에 있음
    counts = [0] * v_size
    for i in range(1, n):
        counts[ca[i]] += 1
    
    curr_h = 0
    for x in range(v_size):
        tree[size + x] = curr_h
        curr_h += counts[x]
    for x in range(v_size, size):
        tree[size + x] = 10**15 # 무한대 패딩
        
    for i in range(size - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])

    # 4. 스위핑(Sweeping): 각 i에 대해 최적의 X를 찾습니다.
    ans_list = []
    for i in range(n):
        # f_i(X)의 최솟값 = i + min(tree[1], 0, n-1-2i)
        # 0은 X가 매우 작을 때, n-1-2i는 X가 매우 클 때의 h_i(X) 값입니다.
        min_h = tree[1]
        if 0 < min_h: min_h = 0
        if (n - 1 - 2 * i) < min_h: min_h = n - 1 - 2 * i
        
        ans_list.append(str(total_inv - inv_i[i] + i + min_h))
        
        if i < n - 1:
            # i번째가 Prefix로 추가됨: X >= A[i] 범위 h 1 감소
            # i+1번째가 Suffix에서 제거됨: X > A[i+1] 범위 h 1 감소
            for start_idx in [ca[i], ca[i+1] + 1]:
                if start_idx >= v_size: continue
                l, r = start_idx + size, size + size - 1
                l0 = l
                while l <= r:
                    if l & 1:
                        tree[l] -= 1; lazy[l] -= 1; l += 1
                    l >>= 1; r >>= 1
                # 부모 노드들 업데이트 (비재귀 방식)
                p = l0 >> 1
                while p > 0:
                    tree[p] = min(tree[2 * p], tree[2 * p + 1]) + lazy[p]
                    p >>= 1

    sys.stdout.write(" ".join(ans_list) + "\n")

if __name__ == "__main__":
    solve()

###############################################################################

