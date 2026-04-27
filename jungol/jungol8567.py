import sys

def solve():
    # 고속 입력을 통해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    # 초기값 설정 (매우 큰 값과 작은 값)
    min_y, max_y = float('inf'), float('-inf')
    min_u, max_u = float('inf'), float('-inf') # u = y - x
    min_v, max_v = float('inf'), float('-inf') # v = y + x
    
    idx = 1
    for _ in range(N):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        u = y - x
        v = y + x
        
        # 각 지표의 최솟값과 최댓값 갱신
        if y < min_y: min_y = y
        if y > max_y: max_y = y
        if u < min_u: min_u = u
        if u > max_u: max_u = u
        if v < min_v: min_v = v
        if v > max_v: max_v = v
        
    # 두 가지 케이스의 빗변 길이 계산
    # 1. 직각 정점이 위쪽인 경우
    L1 = max_u + max_v - 2 * min_y
    
    # 2. 직각 정점이 아래쪽인 경우
    L2 = 2 * max_y - min_u - min_v
    
    # 둘 중 더 짧은 것 출력
    print(min(L1, L2))

if __name__ == "__main__":
    solve()

################################################################


