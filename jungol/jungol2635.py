import sys

def solve():
    # 입력을 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    input_iter = iter(input_data)
    N = int(next(input_iter)) # 막대기 개수
    L = int(next(input_iter)) # 평행선 간격
    
    sticks = []
    for _ in range(N):
        t = int(next(input_iter))
        d = int(next(input_iter))
        sticks.append((t, d))
        
    # t를 주 정렬 기준으로, d를 부 정렬 기준으로 오름차순 정렬
    sticks.sort()
    
    # d 좌표 압축
    all_d = sorted(list(set(s[1] for s in sticks)))
    d_map = {val: i for i, val in enumerate(all_d)}
    num_d = len(all_d)
    
    # best_top_at_bot[idx]는 아래쪽 좌표 d에서 끝나는 경로의 최대 길이
    best_top_at_bot = [0] * num_d
    max_len = 0
    
    i = 0
    while i < N:
        # 같은 위쪽 좌표 t를 가지는 막대기 그룹 처리
        j = i
        while j < N and sticks[j][0] == sticks[i][0]:
            j += 1
        
        t = sticks[i][0]
        
        # 현재 t 그룹에서 위쪽 t로 도착하는 경로 계산
        dp_to_top = []
        for k in range(i, j):
            d = sticks[k][1]
            length = abs(t - d) + L
            dp_to_top.append(length + best_top_at_bot[d_map[d]])
            
        # 현재 t 그룹에서 아래쪽 d로 도착하는 경로 계산 및 갱신
        running_max_top = 0
        for k in range(i, j):
            d = sticks[k][1]
            idx = d_map[d]
            length = abs(t - d) + L
            
            val_top = dp_to_top[k-i] # top t에 도달 (d 공유)
            val_bot = length + running_max_top # bot d에 도달 (t 공유)
            
            # 전체 최대 길이 갱신
            if val_top > max_len: max_len = val_top
            if val_bot > max_len: max_len = val_bot
            
            # 다음 t 그룹을 위해 아래쪽 d 도달 정보 갱신
            if val_bot > best_top_at_bot[idx]:
                best_top_at_bot[idx] = val_bot
            
            # 현재 t 그룹 내에서 위쪽 t 도달 정보 갱신 (point t 공유)
            if val_top > running_max_top:
                running_max_top = val_top
        
        i = j
        
    sys.stdout.write(str(max_len) + '\n')

if __name__ == "__main__":
    solve()

###########################################################################

