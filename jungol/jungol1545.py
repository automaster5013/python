import sys

def solve():
    # 고속 데이터 로드
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    adj = [[] for _ in range(N)]
    ptr = 1
    for i in range(N):
        for j in range(N):
            cost = int(input_data[ptr])
            ptr += 1
            if cost > 0:
                adj[i].append((j, cost))
    
    INF = 10**9
    # dp[mask][city]
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1][0] = 0
    
    # 1. 마스크를 켜진 비트 수(방문한 도시 수)에 따라 그룹화
    # N=19일 때 이 작업은 매우 효율적입니다.
    masks_by_size = [[] for _ in range(N + 1)]
    for i in range(1, 1 << N, 2): # 0번 도시(출발지)가 포함된 홀수 마스크만
        count = bin(i).count('1')
        masks_by_size[count].append(i)
        
    # 2. 도시 수(size) 순서대로 DP 진행
    for size in range(1, N):
        for mask in masks_by_size[size]:
            dp_mask = dp[mask]
            
            for u in range(N):
                d = dp_mask[u]
                if d == INF:
                    continue
                
                # u에서 갈 수 있는 다음 도시(v)만 탐색
                for v, cost in adj[u]:
                    if not (mask & (1 << v)):
                        nxt_mask = mask | (1 << v)
                        new_dist = d + cost
                        
                        # min() 대신 if문 사용 (속도 핵심)
                        if dp[nxt_mask][v] > new_dist:
                            dp[nxt_mask][v] = new_dist
                            
    # 3. 모든 도시 방문 후 회사(0번)로 귀환
    full_mask = (1 << N) - 1
    final_dp = dp[full_mask]
    ans = INF
    
    for i in range(1, N):
        if final_dp[i] != INF:
            # i에서 0으로 돌아오는 비용 확인
            for v, cost in adj[i]:
                if v == 0:
                    res = final_dp[i] + cost
                    if ans > res:
                        ans = res
                    break
                    
    print(ans if ans != INF else 0)

if __name__ == "__main__":
    solve()

##############################################################


