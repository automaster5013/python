import sys

# 고속 입력을 위한 설정
input = sys.stdin.readline

def get_max_overlap(segments):
    """구간 리스트를 받아 가장 많이 겹치는 지점의 횟수를 반환"""
    events = []
    for s, e in segments:
        if s > e: s, e = e, s
        # 선분 위나 아래 끝점과 겹치지 않아야 하므로 
        # 열린 구간 (s, e)에서 최댓값을 찾습니다.
        events.append((s, 1))
        events.append((e, -1))
    
    # 좌표 순으로 정렬
    events.sort()
    
    max_count = 0
    current_count = 0
    i = 0
    n = len(events)
    
    while i < n:
        curr_pos = events[i][0]
        # 동일한 좌표에서 발생하는 모든 이벤트를 한 번에 처리
        while i < n and events[i][0] == curr_pos:
            current_count += events[i][1]
            i += 1
        # 이 시점의 current_count는 curr_pos 바로 위(epsilon) 지점에서의 교차 횟수
        if current_count > max_count:
            max_count = current_count
            
    return max_count

def solve():
    try:
        n = int(input())
    except: return

    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))

    h_segments = [] # 수평 선분 (x축 구간)
    v_segments = [] # 수직 선분 (y축 구간)

    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n] # 시계방향 순회이므로 마지막 점은 첫 점과 연결
        
        if p1[0] == p2[0]: # x가 같으면 수직 선분
            v_segments.append((p1[1], p2[1]))
        else: # y가 같으면 수평 선분
            h_segments.append((p1[0], p2[0]))

    # 수평선 H는 수직 선분(v_segments)을 자릅니다.
    h = get_max_overlap(v_segments)
    # 수직선 V는 수평 선분(h_segments)을 자릅니다.
    v = get_max_overlap(h_segments)

    print(max(h, v))

if __name__ == "__main__":
    solve()

################################################################################


