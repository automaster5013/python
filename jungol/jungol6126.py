import sys

def solve():
    # 고속 입력을 통해 모든 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    N = int(input_data[idx])
    idx += 1
    
    # 시간의 최대 범위가 1,000,000이므로 넉넉하게 배열 크기 설정
    MAX_TIME = 1000000
    diff = [0] * (MAX_TIME + 2)
    
    # 1. 차분 배열에 기록 (O(N))
    for _ in range(N):
        s = int(input_data[idx])
        e = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        diff[s] += c
        if e + 1 <= MAX_TIME:
            diff[e + 1] -= c
            
    # 2. 누적 합을 구하여 각 시간대의 인원수 확정 (O(MAX_TIME))
    # diff 배열 자체를 누적 합 배열로 변환하여 메모리 절약
    for i in range(1, MAX_TIME + 1):
        diff[i] += diff[i-1]
        
    # 3. 쿼리 처리 (O(Q))
    Q = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(Q):
        t = int(input_data[idx])
        idx += 1
        results.append(str(diff[t]))
        
    # 결과 일괄 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

###############################################################


