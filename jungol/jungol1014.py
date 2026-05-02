import sys

def solve():
    # 마법의 두루마리, 악마의 돌다리, 천사의 돌다리 문자열 입력
    scroll = sys.stdin.readline().strip()
    devil = sys.stdin.readline().strip()
    angel = sys.stdin.readline().strip()
    
    if not scroll or not devil:
        return
    
    n = len(scroll)
    m = len(devil)
    
    # dp[k][type][pos] 초기화
    # type 0: 악마, type 1: 천사
    dp = [[[0] * m for _ in range(2)] for _ in range(n)]
    
    # 기저 사례: 두루마리의 첫 번째 문자 처리
    for i in range(m):
        if devil[i] == scroll[0]:
            dp[0][0][i] = 1
        if angel[i] == scroll[0]:
            dp[0][1][i] = 1
            
    # DP 전이 진행
    for k in range(1, n):
        target = scroll[k]
        for i in range(m):
            # 1. 현재 악마의 돌다리 i번 돌을 밟으려는 경우
            if devil[i] == target:
                # 이전에 천사의 돌다리 j < i번 위치에서 넘어와야 함
                for j in range(i):
                    dp[k][0][i] += dp[k-1][1][j]
            
            # 2. 현재 천사의 돌다리 i번 돌을 밟으려는 경우
            if angel[i] == target:
                # 이전에 악마의 돌다리 j < i번 위치에서 넘어와야 함
                for j in range(i):
                    dp[k][1][i] += dp[k-1][0][j]
                    
    # 마지막 문자에 도달한 모든 경로의 수 합산
    ans = 0
    for i in range(m):
        ans += dp[n-1][0][i]
        ans += dp[n-1][1][i]
        
    print(ans)

if __name__ == "__main__":
    solve()

######################################################################

