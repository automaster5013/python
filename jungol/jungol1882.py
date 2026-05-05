import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(100000)

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0]) # 격자 크기
    K = int(input_data[1]) # 소행성 개수
    
    # 행에서 열로 연결되는 인접 리스트
    adj = [[] for _ in range(N + 1)]
    
    idx = 2
    for _ in range(K):
        r = int(input_data[idx])
        c = int(input_data[idx+1])
        adj[r].append(c) # r행과 c열 연결
        idx += 2
        
    # 각 열이 어떤 행과 매칭되어 있는지 기록
    match = [0] * (N + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                # 해당 열이 아직 매칭되지 않았거나, 
                # 기존 매칭된 행이 다른 열과 매칭 가능하다면
                if match[v] == 0 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    count = 0
    for i in range(1, N + 1):
        # 방문 체크 배열 초기화
        visited = [False] * (N + 1)
        if dfs(i, visited):
            count += 1
            
    # 최대 매칭의 수가 곧 최소 무기 사용 횟수임
    print(count)

if __name__ == "__main__":
    solve()

####################################################################

