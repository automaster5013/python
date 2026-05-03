import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0]) # 노드 개수
    K = int(input_data[1]) # 연산 개수
    
    # parent[i]: i의 부모, color[i]: (i, parent[i]) 에지의 색
    # 초기 상태: 0이 루트, 나머지는 0의 자식, 색은 0
    parent = [0] * N
    color = [0] * N
    
    # LCA 탐색 시 방문 체크를 위한 배열 (초기화 비용을 줄이기 위해 타임스탬프 사용)
    visited_version = [0] * N
    current_version = 0
    
    ptr = 2
    results = []
    
    for _ in range(K):
        op = int(input_data[ptr])
        
        if op == 1: # paint(a, b, c)
            a, b, c = int(input_data[ptr+1]), int(input_data[ptr+2]), int(input_data[ptr+3])
            ptr += 4
            
            # 1. LCA 찾기
            current_version += 1
            lca = -1
            
            # a에서 위로 1000단계까지 마킹
            curr = a
            for _ in range(1001):
                visited_version[curr] = current_version
                if curr == 0: break
                curr = parent[curr]
            
            # b에서 위로 올라가며 처음 마킹된 곳이 LCA
            curr = b
            for _ in range(1001):
                if visited_version[curr] == current_version:
                    lca = curr
                    break
                curr = parent[curr]
            
            # 2. 경로 색칠 (a -> LCA, b -> LCA)
            curr = a
            while curr != lca:
                color[curr] = c
                curr = parent[curr]
            curr = b
            while curr != lca:
                color[curr] = c
                curr = parent[curr]
                
        elif op == 2: # move(a, b)
            a, b = int(input_data[ptr+1]), int(input_data[ptr+2])
            ptr += 3
            # 부모만 변경, 에지 색깔은 유지됨
            parent[a] = b
            
        elif op == 3: # count(a, b)
            a, b = int(input_data[ptr+1]), int(input_data[ptr+2])
            ptr += 3
            
            # 1. LCA 찾기
            current_version += 1
            lca = -1
            curr = a
            for _ in range(1001):
                visited_version[curr] = current_version
                if curr == 0: break
                curr = parent[curr]
            curr = b
            for _ in range(1001):
                if visited_version[curr] == current_version:
                    lca = curr
                    break
                curr = parent[curr]
            
            # 2. 고유 색깔 카운트
            distinct_colors = set()
            curr = a
            while curr != lca:
                distinct_colors.add(color[curr])
                curr = parent[curr]
            curr = b
            while curr != lca:
                distinct_colors.add(color[curr])
                curr = parent[curr]
            
            results.append(str(len(distinct_colors)))

    # 결과 일괄 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

########################################################################



