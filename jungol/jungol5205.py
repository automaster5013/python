import sys
from collections import deque

def solve():
    # 입력을 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))  # 완제품 번호
    m = int(next(it))  # 관계의 개수
    
    # 연결 리스트와 진입 차수 배열 초기화
    # adj[i]: i번 부품을 재료로 사용하는 상위 부품들의 목록
    adj = [[] for _ in range(n + 1)]
    # in_degree[i]: i번 부품을 만들기 위해 필요한 하위 재료의 가짓수
    in_degree = [0] * (n + 1)
    # 기본 부품 여부 판별 (조립법 X에 한 번도 등장하지 않으면 기본 부품)
    is_not_basic = [False] * (n + 1)
    
    for _ in range(m):
        x, y, k = int(next(it)), int(next(it)), int(next(it))
        # y(하위) -> x(상위) 관계로 저장
        adj[y].append((x, k))
        # x를 만드는 데 필요한 재료 가짓수 증가
        in_degree[x] += 1
        is_not_basic[x] = True
        
    # needed[i][j]: i번 부품을 하나 만드는 데 필요한 기본 부품 j의 개수
    needed = [[0] * (n + 1) for _ in range(n + 1)]
    
    queue = deque()
    
    # 1. 진입 차수가 0인 '기본 부품'들을 큐에 넣고 초기화
    for i in range(1, n + 1):
        if not is_not_basic[i]:
            needed[i][i] = 1
            queue.append(i)
            
    # 2. 위상 정렬을 이용해 하위 부품부터 상위 부품으로 수량 전파
    while queue:
        curr = queue.popleft()
        
        # curr 부품을 재료로 사용하는 상위 부품(parent) 확인
        for parent, count in adj[curr]:
            # parent를 만드는 데 필요한 기본 부품 수량 = (curr에 필요한 수량 * 개수)
            for j in range(1, n + 1):
                needed[parent][j] += needed[curr][j] * count
            
            # 상위 부품의 모든 재료가 계산 완료되면 큐에 삽입
            in_degree[parent] -= 1
            if in_degree[parent] == 0:
                queue.append(parent)
                
    # 3. 완제품(n)에 들어가는 기본 부품들만 출력
    for i in range(1, n + 1):
        if not is_not_basic[i] and needed[n][i] > 0:
            print(f"{i} {needed[n][i]}")

if __name__ == "__main__":
    solve()

#####################################################################################


