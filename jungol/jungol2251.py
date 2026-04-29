import sys
from bisect import bisect_left

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    switches = list(map(int, input_data[1:n+1]))
    bulbs = list(map(int, input_data[n+1:2*n+1]))

    # 1. 오른쪽 전구의 번호별 위치(인덱스) 저장
    bulb_pos = [0] * (n + 1)
    for i in range(n):
        bulb_pos[bulbs[i]] = i

    # 2. 왼쪽 스위치 순서대로 전구의 위치를 나열한 수열 생성
    # indices[i] = "왼쪽 i번째 스위치와 연결된 전구의 오른쪽 인덱스"
    indices = [bulb_pos[sw] for sw in switches]

    # 3. O(N log N) LIS 및 경로 추적 준비
    tails = []          # LIS를 유지하기 위한 배열
    pos_in_tails = [0] * n  # indices[i]가 LIS의 몇 번째 자리에 들어갔는지 저장
    parent = [-1] * n   # 경로 복원을 위한 이전 인덱스 저장 (옵션)

    # LIS 계산
    for i, x in enumerate(indices):
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
        pos_in_tails[i] = idx

    # 4. 결과 출력 및 경로 역추적
    max_len = len(tails)
    print(max_len)

    # LIS 구성 요소 찾기 (뒤에서부터 역추적)
    res_indices = []
    current_target = max_len - 1
    for i in range(n - 1, -1, -1):
        if pos_in_tails[i] == current_target:
            # 해당 인덱스의 스위치 번호를 가져옴
            res_indices.append(switches[i])
            current_target -= 1
    
    # 문제 요구사항: 스위치 번호를 오름차순으로 출력
    res_indices.sort()
    print(*(res_indices))

if __name__ == "__main__":
    solve()

########################################################################
