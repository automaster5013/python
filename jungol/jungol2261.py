import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, k = int(input_data[0]), int(input_data[1])
    codes = input_data[2:2+n]
    start_idx = int(input_data[2+n]) - 1
    target_idx = int(input_data[3+n]) - 1

    # 2. 해밍 거리가 1인 노드들끼리 인접 리스트 구성
    adj = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # 두 코드 사이의 서로 다른 비트 수 계산
            diff_count = 0
            for bit in range(k):
                if codes[i][bit] != codes[j][bit]:
                    diff_count += 1
                if diff_count > 1: # 거리가 1을 넘으면 중단
                    break
            
            if diff_count == 1:
                adj[i].append(j)
                adj[j].append(i)

    # 3. BFS 탐색
    queue = deque([start_idx])
    visited = [False] * n
    parent = [-1] * n # 경로 역추적용
    
    visited[start_idx] = True
    
    found = False
    while queue:
        curr = queue.popleft()
        
        if curr == target_idx:
            found = True
            break
            
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                queue.append(neighbor)

    # 4. 결과 출력
    if found:
        path = []
        curr = target_idx
        while curr != -1:
            path.append(curr + 1) # 1-based 인덱스로 저장
            curr = parent[curr]
        
        # 역추적했으므로 뒤집어서 출력
        print(*(path[::-1]))
    else:
        print("-1")

if __name__ == "__main__":
    solve()

#################################################################

