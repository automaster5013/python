import sys

def solve():
    # 대량의 데이터를 한 번에 읽어 처리 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    M = int(input_data[ptr]); ptr += 1
    
    # line[i]는 왼쪽에서 i번째에 서 있는 학생의 번호 (1-based)
    line = [0] * (N + 1)
    # pos[id]는 학생 번호 id가 서 있는 위치 (1-based)
    pos = [0] * (N + 1)
    
    for i in range(1, N + 1):
        student_id = int(input_data[ptr]); ptr += 1
        line[i] = student_id
        pos[student_id] = i

    # 세그먼트 트리 크기 설정 (2의 거듭제곱)
    size = 1 << (N - 1).bit_length()
    INF = float('inf')
    min_tree = [INF] * (2 * size)
    max_tree = [-INF] * (2 * size)

    # 초기 트리 구축 (학생 번호를 기준으로 위치 저장)
    for i in range(1, N + 1):
        min_tree[size + i - 1] = pos[i]
        max_tree[size + i - 1] = pos[i]

    for i in range(size - 1, 0, -1):
        min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
        max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])

    def update(student_id, new_pos):
        idx = size + student_id - 1
        min_tree[idx] = new_pos
        max_tree[idx] = new_pos
        while idx > 1:
            idx //= 2
            min_tree[idx] = min(min_tree[2 * idx], min_tree[2 * idx + 1])
            max_tree[idx] = max(max_tree[2 * idx], max_tree[2 * idx + 1])

    def query(a, b):
        l, r = size + a - 1, size + b - 1
        res_min = INF
        res_max = -INF
        while l <= r:
            if l % 2 == 1:
                res_min = min(res_min, min_tree[l])
                res_max = max(res_max, max_tree[l])
                l += 1
            if r % 2 == 0:
                res_min = min(res_min, min_tree[r])
                res_max = max(res_max, max_tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res_min, res_max

    output = []
    for _ in range(M):
        cmd = int(input_data[ptr]); ptr += 1
        if cmd == 1:
            x, y = int(input_data[ptr]), int(input_data[ptr+1]); ptr += 2
            # x번째 학생과 y번째 학생의 번호를 찾음
            student_x = line[x]
            student_y = line[y]
            
            # 줄에서의 번호 교체
            line[x], line[y] = student_y, student_x
            
            # 트리에 저장된 각 학생의 위치(pos) 업데이트
            update(student_x, y)
            update(student_y, x)
        else:
            a, b = int(input_data[ptr]), int(input_data[ptr+1]); ptr += 2
            p_min, p_max = query(a, b)
            
            # 연속 구간 판정
            if p_max - p_min == b - a:
                output.append("YES")
            else:
                output.append("NO")

    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

#############################################################################

