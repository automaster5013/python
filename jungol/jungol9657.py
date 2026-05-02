import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    queries = []
    unique_heights = set()
    
    ptr = 1
    for _ in range(n):
        v = int(input_data[ptr])
        a = int(input_data[ptr + 1])
        queries.append((v, a))
        unique_heights.add(v)
        ptr += 2
        
    # 1. 좌표 압축 (Coordinate Compression)
    sorted_v = sorted(list(unique_heights))
    v_map = {val: i + 1 for i, val in enumerate(sorted_v)}
    num_unique = len(sorted_v)
    
    # 2. 펜윅 트리 (Binary Indexed Tree)
    # 학생 수의 합이 2^31-1을 넘을 수 있으므로 Python의 큰 정수 연산을 활용합니다.
    bit = [0] * (num_unique + 1)
    
    def update(i, delta):
        while i <= num_unique:
            bit[i] += delta
            i += i & (-i)
            
    def find_kth(k):
        # BIT 위에서의 Binary Lifting (O(log N))
        idx = 0
        current_sum = 0
        for i in range(num_unique.bit_length() - 1, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx <= num_unique and current_sum + bit[next_idx] < k:
                idx = next_idx
                current_sum += bit[idx]
        return idx + 1

    total_students = 0
    results = []
    
    # 3. 데이터 입력 시마다 중앙값 계산
    for v, a in queries:
        total_students += a
        update(v_map[v], a)
        
        # 중앙값 위치: (전체 학생 수 + 1) // 2
        target_rank = (total_students + 1) // 2
        kth_idx = find_kth(target_rank)
        results.append(str(sorted_v[kth_idx - 1]))
        
    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

########################################################################

