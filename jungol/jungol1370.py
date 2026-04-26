import sys

def solve():
    # 모든 데이터를 한 번에 읽어와 토큰화합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    meetings = []
    
    # 데이터 파싱: (ID, 시작시간, 종료시간)
    for i in range(n):
        idx = 1 + i * 3
        m_id = int(input_data[idx])
        start = int(input_data[idx+1])
        end = int(input_data[idx+2])
        meetings.append((m_id, start, end))
        
    # 1. 종료 시간(x[2])을 기준으로 오름차순 정렬
    # 종료 시간이 같다면 시작 시간(x[1])을 기준으로 정렬
    meetings.sort(key=lambda x: (x[2], x[1]))
    
    selected_meetings = []
    last_end_time = 0
    
    # 2. 그리디 탐색
    for m_id, start, end in meetings:
        # 현재 회의의 시작 시간이 이전 회의의 종료 시간보다 크거나 같으면 선택
        if start >= last_end_time:
            selected_meetings.append(m_id)
            last_end_time = end
            
    # 3. 결과 출력
    print(len(selected_meetings))
    print(*(selected_meetings))

if __name__ == "__main__":
    solve()

##############################################################################

