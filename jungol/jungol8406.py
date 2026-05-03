import sys

# 재귀 한도 늘리기 (깊은 트리의 경우 필요)
sys.setrecursionlimit(100000)

def solve():
    # 빠른 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 1. 초기화: 모든 학생은 자기 자신이 부모이며, 그룹 크기는 1입니다.
    parent = list(range(n + 1))
    group_size = [1] * (n + 1)
    
    def find(x):
        # 경로 압축(Path Compression) 적용
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        
        # 이미 같은 종교라면 합치지 않음
        if rootX != rootY:
            # 두 집단의 크기를 합산 (rootX를 기준으로 통합)
            parent[rootY] = rootX
            group_size[rootX] += group_size[rootY]

    idx = 2
    output = []
    for _ in range(m):
        command = int(input_data[idx])
        
        if command == 1:
            x = int(input_data[idx + 1])
            y = int(input_data[idx + 2])
            union(x, y)
            idx += 3
        else:
            x = int(input_data[idx + 1])
            # 해당 학생이 속한 그룹의 대표자를 찾아 크기를 출력
            root = find(x)
            output.append(str(group_size[root]))
            idx += 2
            
    # 결과를 한꺼번에 출력하여 속도 향상
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

######################################################################

