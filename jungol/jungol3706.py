import sys

def solve():
    # 고속 입력을 통해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    nums = list(map(int, input_data[1:]))

    # 누적 합의 빈도를 저장할 딕셔너리
    # 초기값 0이 1번 나왔다고 설정해야 합니다. (처음부터 특정 지점까지의 합이 0인 경우 대비)
    prefix_counts = {0: 1}
    
    current_prefix_sum = 0
    total_cases = 0
    
    for num in nums:
        # 현재까지의 누적 합 계산
        current_prefix_sum += num
        
        # 만약 현재 누적 합과 같은 값이 이전에 등장했다면
        if current_prefix_sum in prefix_counts:
            # 그 개수만큼 0이 되는 구간이 존재함
            total_cases += prefix_counts[current_prefix_sum]
            # 빈도수 업데이트
            prefix_counts[current_prefix_sum] += 1
        else:
            # 처음 등장하는 누적 합 기록
            prefix_counts[current_prefix_sum] = 1
            
    print(total_cases)

if __name__ == "__main__":
    solve()

#########################################################################################

