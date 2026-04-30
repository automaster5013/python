import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    fixed_seats = [int(x) for x in input_data[2:]]
    
    # 2. 피보나치 수열 미리 계산 (최대 40까지)
    # f[k]: 연속된 k개의 좌석에 앉는 방법의 수
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i-1] + f[i-2]
        
    # 3. 고정석 사이의 구간 길이 구하기
    segments = []
    last_pos = 0
    
    for seat in fixed_seats:
        # 고정석 바로 직전까지의 자유석 구간 길이
        segments.append(seat - last_pos - 1)
        last_pos = seat
        
    # 마지막 고정석 이후부터 끝까지의 구간 추가
    segments.append(n - last_pos)
    
    # 4. 각 구간의 경우의 수를 모두 곱함
    ans = 1
    for length in segments:
        ans *= f[length]
        
    print(ans)

if __name__ == "__main__":
    solve()

#######################################################

