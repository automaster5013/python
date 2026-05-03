import sys
from collections import deque

def solve():
    # 빠른 입력을 위해 stdin.readline 사용
    line = sys.stdin.readline().split()
    if not line:
        return
    n, k = map(int, line)
    
    # 이진 코드를 정수로 변환하여 인덱스와 함께 저장
    code_to_idx = {}
    indices_to_int = [0] * (n + 1)
    
    for i in range(1, n + 1):
        code_str = sys.stdin.readline().strip()
        val = int(code_str, 2)
        code_to_idx[val] = i
        indices_to_int[i] = val
        
    # BFS를 위한 초기 설정
    # parent[i]: i번 노드에 도달하기 전의 노드 번호
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    queue = deque([1])
    visited[1] = True
    
    # 1번 노드에서 시작하는 BFS 수행
    while queue:
        u_idx = queue.popleft()
        u_val = indices_to_int[u_idx]
        
        # 현재 값에서 비트 하나를 뒤집어 인접한 코드가 있는지 확인
        for bit in range(k):
            v_val = u_val ^ (1 << bit)
            if v_val in code_to_idx:
                v_idx = code_to_idx[v_val]
                if not visited[v_idx]:
                    visited[v_idx] = True
                    parent[v_idx] = u_idx
                    queue.append(v_idx)
    
    # 질의 처리
    try:
        m_line = sys.stdin.readline().strip()
        if not m_line:
            return
        m = int(m_line)
    except ValueError:
        return
    
    for _ in range(m):
        target = int(sys.stdin.readline().strip())
        
        # 경로가 존재하지 않는 경우
        if not visited[target]:
            print("-1")
        else:
            # parent 배열을 이용해 경로 역추적
            path = []
            curr = target
            while curr != -1:
                path.append(curr)
                curr = parent[curr]
            # 역순으로 정렬하여 출력
            print(*(path[::-1]))

if __name__ == "__main__":
    solve()

#################################################################



