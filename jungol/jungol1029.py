import sys

# 재귀 깊이 제한 해제 (N이 100,000이므로 넉넉하게 설정)
sys.setrecursionlimit(200000)

def solve():
    # 고속 입력을 위해 한꺼번에 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    adj = []
    ptr = 1
    for _ in range(n):
        l = int(input_data[ptr])
        r = int(input_data[ptr+1])
        adj.append((l, r))
        ptr += 2
    
    # get_info(u)는 (min_depth, max_depth, swaps)를 반환함
    def get_info(u):
        if u == -1: # 장난감(리프 노드)인 경우
            return (0, 0, 0)
        
        l_child, r_child = adj[u-1]
        l_min, l_max, l_s = get_info(l_child)
        r_min, r_max, r_s = get_info(r_child)
        
        # 하위 노드에서 이미 불가능하다고 판정된 경우
        if l_min == -1 or r_min == -1:
            return (-1, -1, -1)
        
        # 현재 막대를 거치므로 깊이 1씩 증가
        l_min += 1; l_max += 1
        r_min += 1; r_max += 1
        
        cur_min = min(l_min, r_min)
        cur_max = max(l_max, r_max)
        
        # 조건 (i): 레벨 차이가 1을 초과하면 불가능
        if cur_max - cur_min > 1:
            return (-1, -1, -1)
        
        # Case 1: 양쪽 서브트리의 모든 장난감 깊이가 각각 일정한 경우
        if l_min == l_max and r_min == r_max:
            if l_min == r_min: # 깊이가 모두 같으면 교체 불필요
                return (cur_min, cur_max, l_s + r_s)
            if l_min > r_min: # 왼쪽이 더 깊음 (d+1, d) -> 정상
                return (cur_min, cur_max, l_s + r_s)
            else: # 오른쪽이 더 깊음 (d, d+1) -> 교체 필요
                return (cur_min, cur_max, l_s + r_s + 1)
        
        # Case 2: 왼쪽 서브트리는 깊이가 섞여 있고, 오른쪽은 일정한 경우
        if l_min != l_max and r_min == r_max:
            # L = {d, d+1}, R = {d} -> (d+1...d), (d) -> 정상
            if l_min == r_min:
                return (cur_min, cur_max, l_s + r_s)
            # L = {d, d+1}, R = {d+1} -> (d+1...d), (d+1) -> 교체 필요 (R이 왼쪽으로)
            if l_max == r_min:
                return (cur_min, cur_max, l_s + r_s + 1)
        
        # Case 3: 왼쪽 서브트리는 일정하고, 오른쪽은 깊이가 섞여 있는 경우
        if l_min == l_max and r_min != r_max:
            # L = {d+1}, R = {d, d+1} -> (d+1), (d+1...d) -> 정상
            if l_min == r_max:
                return (cur_min, cur_max, l_s + r_s)
            # L = {d}, R = {d, d+1} -> (d), (d+1...d) -> 교체 필요 (R이 왼쪽으로)
            if l_min == r_min:
                return (cur_min, cur_max, l_s + r_s + 1)
        
        # 그 외 (양쪽 모두 섞여 있거나 배치 불가능한 경우)
        return (-1, -1, -1)

    result = get_info(1)
    # 불가능하면 -1, 가능하면 최소 교체 횟수 출력
    print(result[2])

if __name__ == "__main__":
    solve()

######################################################################################

