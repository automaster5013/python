import sys
from collections import deque
import array

def solve():
    # 모든 입력을 토큰 단위로 읽어 들임
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    ptr = 0
    while ptr < len(tokens):
        n = int(tokens[ptr])
        m = int(tokens[ptr+1])
        ptr += 2
        
        if n == 0 and m == 0:
            break
            
        adj = [0] * n
        for _ in range(m):
            u = int(tokens[ptr])
            v = int(tokens[ptr+1])
            ptr += 2
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
        
        # 연결 그래프에서 간선의 수가 정점 수 이상이면 사이클이 존재함
        if m >= n:
            print("Impossible")
            continue
            
        # 초기 상태: 모든 나무에 로봇이 있을 수 있음
        start = (1 << n) - 1
        queue = deque([start])
        
        # 메모리 효율을 위해 array.array 사용 (부모 상태 및 수행한 사격 번호 기록)
        parent_state = array.array('I', [0] * (1 << n))
        parent_action = array.array('b', [-1] * (1 << n))
        visited = bytearray(1 << n)
        
        visited[start] = 1
        found = False
        
        # 비트마스크 변환 최적화를 위해 절반씩 미리 계산
        split = n // 2
        low_mask = (1 << split) - 1
        move_low = [0] * (1 << split)
        for i in range(1 << split):
            for bit in range(split):
                if (i >> bit) & 1:
                    move_low[i] |= adj[bit]
        
        move_high = [0] * (1 << (n - split))
        for i in range(1 << (n - split)):
            for bit in range(n - split):
                if (i >> bit) & 1:
                    move_high[i] |= adj[bit + split]
        
        # BFS 탐색
        while queue:
            curr = queue.popleft()
            
            if curr == 0:
                found = True
                break
            
            for t in range(n):
                rem = curr & ~(1 << t) # 나무 t 사격
                if rem == 0:
                    nxt = 0
                else:
                    # 로봇이 이웃 나무로 이동 (미리 계산된 테이블 사용)
                    nxt = move_low[rem & low_mask] | move_high[rem >> split]
                
                if not visited[nxt]:
                    visited[nxt] = 1
                    parent_state[nxt] = curr
                    parent_action[nxt] = t
                    queue.append(nxt)
        
        if found:
            res = []
            curr = 0
            while curr != start:
                res.append(parent_action[curr])
                curr = parent_state[curr]
            res.reverse()
            print(f"{len(res)}:", *res)
        else:
            print("Impossible")

if __name__ == "__main__":
    solve()

##################################################################################3

