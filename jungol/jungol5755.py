import sys
import bisect

# 세그먼트 트리 탐색을 위한 재귀 깊이 제한 확장
sys.setrecursionlimit(500000)

def solve():
    # 제너레이터를 이용한 메모리 효율적 입력 처리
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    input_gen = get_input()
    
    try:
        n = int(next(input_gen))
        m = int(next(input_gen))
    except StopIteration:
        return

    # 고기 데이터 로드 및 s 좌표 기준 정렬
    meats = []
    for _ in range(n):
        s = int(next(input_gen))
        e = int(next(input_gen))
        t = int(next(input_gen))
        meats.append((s, e, t))
    
    # s 좌표로 정렬하여 인덱스 기반 세그먼트 트리 구성 준비
    meats.sort()
    
    meat_s = [m[0] for m in meats]
    meat_e = [m[1] for m in meats]
    meat_t = [m[2] for m in meats]
    
    # 세그먼트 트리 크기 설정 (2의 거듭제곱)
    size = 1
    while size < n:
        size *= 2
    
    # tree[v]는 해당 구간 고기들 중 최대 e_i 값을 저장 (제거된 경우 -1)
    tree = [-1] * (2 * size)
    for i in range(n):
        tree[size + i] = meat_e[i]
    
    # 트리 빌드 (Bottom-up)
    for i in range(size - 1, 0, -1):
        l, r = tree[2 * i], tree[2 * i + 1]
        tree[i] = l if l > r else r
        
    # 조건에 맞는 고기를 찾아 제거하고 점수를 반환하는 함수
    def find_and_delete(v, tl, tr, R, e_min, eaten_e_min):
        # 1. 구간의 최대 e가 기준보다 작거나, s 범위(R)를 벗어나면 즉시 종료 (Pruning)
        if tree[v] < e_min or tl > R:
            return 0
        
        # 2. 리프 노드에 도달한 경우
        if tl == tr:
            # 두 꼬치 조건(s <= a, e >= b+1)을 모두 만족하면 점수 반환
            res = meat_t[tl] if meat_e[tl] >= eaten_e_min else 0
            tree[v] = -1 # 그릴에서 제거
            return res
        
        # 3. 자식 노드 탐색
        tm = (tl + tr) // 2
        res = find_and_delete(2 * v, tl, tm, R, e_min, eaten_e_min)
        if tm < R: # 오른쪽 자식 범위에 s_i <= a 인 고기가 있을 때만 탐색
            res += find_and_delete(2 * v + 1, tm + 1, tr, R, e_min, eaten_e_min)
        
        # 4. 부모 노드 최댓값 갱신
        l, r = tree[2 * v], tree[2 * v + 1]
        tree[v] = l if l > r else r
        return res

    results = []
    INF = 2000000001 # 절대 도달할 수 없는 큰 값

    for _ in range(m):
        a = int(next(input_gen))
        b = int(next(input_gen))
        
        # 꼬치 A(a+0.1)가 닿는 s 좌표의 최대 인덱스 찾기
        idx_a = bisect.bisect_right(meat_s, a) - 1
        # 꼬치 A에 꽂힌 고기 제거 및 점수 계산 (e >= b+1 조건 확인)
        score = find_and_delete(1, 0, size - 1, idx_a, a + 1, b + 1)
        
        # 꼬치 B(b+0.9)가 닿는 s 좌표의 최대 인덱스 찾기
        idx_b = bisect.bisect_right(meat_s, b) - 1
        # 꼬치 B에 꽂힌 남은 고기 제거 (이들은 먹을 수 없음)
        find_and_delete(1, 0, size - 1, idx_b, b + 1, INF)
        
        results.append(str(score))
        
    # 결과 일괄 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()

###########################################################################

