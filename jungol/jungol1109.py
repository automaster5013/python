import sys

def solve():
    # 성냥개비 개수 입력
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        n = int(input_data)
    except EOFError:
        return

    count = 0
    
    # 가장 긴 변 c의 가능한 범위 탐색
    # c는 n/3 보다는 크거나 같아야 하고, n/2 보다는 작아야 함
    start_c = (n + 2) // 3  # math.ceil(n/3)
    end_c = (n - 1) // 2    # c < n/2 를 만족하는 정수 최대값

    for c in range(start_c, end_c + 1):
        # a + b = n - c 이고 a <= b <= c 를 만족하는 (a, b) 쌍의 개수를 구함
        # a + b = sum_ab 라고 할 때
        sum_ab = n - c
        
        # 1. a <= b 조건: a + a <= a + b = sum_ab => 2a <= sum_ab => a <= sum_ab // 2
        # 2. b <= c 조건: sum_ab - a <= c => a >= sum_ab - c
        
        a_max = sum_ab // 2
        a_min = sum_ab - c
        
        # a는 1보다 작을 수 없음
        if a_min < 1:
            a_min = 1
            
        if a_max >= a_min:
            count += (a_max - a_min + 1)

    print(count)

if __name__ == "__main__":
    solve()

#######################################################################################


