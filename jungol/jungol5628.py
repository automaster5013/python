import sys

def solve():
    # 고속 입력을 통해 N과 H, 그리고 장애물 정보를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    h_max = int(input_data[1])
    
    # 석순과 종유석의 높이별 개수를 저장할 배열
    bottom = [0] * (h_max + 1)
    top = [0] * (h_max + 1)
    
    # 장애물 분리 저장
    for i in range(n):
        val = int(input_data[2 + i])
        if i % 2 == 0: # 첫 번째(인덱스 0)는 석순
            bottom[val] += 1
        else: # 종유석
            top[val] += 1
            
    # 역방향 누적 합 계산
    # bottom[i]: 높이가 i 이상인 석순의 개수
    # top[i]: 높이가 i 이상인 종유석의 개수
    for i in range(h_max - 1, 0, -1):
        bottom[i] += bottom[i + 1]
        top[i] += top[i + 1]
        
    min_obstacles = n
    count_heights = 0
    
    # 각 비행 높이 1부터 H까지 탐색
    for i in range(1, h_max + 1):
        # 현재 높이 i에서 파괴되는 장애물 총합
        # 석순은 i 이상인 것들, 종유석은 높이가 (H - i + 1) 이상인 것들이 해당됨
        current_broken = bottom[i] + top[h_max - i + 1]
        
        if current_broken < min_obstacles:
            min_obstacles = current_broken
            count_heights = 1
        elif current_broken == min_obstacles:
            count_heights += 1
            
    print(f"{min_obstacles} {count_heights}")

if __name__ == "__main__":
    solve()

###############################################################################


