import sys

def solve():
    # 고속 입력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    # 빵 맛 리스트를 정수로 변환하여 정렬
    breads = sorted([int(x) for x in input_data[2:]])

    # 1. 초기 윈도우 (0 ~ k-1)의 분노도와 합 계산
    current_anger = 0
    window_sum = 0
    for i in range(k):
        # 정렬된 상태에서 각 원소의 기여도 계산 식
        current_anger += (2 * i - k + 1) * breads[i]
        window_sum += breads[i]

    min_anger = current_anger

    # 2. 슬라이딩 윈도우 시작
    for i in range(n - k):
        # 현재 윈도우에서 빠질 값과 새로 들어올 값
        out_val = breads[i]
        in_val = breads[i + k]
        
        # 중간 부분(i+1 ~ i+k-1)의 합
        mid_sum = window_sum - out_val
        
        # 윈도우 이동에 따른 분노도 변화량 계산 (O(1))
        # 이전 분노도 - (중간합 - (k-1)*out) + ((k-1)*in - 중간합)
        current_anger = current_anger + (k - 1) * (out_val + in_val) - 2 * mid_sum
        
        # 윈도우 전체 합 갱신
        window_sum = mid_sum + in_val
        
        if current_anger < min_anger:
            min_anger = current_anger

    print(min_anger)

if __name__ == "__main__":
    solve()

#####################################################################################



