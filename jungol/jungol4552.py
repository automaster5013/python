import sys

# 재귀 한도 설정 (CDQ 분할 정복용)
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def update(rank, val, bit, size):
    while rank <= size:
        bit[rank] += val
        rank += rank & (-rank)

def query(rank, bit):
    s = 0
    while rank > 0:
        s += bit[rank]
        rank -= rank & (-rank)
    return s

def solve_cdq(l, r, events, ans, bit, bit_size):
    if l >= r:
        return
    
    mid = (l + r) // 2
    solve_cdq(l, mid, events, ans, bit, bit_size)
    solve_cdq(mid + 1, r, events, ans, bit, bit_size)
    
    # 2차원(B 성적) 내림차순 처리를 위한 두 포인터 활용
    ptr_l = l
    for ptr_r in range(mid + 1, r + 1):
        # 질의 데이터인 경우에만 왼쪽(A 성적이 더 높은 그룹)의 학생 데이터를 반영
        if events[ptr_r][2] == 1:  # Type 1: Query
            while ptr_l <= mid and events[ptr_l][1] >= events[ptr_r][1]:
                if events[ptr_l][2] == 0:  # Type 0: Student
                    update(events[ptr_l][3], 1, bit, bit_size)
                ptr_l += 1
            ans[events[ptr_r][4]] += query(events[ptr_r][3], bit)
            
    # BIT 초기화 (다음 단계를 위해 사용한 만큼 차감)
    for k in range(l, ptr_l):
        if events[k][2] == 0:
            update(events[k][3], -1, bit, bit_size)
            
    # B 성적 내림차순으로 정렬 유지 (Merge Sort 효과)
    events[l:r+1] = sorted(events[l:r+1], key=lambda x: (-x[1], x[2]))

def main():
    # 입력 처리
    try:
        line1 = input().split()
        if not line1: return
        n, q = map(int, line1)
    except ValueError: return

    students = []
    for _ in range(n):
        students.append(list(map(int, input().split())))
    
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())) + [i])

    # 합계 점수(Z)와 학생 점수 합계(A+B) 좌표 압축
    # 내림차순 정렬하여 큰 값이 작은 인덱스를 갖게 함 (BIT 쿼리 단순화)
    total_scores = []
    for a, b in students:
        total_scores.append(a + b)
    for x, y, z, i in queries:
        total_scores.append(z)
    
    sorted_totals = sorted(list(set(total_scores)), reverse=True)
    rank_map = {val: i + 1 for i, val in enumerate(sorted_totals)}
    bit_size = len(sorted_totals)
    
    # 이벤트 생성: (A, B, type, sum_rank, original_id)
    # type 0: 학생, type 1: 질의
    events = []
    for a, b in students:
        events.append([a, b, 0, rank_map[a + b], None])
    for x, y, z, i in queries:
        events.append([x, y, 1, rank_map[z], i])
        
    # 1차원(A 성적) 내림차순 정렬
    events.sort(key=lambda x: (-x[0], x[2]))
    
    ans = [0] * q
    bit = [0] * (bit_size + 1)
    
    solve_cdq(0, len(events) - 1, events, ans, bit, bit_size)
    
    # 결과 출력
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

if __name__ == "__main__":
    main()

#################################################################################

