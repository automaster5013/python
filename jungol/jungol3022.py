import sys

def solve():
    # 입력을 효율적으로 읽어오기 위해 sys.stdin 사용
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    # 유권자들의 투표 정보를 M(최대 단일 득표) 기준으로 그룹화
    # m_groups[m] = [(t1, d1), (t2, d2), ...]
    m_groups = {}
    for i in range(n):
        a = int(data[1 + 2*i])
        b = int(data[2 + 2*i])
        m = max(a, b)
        t = a + b
        d = a - b
        if m not in m_groups:
            m_groups[m] = []
        m_groups[m].append((t, d))
        
    sorted_m_keys = sorted(m_groups.keys())
    active_t_totals = {}  # 현재 유효한(X 조건 만족) 유권자들의 T값별 D합계
    total_ans = 0
    prev_m = 0
    limit = 100000
    
    # 고유한 M값들을 순회하며 X의 구간별로 계산
    # X가 (prev_m, m] 구간에 있을 때 유효 유권자 집합은 동일함
    for m in sorted_m_keys:
        if m > prev_m:
            count_y = 0
            if active_t_totals:
                # 현재 유효한 유권자들 중 Y 조건을 만족하는 경우를 찾음
                sorted_t_keys = sorted(active_t_totals.keys())
                curr_margin = 0
                prev_t = 0
                for t in sorted_t_keys:
                    # Y가 (prev_t, t] 구간에 있을 때 유효한 표의 총합이 양수인지 확인
                    if curr_margin > 0:
                        if prev_t < limit:
                            count_y += min(limit, t) - prev_t
                    
                    curr_margin += active_t_totals[t]
                    prev_t = t
                    if prev_t >= limit:
                        break
                
                # 마지막 T값 이후부터 100,000까지의 Y 구간 처리
                if curr_margin > 0 and prev_t < limit:
                    count_y += limit - prev_t
            
            # X 구간의 길이만큼 곱하여 총 경우의 수에 합산
            total_ans += count_y * (min(limit, m) - prev_m)
            
        # 다음 X 구간을 위해 현재 M값을 가진 유권자들을 활성 집합에 추가
        for t, d in m_groups[m]:
            active_t_totals[t] = active_t_totals.get(t, 0) + d
        prev_m = m
        if prev_m >= limit:
            break
            
    # 마지막 M값 이후부터 100,000까지의 X 구간 처리
    if prev_m < limit:
        count_y = 0
        if active_t_totals:
            sorted_t_keys = sorted(active_t_totals.keys())
            curr_margin = 0
            prev_t = 0
            for t in sorted_t_keys:
                if curr_margin > 0:
                    if prev_t < limit:
                        count_y += min(limit, t) - prev_t
                curr_margin += active_t_totals[t]
                prev_t = t
                if prev_t >= limit:
                    break
            if curr_margin > 0 and prev_t < limit:
                count_y += limit - prev_t
        total_ans += count_y * (limit - prev_m)
        
    print(total_ans)

if __name__ == "__main__":
    solve()

###########################################################################

