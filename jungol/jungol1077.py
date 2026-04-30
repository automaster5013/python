import sys

def solve():
    # 1. 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 보석의 종류 수
    w_limit = int(input_data[1]) # 배낭의 최대 용량
    
    # 2. DP 테이블 초기화
    dp = [0] * (w_limit + 1)
    
    ptr = 2
    # 3. 각 보석 종류에 대해 처리
    for _ in range(n):
        weight = int(input_data[ptr])
        value = int(input_data[ptr+1])
        ptr += 2
        
        # 무한 배낭 문제의 핵심: 무게를 '앞에서부터' 갱신
        # 이렇게 하면 같은 보석을 여러 번 담는 것이 허용됩니다.
        for j in range(weight, w_limit + 1):
            if dp[j - weight] + value > dp[j]:
                dp[j] = dp[j - weight] + value
                
    # 4. 결과 출력
    print(dp[w_limit])

if __name__ == "__main__":
    solve()

################################################################

