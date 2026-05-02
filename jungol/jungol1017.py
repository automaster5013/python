import sys

def solve():
    # 입력을 빠르게 읽어옵니다.
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    dist = []
    stre = []
    carr = []
    
    idx = 1
    for _ in range(n):
        dist.append(int(data[idx]))
        stre.append(int(data[idx+1]))
        carr.append(int(data[idx+2]))
        idx += 3
        
    # dp[i][j] : 가는 경로가 i에 있고, 오는 경로가 j에 있는 경우의 수
    # 모듈러 1,000 연산을 적용합니다.
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    
    # 1번부터 n-2번 섬까지 순차적으로 처리하여 정점 불일치를 보장합니다.
    for k in range(1, n - 1):
        dk, sk, ck = dist[k], stre[k], carr[k]
        
        # k를 가는 경로(Path A)에 추가하는 경우: i -> k
        for i in range(k):
            if dk - dist[i] <= stre[i]:
                # j는 k보다 작아야 하므로 k번 섬은 이전에 사용된 적이 없음이 보장됩니다.
                row_i = dp[i]
                row_k = dp[k]
                for j in range(k):
                    if row_i[j]:
                        row_k[j] = (row_k[j] + row_i[j]) % 1000
                        
        # k를 오는 경로(Path B)에 추가하는 경우: k -> j
        # 공주를 데리고 올 수 있는 섬(ck == 1)만 가능합니다.
        if ck == 1:
            for j in range(k):
                if dk - dist[j] <= sk:
                    for i in range(k):
                        if dp[i][j]:
                            dp[i][k] = (dp[i][k] + dp[i][j]) % 1000
                            
    # 마지막 후퍼 섬(n-1)에서 두 경로를 연결합니다.
    ans = 0
    dn_1 = dist[n-1]
    sn_1 = stre[n-1] # 후퍼 섬의 스프링 세기
    
    for i in range(n - 1):
        for j in range(n - 1):
            if dp[i][j]:
                # 가는 경로 마무리: i -> n-1
                if dn_1 - dist[i] <= stre[i]:
                    # 오는 경로 시작: n-1 -> j
                    if dn_1 - dist[j] <= sn_1:
                        ans = (ans + dp[i][j]) % 1000
                        
    # 최종 결과 출력 (1,000으로 나눈 나머지)
    sys.stdout.write(str(ans % 1000) + '\n')

if __name__ == "__main__":
    solve()

#####################################################################

