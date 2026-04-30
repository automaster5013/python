import sys

# 1. 재귀 한도 늘리기 (N이 100,000이므로 넉넉히 설정)
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    # 2. 방의 수 N, 문의 수 M 입력
    try:
        line = input().split()
        if not line: return
        n, m = map(int, line)
    except ValueError:
        return

    # 3. 인접 리스트 생성
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # 4. "작은 번호의 방부터" 가야 하므로 각 인접 리스트 정렬
    for i in range(1, n + 1):
        adj[i].sort()

    visited = [False] * (n + 1)
    result = []

    # 5. DFS 탐색 정의
    def dfs(curr):
        visited[curr] = True
        result.append(curr) # 방문 순서 기록
        
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                dfs(neighbor)
                # 왔던 곳으로 되돌아오는 과정은 재귀 함수 종료로 자연스럽게 구현됨

    # 6. 1번 방에서 탐색 시작
    dfs(1)

    # 7. 결과 출력
    print(*(result))

if __name__ == "__main__":
    solve()

###################################################################################

