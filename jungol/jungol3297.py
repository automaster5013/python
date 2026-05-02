import sys

def solve():
    # 모든 데이터를 한 번에 읽어와 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    # 초기 배열 저장 (인덱스 관리를 위해 1-based로 구성)
    arr = [0] * (N + 1)
    # 펜윅 트리 초기화
    bit = [0] * (N + 1)

    def update(idx, diff):
        while idx <= N:
            bit[idx] += diff
            idx += (idx & -idx)

    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= (idx & -idx)
        return s

    # 초기 배열 값 입력 및 트리 구축
    for i in range(1, N + 1):
        val = int(input_data[i])
        arr[i] = val
        update(i, val)

    m_idx = N + 1
    M = int(input_data[m_idx])
    
    ptr = m_idx + 1
    results = []
    
    # M개의 명령 처리
    for _ in range(M):
        cmd = input_data[ptr]
        if cmd == '1':
            idx = int(input_data[ptr + 1])
            new_val = int(input_data[ptr + 2])
            ptr += 3
            # 값의 차이를 계산하여 트리에 반영
            diff = new_val - arr[idx]
            arr[idx] = new_val
            update(idx, diff)
        else:
            st = int(input_data[ptr + 1])
            ed = int(input_data[ptr + 2])
            ptr += 3
            # 구간 합 계산: Sum(1~ed) - Sum(1~st-1)
            ans = query(ed) - query(st - 1)
            results.append(str(ans))

    # 결과 일괄 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

#######################################################

