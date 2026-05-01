import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(2000)

def solve():
    # 고속 입출력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    K = int(input_data[0])
    N = int(input_data[1])
    
    # INF는 경로의 최대 길이보다 큰 값으로 설정
    INF = K + 10
    
    # dist[i][j]는 S[j] - S[i]가 가질 수 있는 최댓값을 저장
    dist = [[INF] * (K + 1) for _ in range(K + 1)]
    for i in range(K + 1):
        dist[i][i] = 0
        
    # 기본 제약: 0 <= S[i] - S[i-1] <= 1
    for i in range(K):
        dist[i][i+1] = 1   # S[i+1] - S[i] <= 1
        dist[i+1][i] = 0   # S[i] - S[i+1] <= 0
        
    # 탐사 제약: S[y] - S[x-1] == r
    ptr = 2
    for _ in range(N):
        try:
            x = int(input_data[ptr])
            y = int(input_data[ptr+1])
            r = int(input_data[ptr+2])
            ptr += 3
            # S[y] - S[x-1] <= r
            dist[x-1][y] = min(dist[x-1][y], r)
            # S[y] - S[x-1] >= r  =>  S[x-1] - S[y] <= -r
            dist[y][x-1] = min(dist[y][x-1], -r)
        except IndexError:
            break
            
    # 플로이드-워셜 알고리즘 (O(K^3))
    # 모든 제약 조건을 전파하여 각 구간의 엄격한 상한/하한을 계산
    for k in range(K + 1):
        for i in range(K + 1):
            if dist[i][k] >= INF: continue
            for j in range(K + 1):
                if dist[k][j] >= INF: continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # 모순 체크 (음수 사이클 존재 시 NONE)
    for i in range(K + 1):
        if dist[i][i] < 0:
            print("NONE")
            return

    # s[i]는 누적합 S[i]를 저장
    s = [0] * (K + 1)
    s[0] = 0
    
    def dfs(idx):
        if idx == K + 1:
            return True
        
        # '-' (변화량 0) 시도 후 '#' (변화량 1) 시도
        for val in [0, 1]:
            cur_s = s[idx-1] + val
            
            is_possible = True
            
            # 1. 과거 노드들과의 일관성 체크
            # S[idx] - S[j] <= dist[j][idx] 및 S[j] - S[idx] <= dist[idx][j]를 만족해야 함
            for j in range(idx):
                if cur_s - s[j] > dist[j][idx] or s[j] - cur_s > dist[idx][j]:
                    is_possible = False
                    break
            if not is_possible: continue
            
            # 2. 미래 노드들과의 일관성 체크 (강력한 가지치기)
            # 미래의 모든 S[j]가 현재 결정된 S[idx]와 S[0]의 제약 내에서 존재 가능한지 확인
            for j in range(idx + 1, K + 1):
                # S[j]의 하한선과 상한선이 교차하는지 확인
                lower = max(-dist[j][0], cur_s - dist[j][idx])
                upper = min(dist[0][j], cur_s + dist[idx][j])
                if lower > upper:
                    is_possible = False
                    break
            if not is_possible: continue
            
            s[idx] = cur_s
            if dfs(idx + 1):
                return True
                
        return False

    if dfs(1):
        ans = []
        for i in range(1, K + 1):
            ans.append('#' if s[i] > s[i-1] else '-')
        print("".join(ans))
    else:
        print("NONE")

if __name__ == "__main__":
    solve()

##########################################################################################

