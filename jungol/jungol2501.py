import sys
from itertools import permutations

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    nums = list(map(int, input_data[1:]))
    
    # 1. 각 숫자의 전체 개수 카운트 및 누적 합 계산
    counts = [0, 0, 0, 0]
    prefix_sum = [[0] * (n + 1) for _ in range(4)]
    
    for i in range(n):
        val = nums[i]
        counts[val] += 1
        for j in range(1, 4):
            prefix_sum[j][i+1] = prefix_sum[j][i] + (1 if val == j else 0)
            
    # 구간 [start, end) 내의 특정 숫자 개수를 반환하는 함수
    def get_count(num, start, end):
        return prefix_sum[num][end] - prefix_sum[num][start]

    min_swaps = float('inf')
    
    # 2. 가능한 6가지 정렬 순서(순열) 시도
    for p in permutations([1, 2, 3]):
        # 구역 경계 설정
        z1_target, z2_target, z3_target = p
        
        # 각 구역의 시작과 끝 인덱스
        s1, e1 = 0, counts[z1_target]
        s2, e2 = e1, e1 + counts[z2_target]
        s3, e3 = e2, e2 + counts[z3_target]
        
        # M[i][j]: i구역에 있는 j모양의 개수
        # (구역 번호는 타겟 숫자로 매핑)
        m = {t: {1: 0, 2: 0, 3: 0} for t in [1, 2, 3]}
        
        for shape in [1, 2, 3]:
            m[z1_target][shape] = get_count(shape, s1, e1)
            m[z2_target][shape] = get_count(shape, s2, e2)
            m[z3_target][shape] = get_count(shape, s3, e3)
            
        # 3. 교환 횟수 계산
        # 직접 교환 (두 구역 간 서로 필요한 걸 주고받음)
        s12 = min(m[z1_target][z2_target], m[z2_target][z1_target])
        s13 = min(m[z1_target][z3_target], m[z3_target][z1_target])
        s23 = min(m[z2_target][z3_target], m[z3_target][z2_target])
        
        direct_swaps = s12 + s13 + s23
        
        # 순환 교환 (남은 미배치 아이템 처리)
        # 한 구역에서 직접 교환 후 남은 잘못된 아이템의 수 * 2
        remaining = (m[z1_target][z2_target] - s12) + (m[z1_target][z3_target] - s13)
        circular_swaps = remaining * 2
        
        min_swaps = min(min_swaps, direct_swaps + circular_swaps)

    print(min_swaps)

if __name__ == "__main__":
    solve()

#######################################################################################

