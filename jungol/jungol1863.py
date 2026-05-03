import sys

# 재귀 깊이 제한을 늘려 깊은 트리 구조에서도 안전하게 동작하도록 합니다.
sys.setrecursionlimit(100000)

def find(parent, x):
    # 경로 압축(Path Compression): 대표 노드를 직접 가리키도록 업데이트
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    # 두 학생의 종교 대표가 다를 경우에만 합치고 True 반환
    if rootX != rootY:
        parent[rootX] = rootY
        return True
    return False

def solve():
    # 대량의 데이터를 빠르게 읽기 위해 sys.stdin.read()를 사용합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 학생 수
    m = int(input_data[1]) # 쌍의 수
    
    # 각 학생의 부모 노드를 저장하는 리스트 (초기값은 자기 자신)
    parent = list(range(n + 1))
    # 초기 종교의 가짓수는 학생 수와 같습니다.
    religions_count = n
    
    idx = 2
    for _ in range(m):
        if idx + 1 >= len(input_data):
            break
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        # 두 집합이 성공적으로 합쳐지면 종교의 수를 1 줄입니다.
        if union(parent, u, v):
            religions_count -= 1
            
    # 최종적으로 계산된 종교의 가짓수를 출력합니다.
    print(religions_count)

if __name__ == "__main__":
    solve()

##########################################################################



