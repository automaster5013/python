import sys

def solve():
    # 입력 받기
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    N = int(input_data[0])
    K = int(input_data[1])
    
    MOD = 1000000009
    
    # 상태별 DP 초기값 (길이 0일 때 상태 0은 1개)
    dp0 = 1
    dp1 = dp2 = dp3 = dp4 = dp5 = dp6 = 0
    
    for _ in range(N):
        sn = (dp0 + dp1 + dp2 + dp3 + dp4 + dp5 + dp6) % MOD
        
        # 다음 상태 계산
        ndp1 = (dp0 + dp1 + dp3 + dp5 + dp6) % MOD
        ndp2 = dp1
        ndp3 = (dp2 + dp4) % MOD
        ndp4 = dp3
        ndp5 = dp2
        ndp6 = dp5
        # 문자 A, B, C 중 상태 0으로 가는 경우와 나머지 K-3개 문자 합산
        ndp0 = (sn * (K - 2) + dp0) % MOD
        
        # 상태 업데이트
        dp0, dp1, dp2, dp3, dp4, dp5, dp6 = ndp0, ndp1, ndp2, ndp3, ndp4, ndp5, ndp6
        
    # 최종 결과 출력 (모든 안전한 상태의 합)
    result = (dp0 + dp1 + dp2 + dp3 + dp4 + dp5 + dp6) % MOD
    print(result)

if __name__ == '__main__':
    solve()

#######################################################################################

