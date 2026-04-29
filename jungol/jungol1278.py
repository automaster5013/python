import sys

def solve():
    # 1. 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 보석의 개수
    w_limit = int(input_data[1]) # 배낭의 최대 용량
    
    # 2. DP 테이블 초기화 (용량 W까지 담을 수 있도록 설정)
    dp = [0] * (w_limit + 1)
    
    ptr = 2
    # 3. 보석을 하나씩 확인하며 DP 테이블 갱신
    for _ in range(n):
        weight = int(input_data[ptr])
        value = int(input_data[ptr+1])
        ptr += 2
        
        # 0/1 배낭 문제이므로 무게를 뒤에서부터 갱신 (중복 사용 방지)
        for j in range(w_limit, weight - 1, -1):
            if dp[j - weight] + value > dp[j]:
                dp[j] = dp[j - weight] + value
                
    # 4. 결과 출력
    print(dp[w_limit])

if __name__ == "__main__":
    solve()

#######################################################################

