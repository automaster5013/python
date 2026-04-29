import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    c_list = list(map(int, input_data[3:]))
    
    # 마법력의 최대 예상 범위 설정
    max_mana = k + (n * m)
    
    # dp[j] : 현재 마법력이 j일 때 벌 수 있는 최대 금액
    # -1은 도달할 수 없는 상태를 의미
    dp = [-1] * (max_mana + 1)
    dp[k] = 0
    
    curr_limit = k # 현재 탐색할 마법력의 유효 범위 (계산 최적화)
    
    # 2. DP 진행
    for c in c_list:
        new_dp = [-1] * (max_mana + 1)
        
        # 현재 가능한 마법력 범위 내에서만 탐색
        for j in range(curr_limit + 1):
            if dp[j] == -1:
                continue
            
            # 선택 1: 수리하기
            if j >= c:
                if dp[j] + c > new_dp[j - c]:
                    new_dp[j - c] = dp[j] + c
            
            # 선택 2: 명상하기
            next_mana = j + m
            if dp[j] > new_dp[next_mana]:
                new_dp[next_mana] = dp[j]
        
        dp = new_dp
        curr_limit += m # 명상으로 인해 가능한 최대 마법력이 매턴 M씩 증가
        
    # 3. 결과 출력
    print(max(dp))

if __name__ == "__main__":
    solve()

##########################################################################

