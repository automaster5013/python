import sys
from bisect import bisect_left

def solve():
    # 빠른 입력을 위한 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    wires = []
    idx = 1
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        wires.append((a, b))
        idx += 2
        
    # 1. A 전봇대 위치 기준으로 오름차순 정렬
    wires.sort()
    
    # 2. B 전봇대 위치 값들로 LIS 탐색
    b_values = [w[1] for w in wires]
    tails = []          # LIS를 유지하기 위한 배열
    pos_in_lis = []     # 각 원소가 LIS의 어느 위치에 들어갔는지 기록
    
    for x in b_values:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
        pos_in_lis.append(idx)
    
    # 남길 수 있는 최대 전깃줄 개수
    lis_len = len(tails)
    # 없애야 하는 최소 전깃줄 개수
    print(n - lis_len)
    
    # 3. 역추적을 통해 LIS에 포함된 전깃줄 식별
    is_lis_member = [False] * n
    target_idx = lis_len - 1
    for i in range(n - 1, -1, -1):
        if pos_in_lis[i] == target_idx:
            is_lis_member[i] = True
            target_idx -= 1
            
    # 4. LIS에 포함되지 않은(제거할) 전깃줄의 A 위치 출력
    removed_a = []
    for i in range(n):
        if not is_lis_member[i]:
            removed_a.append(wires[i][0])
            
    # 제거할 전깃줄을 A 위치 오름차순으로 출력
    for a_pos in sorted(removed_a):
        print(a_pos)

if __name__ == "__main__":
    solve()

##########################################################################

