import sys

def solve():
    # 고속 입력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = input_data[1]

    # 1. 각 숫자에서 1을 뺀 값의 누적 합을 구함
    # 누적 합의 초기값 0은 반드시 포함되어야 함 (처음부터 특정 지점까지의 합이 0인 경우 대비)
    prefix_sum = 0
    counts = {0: 1} # 누적 합의 빈도를 저장할 딕셔너리
    
    total_cases = 0
    
    for char in s:
        # 숫자에서 1을 뺀 값을 누적
        prefix_sum += (int(char) - 1)
        
        # 2. 현재까지의 누적 합이 이전에 나온 적이 있는지 확인
        if prefix_sum in counts:
            # 이전에 n번 나왔다면, 현재 지점과 짝을 이룰 수 있는 구간이 n개 존재함
            total_cases += counts[prefix_sum]
            counts[prefix_sum] += 1
        else:
            counts[prefix_sum] = 1
            
    print(total_cases)

if __name__ == "__main__":
    solve()

############################################################################################



