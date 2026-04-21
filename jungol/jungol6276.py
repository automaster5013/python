import sys

def solve():
    # 데이터 입력 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    fires = []
    
    idx = 1
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        fires.append((a, b))
        idx += 2
    
    # 정렬 기준: b_i * a_j < b_j * a_i 
    # 파이썬의 sort는 유연하므로 key에 커스텀 비교 로직을 적용하거나 
    # 비율을 사용하되 a=0 처리를 위해 작은 값을 더해줄 수 있습니다.
    # 여기서는 정렬을 위해 b/a 값이 작은 순서대로 정렬합니다. 
    # a가 0인 경우는 b/a가 무한대가 되므로 가장 마지막에 처리됩니다.
    fires.sort(key=lambda x: x[1] / x[0] if x[0] != 0 else float('inf'))
    
    current_time = 0
    mod = 40000
    
    for a, b in fires:
        # t초 후에 도착했을 때 진압 시간: at + b
        duration = (a * current_time + b)
        current_time = (current_time + duration) % mod
        
    print(current_time)

if __name__ == "__main__":
    solve()



