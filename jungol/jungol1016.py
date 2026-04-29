import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    nums = list(map(int, input_data[1:]))
    
    # 2. 각 숫자의 전체 개수 카운트
    c1 = nums.count(1)
    c2 = nums.count(2)
    c3 = nums.count(3)
    
    # 3. 구역별 데이터 분포 파악
    # m[i][j] = i구역에 있는 숫자 j의 개수
    m = [[0] * 4 for _ in range(4)]
    
    # 1구역 검사
    for i in range(0, c1):
        m[1][nums[i]] += 1
    # 2구역 검사
    for i in range(c1, c1 + c2):
        m[2][nums[i]] += 1
    # 3구역 검사
    for i in range(c1 + c2, n):
        m[3][nums[i]] += 1
        
    # 4. 최소 교환 횟수 계산
    swaps = 0
    
    # (1) 직접 교환: 서로의 구역에 있는 숫자를 맞바꿈
    # 1구역의 2 <-> 2구역의 1
    d12 = min(m[1][2], m[2][1])
    swaps += d12
    m[1][2] -= d12; m[2][1] -= d12
    
    # 1구역의 3 <-> 3구역의 1
    d13 = min(m[1][3], m[3][1])
    swaps += d13
    m[1][3] -= d13; m[3][1] -= d13
    
    # 2구역의 3 <-> 3구역의 2
    d23 = min(m[2][3], m[3][2])
    swaps += d23
    m[2][3] -= d23; m[3][2] -= d23
    
    # (2) 간접/순환 교환
    # 직접 교환 후 남은 잘못된 숫자들은 반드시 3개씩 사이클을 이룸
    # 사이클 하나당 2번의 스왑 필요
    remaining_misplaced = m[1][2] + m[1][3]  # 1구역에 남은 잘못된 숫자들
    swaps += remaining_misplaced * 2
    
    print(swaps)

if __name__ == "__main__":
    solve()

###########################################################################

