import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    K = int(input[0])
    N = int(input[1])
    
    plates = []
    y_coords = []
    
    ptr = 2
    for _ in range(N):
        pid, x, ymin, ymax = map(int, input[ptr:ptr+4])
        plates.append((x, ymin, ymax, pid))
        y_coords.append(ymin)
        y_coords.append(ymax)
        ptr += 4
        
    # 좌표 압축
    y_coords = sorted(list(set(y_coords)))
    y_map = {val: i for i, val in enumerate(y_coords)}
    m = len(y_coords) - 1
    
    # 비재귀 세그먼트 트리 설정을 위한 크기 결정 (2의 거듭제곱)
    size = 1
    while size < m:
        size *= 2
        
    # t: 구간 최솟값, d: lazy 값 (지연 전파용)
    t = [0] * (2 * size)
    d = [0] * size

    def apply(p, value):
        t[p] += value
        if p < size:
            d[p] += value

    def build(p):
        while p > 1:
            p >>= 1
            t[p] = min(t[p << 1], t[p << 1 | 1]) + d[p]

    def push(p):
        for s in range(size.bit_length(), 0, -1):
            i = p >> s
            if d[i] != 0:
                apply(i << 1, d[i])
                apply(i << 1 | 1, d[i])
                d[i] = 0

    def update(l, r, value):
        l += size
        r += size
        l0, r0 = l, r
        while l < r:
            if l & 1:
                apply(l, value)
                l += 1
            if r & 1:
                r -= 1
                apply(r, value)
            l >>= 1
            r >>= 1
        build(l0)
        build(r0 - 1)

    def query(l, r):
        l += size
        r += size
        push(l)
        push(r - 1)
        res = float('inf')
        while l < r:
            if l & 1:
                res = min(res, t[l])
                l += 1
            if r & 1:
                r -= 1
                res = min(res, t[r])
            l >>= 1
            r >>= 1
        return res

    # x 좌표 기준 정렬
    plates.sort()
    
    safe_plates = []
    for x, ymin, ymax, pid in plates:
        l_idx = y_map[ymin]
        r_idx = y_map[ymax]
        
        # 해당 구간이 이미 K번 이상 가려졌는지 확인
        if query(l_idx, r_idx) >= K:
            safe_plates.append(pid)
        
        # 현재 철판으로 구간 업데이트
        update(l_idx, r_idx, 1)
        
    if not safe_plates:
        print(0)
    else:
        print(*(sorted(safe_plates)))

if __name__ == "__main__":
    solve()

########################################################

 