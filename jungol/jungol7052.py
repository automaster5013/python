import sys

def solve():
    # 고속 입력을 통해 데이터 로드
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    R = int(input_data[0])
    S = int(input_data[1])
    a = int(input_data[2])
    b = int(input_data[3])
    
    grid = []
    it = iter(input_data[4:])
    for r in range(R):
        grid.append([int(next(it)) for _ in range(S)])
        
    # a, b의 범위를 설정
    min_ab = min(a, b)
    max_ab = max(a, b)
    sum_ab = a + b
    target_min = max_ab - min_ab # 구간 내에 있을 때의 최솟값
    
    # 가로가 세로보다 길면 전치(Transpose)하여 연산 횟수 최적화
    if S < R:
        grid = list(zip(*grid))
        R, S = S, R
        
    ans = float('inf')
    
    # r1: 시작 행, r2: 끝 행
    for r1 in range(R):
        col_sums = [0] * S
        for r2 in range(r1, R):
            row_data = grid[r2]
            
            # 1차원 투 포인터 (슬라이딩 윈도우)
            left = 0
            curr_sum = 0
            for right in range(S):
                col_sums[right] += row_data[right]
                curr_sum += col_sums[right]
                
                # 합이 범위를 초과할 때까지 왼쪽 포인터를 이동하며 체크
                while curr_sum > max_ab:
                    # C > max_ab 인 경우: f(C) = 2*C - (a+b)
                    diff = 2 * curr_sum - sum_ab
                    if diff < ans: ans = diff
                    
                    curr_sum -= col_sums[left]
                    left += 1
                
                # 이제 curr_sum <= max_ab 인 상태
                if left <= right:
                    if curr_sum >= min_ab:
                        # 합이 [min_ab, max_ab] 구간에 들어오면 이론적 최솟값 도달
                        print(target_min)
                        return
                    else:
                        # C < min_ab 인 경우: f(C) = (a+b) - 2*C
                        diff = sum_ab - 2 * curr_sum
                        if diff < ans: ans = diff
                        
    print(ans)

if __name__ == "__main__":
    solve()

####################################################################################

# 파이썬 최적화 코드 (PyPy3 권장)
# 이 문제는 연산량이 많으므로, LG 그램 환경에서 실행하면 
# 일반 Python 3보다는 PyPy3 언어로 제출하는 것을 강력히 추천

