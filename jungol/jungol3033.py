import heapq
import sys
import array

def solve():
    # 전체 입력을 한 번에 읽어 처리 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N, M, X = map(int, input_data[:3])
    ptr = 3
    
    T = [int(input_data[ptr + i]) for i in range(N)]
    ptr += N
    
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u = int(input_data[ptr]) - 1
        v = int(input_data[ptr+1]) - 1
        d = int(input_data[ptr+2])
        ptr += 3
        adj[u].append((v, d))
        adj[v].append((u, d))
        
    TWO_X = 2 * X
    INF = 10**9 # 32비트 정수 범위 내의 충분히 큰 값
    
    # 메모리 효율을 위해 array.array('i') 사용 (4 bytes per int)
    dist = array.array('i', [INF] * (N * (TWO_X + 1)))
    
    # 시작점 설정: 방 1(index 0)은 추운 방이므로 s=0
    dist[0] = 0 
    pq = [(0, 0, 0)] # (누적 시간, 현재 방 index, 상태 s)
    
    heappop = heapq.heappop
    heappush = heapq.heappush
    
    while pq:
        d, u, s = heappop(pq)
        
        u_offset = u * (TWO_X + 1)
        if d > dist[u_offset + s]: continue
            
        for v, w in adj[u]:
            tv = T[v]
            ns = -1 # 다음 상태(Next State)
            
            if tv == 0: # 추운 방으로 이동 시
                if s <= X or (TWO_X - s) + w >= X:
                    ns = 0
            elif tv == 2: # 더운 방으로 이동 시
                if s >= X or s + w >= X:
                    ns = TWO_X
            else: # 적당한 온도 방으로 이동 시
                if s <= X:
                    ns = s + w
                    if ns > X: ns = X
                else:
                    ns = s - w
                    if ns < X: ns = X
            
            if ns != -1:
                v_offset = v * (TWO_X + 1)
                target_idx = v_offset + ns
                if d + w < dist[target_idx]:
                    dist[target_idx] = d + w
                    heappush(pq, (d + w, v, ns))
                    
    # N번 방(index N-1)에 도달한 모든 상태 중 최솟값 출력
    ans = INF
    last_room_offset = (N - 1) * (TWO_X + 1)
    for s in range(TWO_X + 1):
        if dist[last_room_offset + s] < ans:
            ans = dist[last_room_offset + s]
            
    sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()

###################################################################

