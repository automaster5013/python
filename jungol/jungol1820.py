import sys

# 재귀 제한 해제 및 빠른 입력
sys.setrecursionlimit(2000)
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    W = int(data[1])
    
    # 사건 좌표 저장 (0번: 경찰차1 시작점, 1~W번: 사건들, W+1번: 경찰차2 시작점)
    pos = [(1, 1)]
    for i in range(W):
        pos.append((int(data[2 + i*2]), int(data[3 + i*2])))
    pos.append((N, N))
    
    # memo[i][j]: 경찰차1이 pos[i], 경찰차2가 pos[j]에 있을 때 남은 최단 거리
    memo = [[-1] * (W + 2) for _ in range(W + 2)]
    
    def get_dist(idx1, idx2):
        return abs(pos[idx1][0] - pos[idx2][0]) + abs(pos[idx1][1] - pos[idx2][1])

    def find_min_dist(p1, p2):
        # 모든 사건을 다 처리한 경우
        curr_event = max(p1, p2 if p2 <= W else 0) + 1
        if curr_event > W:
            return 0
        
        if memo[p1][p2] != -1:
            return memo[p1][p2]
        
        # 경찰차 1이 이동하는 경우
        dist1 = find_min_dist(curr_event, p2) + get_dist(p1, curr_event)
        
        # 경찰차 2가 이동하는 경우
        # p2가 W+1(초기위치)인 경우 처리 주의
        dist2 = find_min_dist(p1, curr_event) + get_dist(p2, curr_event)
        
        memo[p1][p2] = min(dist1, dist2)
        return memo[p1][p2]

    # 최소 거리 출력
    print(find_min_dist(0, W + 1))

    # 어떤 경찰차가 이동했는지 경로 역추적
    p1, p2 = 0, W + 1
    for k in range(1, W + 1):
        # 경찰차 1이 이동했을 때의 결과와 현재 memo 값이 같은지 확인
        dist_to_event = get_dist(p1, k)
        if memo[p1][p2] == find_min_dist(k, p2) + dist_to_event:
            print(1)
            p1 = k
        else:
            print(2)
            p2 = k

if __name__ == "__main__":
    solve()

############################################################################



