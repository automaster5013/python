import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    # 세그먼트 트리 크기 설정 (N보다 큰 가장 가까운 2의 거듭제곱)
    size = 1
    while size < N:
        size *= 2
    
    # 트리 초기화 (1-based index)
    tree = [0] * (2 * size)
    
    # 1. 트리 리프 노드에 데이터 채우기
    for i in range(N):
        tree[size + i] = int(input_data[2 + i])
    
    # 2. 트리 구축 (부모 노드 = 두 자식 중 최댓값)
    for i in range(size - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    
    # 3. 질의 처리 (비재귀 방식)
    results = []
    ptr = 2 + N
    for _ in range(Q):
        # A, B는 1-indexed
        left = int(input_data[ptr]) + size - 1
        right = int(input_data[ptr + 1]) + size - 1
        ptr += 2
        
        max_val = 0
        while left <= right:
            # 왼쪽 인덱스가 홀수면 현재 노드를 포함하고 오른쪽으로 이동
            if left % 2 == 1:
                if tree[left] > max_val:
                    max_val = tree[left]
                left += 1
            # 오른쪽 인덱스가 짝수면 현재 노드를 포함하고 왼쪽으로 이동
            if right % 2 == 0:
                if tree[right] > max_val:
                    max_val = tree[right]
                right -= 1
            
            # 부모 노드로 이동
            left //= 2
            right //= 2
            
        results.append(str(max_val))
    
    # 한꺼번에 출력하여 속도 향상
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

########################################################################


