import sys

def solve():
    # 데이터 입력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0]) # 최대 주행 거리
    N = int(input_data[1]) # 정비소 개수
    
    # 인접 정비소 사이의 거리 (N+1개) -> 누적 거리로 변환
    inter_dists = list(map(int, input_data[2:N+3]))
    pos = [0] * (N + 2)
    for i in range(1, N + 2):
        pos[i] = pos[i-1] + inter_dists[i-1]
        
    # 각 정비소 정비 시간 (N개) + 도착점(0)
    times = [0] + list(map(int, input_data[N+3:])) + [0]
    
    # DP 테이블 및 경로 추적 배열 초기화
    inf = float('inf')
    dp = [inf] * (N + 2)
    prev = [-1] * (N + 2)
    
    dp[0] = 0 # 출발점
    
    # DP 수행
    for i in range(1, N + 2):
        for j in range(i):
            # j번 정비소에서 i번 정비소까지 갈 수 있는지 확인
            if pos[i] - pos[j] <= L:
                cost = dp[j] + times[i]
                if cost < dp[i]:
                    dp[i] = cost
                    prev[i] = j
                    
    # 결과 출력
    if dp[N+1] == 0:
        print(0)
    else:
        print(dp[N+1])
        
        # 경로 역추적
        path = []
        curr = prev[N+1]
        while curr > 0:
            path.append(curr)
            curr = prev[curr]
        
        path.reverse()
        print(len(path))
        print(*(path))

if __name__ == "__main__":
    solve()

###################################################################

