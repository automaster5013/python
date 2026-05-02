import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    Q = int(input_data[ptr]); ptr += 1
    
    # 세그먼트 트리 크기 설정 (N보다 큰 가장 가까운 2의 거듭제곱)
    size = 1
    while size < N:
        size *= 2
        
    # 최댓값 트리와 최솟값 트리 초기화
    # 최댓값은 0, 최솟값은 가능한 최대 키(1,000,000)보다 큰 값으로 설정
    INF = 1000001
    max_tree = [0] * (2 * size)
    min_tree = [INF] * (2 * size)
    
    # 리프 노드에 소들의 키 입력
    for i in range(N):
        val = int(input_data[ptr])
        ptr += 1
        max_tree[size + i] = val
        min_tree[size + i] = val
        
    # 트리 구축 (Bottom-up)
    for i in range(size - 1, 0, -1):
        # 부모 노드 = 왼쪽 자식과 오른쪽 자식의 비교값
        max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])
        min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
        
    results = []
    # Q개의 질의 처리
    for _ in range(Q):
        A = int(input_data[ptr]); ptr += 1
        B = int(input_data[ptr]); ptr += 1
        
        # 1-indexed인 소의 번호를 0-indexed 세그먼트 인덱스로 변환
        left = size + A - 1
        right = size + B - 1
        
        curr_max = 0
        curr_min = INF
        
        # 비재귀 구간 질의
        while left <= right:
            if left % 2 == 1: # 왼쪽 인덱스가 홀수면 독립 노드
                if max_tree[left] > curr_max: curr_max = max_tree[left]
                if min_tree[left] < curr_min: curr_min = min_tree[left]
                left += 1
            if right % 2 == 0: # 오른쪽 인덱스가 짝수면 독립 노드
                if max_tree[right] > curr_max: curr_max = max_tree[right]
                if min_tree[right] < curr_min: curr_min = min_tree[right]
                right -= 1
            left //= 2
            right //= 2
            
        results.append(str(curr_max - curr_min))
        
    # 결과 일괄 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

##############################################################################


