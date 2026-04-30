import sys

def solve():
    # 대량의 데이터를 빠르게 읽기 위해 sys.stdin.read 사용
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    L = int(raw_data[0])
    N = int(raw_data[1])
    K = int(raw_data[2])
    A = [int(x) for x in raw_data[3:]]

    results = []
    
    # 1. 어두운 정도 0인 위치 (가로등 위치)
    num_zeros = min(N, K)
    results.extend([0] * num_zeros)
    K_rem = K - num_zeros
    
    if K_rem <= 0:
        sys.stdout.write('\n'.join(map(str, results)) + '\n')
        return

    h_list = []      # 2개씩 존재하는 거리의 최대값(h) 목록
    m_counts = {}    # 짝수 간격의 중앙값(m) 빈도수

    for i in range(N - 1):
        gap = A[i+1] - A[i]
        # 거리 1부터 h까지는 2개씩 존재
        h = (gap - 1) // 2
        if h > 0:
            h_list.append(h)
        # gap이 짝수면 정중앙에 1개만 존재하는 거리 m이 있음
        if gap % 2 == 0:
            m = gap // 2
            m_counts[m] = m_counts.get(m, 0) + 1

    # h_list를 오름차순 정렬하여 포인터로 효율적으로 관리
    h_list.sort()
    h_ptr = 0 # 현재 거리 d보다 작은 h값들을 건너뛰기 위한 포인터
    
    head_max = A[0]        # 0 ~ A1 구간의 최대 거리
    tail_max = L - A[-1]   # AN ~ L 구간의 최대 거리

    d = 1
    # K개를 채울 때까지 거리 d를 1씩 증가
    while K_rem > 0:
        # 현재 거리 d를 더 이상 2개씩 제공하지 못하는 h값들을 제외
        while h_ptr < len(h_list) and h_list[h_ptr] < d:
            h_ptr += 1
        
        # d를 2개씩 제공하는 구간의 개수
        active_h = len(h_list) - h_ptr
        count = 2 * active_h
        
        # 중앙값 m이 d인 경우 추가
        if d in m_counts:
            count += m_counts[d]
        
        # 도로 양 끝 구간에서 d가 가능한지 체크
        if d <= head_max:
            count += 1
        if d <= tail_max:
            count += 1
        
        # 필요한 개수만큼 결과에 추가
        num_to_print = min(count, K_rem)
        if num_to_print > 0:
            results.extend([d] * num_to_print)
        
        K_rem -= count
        d += 1

    # 최종 결과 출력
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()

####################################################################

