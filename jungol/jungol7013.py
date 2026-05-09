import sys

def solve():
    # 모든 입력을 한 번에 읽어와서 파싱을 고속화합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 캠핑장 격자 맵 정보
    grid = input_data[2:2+N]
    
    Q_idx = 2 + N
    Q = int(input_data[Q_idx])
    
    queries = []
    idx = Q_idx + 1
    for _ in range(Q):
        # 파이썬 리스트 접근을 위해 좌표를 0-based index로 변경합니다.
        queries.append((int(input_data[idx]) - 1, int(input_data[idx+1]) - 1))
        idx += 2
        
    # 1. DP로 각 셀을 우하단으로 하는 최대 정사각형 한 변의 길이 구하기
    D = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                if i == 0 or j == 0:
                    D[i][j] = 1
                else:
                    D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1
            else:
                D[i][j] = 0
                
    max_size = min(N, M)
    # 크기별로 버킷을 만들어 정렬(O(N*M))
    buckets = [[] for _ in range(max_size + 1)]
    
    # 2. 어떤 정사각형에도 완전히 속하지 않는 극대 정사각형(Maximal Square) 추출
    for i in range(N):
        for j in range(M):
            V = D[i][j]
            if V == 0:
                continue
            
            is_maximal = True
            # 오른쪽, 아래쪽, 우측대각선 아래쪽으로 1칸이라도 확장되는 더 큰 정사각형이 있는지 확인
            if i + 1 < N and D[i+1][j] >= V + 1:
                is_maximal = False
            elif j + 1 < M and D[i][j+1] >= V + 1:
                is_maximal = False
            elif i + 1 < N and j + 1 < M and D[i+1][j+1] >= V + 1:
                is_maximal = False
                
            if is_maximal:
                # 메모리 절약을 위해 1차원 좌표로 압축하여 삽입
                buckets[V].append(i * M + j)
                
    # 3. 큰 정사각형부터 우선적으로 빈 캠핑장에 채워넣기 (DSU 활용)
    ans = [[0] * M for _ in range(N)]
    parent = [list(range(M + 1)) for _ in range(N)]
    
    for V in range(max_size, 0, -1):
        for val in buckets[V]:
            x = val // M
            y = val % M
            
            r_start = x - V + 1
            c_start = y - V + 1
            
            for r in range(r_start, x + 1):
                p = parent[r]
                curr = c_start
                
                # 아직 V값이 할당 안된 가장 가까운 다음 열을 찾습니다 (Find)
                while p[curr] != curr:
                    p[curr] = p[p[curr]]
                    curr = p[curr]
                
                # 범위를 벗어나지 않는다면 값을 갱신하고 우측으로 점프시킵니다
                while curr <= y:
                    ans[r][curr] = V
                    nxt = curr + 1
                    while p[nxt] != nxt:
                        p[nxt] = p[p[nxt]]
                        nxt = p[nxt]
                    p[curr] = nxt
                    curr = nxt

    # 질의들에 대해 넓이(= 길이의 제곱) 반환
    out = []
    for r, c in queries:
        a = ans[r][c]
        out.append(str(a * a))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

###############################################################################


