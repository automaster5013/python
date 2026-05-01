import sys

def solve():
    # 고속 입력을 위해 데이터를 한꺼번에 읽어옵니다.
    # N, M이 크기 때문에 일반적인 input()은 병목 현상의 원인이 됩니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    
    # 토마토 숙성도 정보 (값, 원래 인덱스)
    a = list(map(int, input_data[2:n+2]))
    tomatoes = sorted([(val, i + 1) for i, val in enumerate(a)])

    # 각 질의를 두 개의 서브 질의로 나눕니다 (H 이하 개수 - L-1 이하 개수)
    sub_queries = []
    idx_ptr = n + 2
    for i in range(m):
        s = int(input_data[idx_ptr])
        e = int(input_data[idx_ptr + 1])
        l = int(input_data[idx_ptr + 2])
        h = int(input_data[idx_ptr + 3])
        idx_ptr += 4

        # (기준 숙성도, 시작점, 끝점, 쿼리 번호, 부호)
        sub_queries.append((h, s, e, i, 1))
        sub_queries.append((l - 1, s, e, i, -1))

    # 서브 질의를 숙성도 기준치(limit) 순으로 정렬합니다.
    sub_queries.sort()

    # 펜윅 트리 (Binary Indexed Tree) 구현
    bit = [0] * (n + 1)

    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)

    def query_bit(idx):
        res = 0
        while idx > 0:
            res += bit[idx]
            idx -= idx & (-idx)
        return res

    results = [0] * m
    t_ptr = 0
    
    # 숙성도가 낮은 토마토부터 트리에 추가하며 질의를 처리합니다.
    for limit, s, e, q_idx, sign in sub_queries:
        while t_ptr < n and tomatoes[t_ptr][0] <= limit:
            update(tomatoes[t_ptr][1], 1)
            t_ptr += 1
        
        # 구간 [s, e]에 속하는 토마토 개수 계산
        count = query_bit(e) - query_bit(s - 1)
        results[q_idx] += sign * count

    # 결과 출력
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    solve()

#####################################################################


