import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 박스 한계 적재량
    boxes = list(map(int, input_data[2:2+N]))
    # 물건 무게
    items = list(map(int, input_data[2+N:2+N+M]))
    
    # 세그먼트 트리 크기 설정 (N보다 큰 가장 가까운 2의 거듭제곱)
    size = 1
    while size < N:
        size *= 2
    
    # 최댓값 세그먼트 트리 초기화
    tree = [0] * (2 * size)
    for i in range(N):
        tree[size + i] = boxes[i]
    
    # 트리 구축 (Bottom-up)
    for i in range(size - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    
    results = []
    
    for w in items:
        # 루트 노드의 최댓값이 물건 무게보다 작으면 담을 수 없음
        if tree[1] < w:
            results.append("0")
            continue
        
        # 조건을 만족하는 가장 왼쪽 박스 찾기 (Top-down search)
        node = 1
        while node < size:
            if tree[2 * node] >= w:
                node = 2 * node
            else:
                node = 2 * node + 1
        
        # 찾은 박스 번호 (1-based index)
        box_idx = node - size + 1
        
        # 실제 박스 범위 내인지 확인
        if box_idx > N:
            results.append("0")
        else:
            results.append(str(box_idx))
            # 박스 용량 갱신 및 트리 업데이트
            tree[node] -= w
            while node > 1:
                node >>= 1
                tree[node] = max(tree[2 * node], tree[2 * node + 1])
                
    # 결과 출력
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()

########################################################################

