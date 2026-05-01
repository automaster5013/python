import sys

def solve():
    # 고속 입력을 사용하여 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr])  # 학생 수
    M = int(input_data[ptr + 1])  # 선물 수
    ptr += 2
    
    # 인접 리스트 생성 (각 학생이 좋아하는 선물의 번호를 저장)
    adj = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        s_count = int(input_data[ptr])
        ptr += 1
        for _ in range(s_count):
            adj[i].append(int(input_data[ptr]))
            ptr += 1
            
    # match[i]: i번 선물을 가져간 학생의 번호를 저장 (-1은 배정 안 됨)
    match = [-1] * (M + 1)
    
    # DFS를 이용한 이분 매칭 함수
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                # 선물이 비어있거나, 이미 배정된 학생이 다른 선물을 찾을 수 있는 경우
                if match[v] == -1 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    count = 0
    for i in range(1, N + 1):
        # 각 학생마다 방문 여부 초기화
        visited = [False] * (M + 1)
        if dfs(i, visited):
            count += 1
            
    # 최대로 연결된 수 출력
    print(count)

if __name__ == "__main__":
    solve()

######################################################################################

