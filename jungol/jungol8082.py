import sys
from array import array

def solve():
    # 메모리를 아끼기 위한 제너레이터 기반 입력
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    tokens = get_input()
    
    try:
        n = int(next(tokens))
    except StopIteration: return

    # 1. 초기 배열 누적 합 (O(N)) - 펜윅 트리보다 훨씬 빠름
    # 'q'는 8바이트 정수형 (long long)
    init_prefix_sum = array('q', [0] * (n + 1))
    for i in range(1, n + 1):
        init_prefix_sum[i] = init_prefix_sum[i-1] + int(next(tokens))
    
    try:
        q = int(next(tokens))
    except StopIteration: return

    # 2. 업데이트된 값(Delta)만 관리하는 두 개의 펜윅 트리
    # 크기를 n+2로 설정하여 r+1 인덱스 에러 방지
    bit1 = array('q', [0] * (n + 2))
    bit2 = array('q', [0] * (n + 2))

    def update(bit, idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)

    def query(bit, idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    def get_delta_sum(idx):
        if idx <= 0: return 0
        # 구간 업데이트/구간 합 공식: (idx+1)*sum(D) - sum(i*D)
        return query(bit1, idx) * (idx + 1) - query(bit2, idx)

    output = []
    for _ in range(q):
        try:
            cmd = next(tokens)
            if cmd == '1':
                f, r, x = int(next(tokens)), int(next(tokens)), int(next(tokens))
                # 변화량(Delta) 트리에만 업데이트
                update(bit1, f, x)
                update(bit1, r + 1, -x)
                update(bit2, f, x * f)
                update(bit2, r + 1, -x * (r + 1))
            else:
                f, r = int(next(tokens)), int(next(tokens))
                # 최종 합 = (초기 누적 합) + (업데이트된 누적 합)
                original_range_sum = init_prefix_sum[r] - init_prefix_sum[f-1]
                added_range_sum = get_delta_sum(r) - get_delta_sum(f-1)
                output.append(str(original_range_sum + added_range_sum))
        except StopIteration:
            break
            
    # 결과 출력
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()

######################################################################################
