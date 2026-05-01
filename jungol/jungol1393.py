import sys

def solve():
    # 고속 입출력을 위해 모든 데이터를 한꺼번에 읽습니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    # 열차 A의 구간 변화 지점 (위치, 변화량)
    n = int(input_data[ptr]); ptr += 1
    p_delta = []
    for _ in range(n):
        x = int(input_data[ptr]); y = int(input_data[ptr+1]); ptr += 2
        p_delta.append((x, 1))
        p_delta.append((y + 1, -1))
        
    # 열차 B의 구간 변화 지점
    m = int(input_data[ptr]); ptr += 1
    q_delta = []
    for _ in range(m):
        z = int(input_data[ptr]); w = int(input_data[ptr+1]); ptr += 2
        q_delta.append((z, 1))
        q_delta.append((w + 1, -1))

    # 모든 s = p + q 지점에서의 이계 차분 이벤트 생성
    # 파이썬의 객체 오버헤드를 줄이기 위해 (위치 << 2 | 가중치) 형태로 패킹합니다.
    # 가중치: 1*1=1(2), 1*-1=-1(0), -1*-1=1(2)
    events = [((px + qx) << 2 | (pv * qv + 1)) 
              for px, pv in p_delta 
              for qx, qv in q_delta]
    
    # 400만 개의 정수를 정렬합니다 (약 1.0~1.5초 소요)
    events.sort()

    max_f = -1
    best_s = 0
    curr_f = 0  # 현재 s에서의 겹침 수 f(s)
    curr_d = 0  # 현재 s에서의 기울기 f(s) - f(s-1)
    prev_s = events[0] >> 2
    
    i = 0
    total_events = len(events)
    while i < total_events:
        e = events[i]
        s = e >> 2
        
        # 1. 이전 이벤트와 현재 s 사이의 직선 구간 처리
        if s > prev_s:
            # 기울기(curr_d)가 양수라면 구간의 마지막(s-1)에서 최댓값이 갱신될 가능성이 큼
            if curr_d > 0:
                val = curr_f + curr_d * (s - 1 - prev_s)
                if val > max_f:
                    max_f = val
                    best_s = s - 1
            # f(s-1) 값 갱신
            curr_f += curr_d * (s - 1 - prev_s)
            prev_s = s
        
        # 2. 동일한 s 위치의 모든 이계 차분 값을 합산
        dd = 0
        while i < total_events and (events[i] >> 2) == s:
            dd += (events[i] & 3) - 1 # 0 -> -1, 2 -> 1
            i += 1
            
        # 3. f(s) 값과 기울기 갱신
        curr_d += dd
        curr_f += curr_d
        
        # 최댓값 발생 시 최소 s를 유지하기 위해 등호 없이 비교
        if curr_f > max_f:
            max_f = curr_f
            best_s = s

    # 문제의 정의에 따라 이동 칸수 k = s - 1 (예제 s=11 -> k=10)
    print(best_s - 1)

if __name__ == "__main__":
    solve()

########################################################################################


