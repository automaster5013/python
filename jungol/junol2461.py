import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    flowers = []
    idx = 1
    for _ in range(N):
        # 날짜를 월*100 + 일 형태로 변환하여 정수화
        f_start = int(input_data[idx]) * 100 + int(input_data[idx+1])
        f_end = int(input_data[idx+2]) * 100 + int(input_data[idx+3])
        flowers.append((f_start, f_end))
        idx += 4

    # 피는 날짜 기준 오름차순 정렬
    flowers.sort()

    count = 0
    current_end = 301  # 현재 꽃이 피어 있어야 하는 목표 시작점
    max_end = 0        # 현재 선택할 수 있는 꽃 중 가장 늦게 지는 날짜
    flower_idx = 0
    
    while current_end <= 1130: # 11월 30일까지 덮어야 함
        found = False
        
        # 현재 비어있는 시점(current_end) 이전에 피는 꽃들 중 가장 늦게 지는 꽃 찾기
        while flower_idx < N:
            if flowers[flower_idx][0] <= current_end:
                if flowers[flower_idx][1] > max_end:
                    max_end = flowers[flower_idx][1]
                    found = True
                flower_idx += 1
            else:
                break
        
        if found:
            # 가장 멀리 가는 꽃을 선택하고 카운트 증가
            current_end = max_end
            count += 1
            # 이미 12월 1일(1201) 이후까지 덮었다면 성공
            if current_end > 1130:
                print(count)
                return
        else:
            # 연결할 수 있는 꽃이 없는 경우
            print(0)
            return

    # 끝까지 도달하지 못한 경우
    print(0)

if __name__ == "__main__":
    solve()

#######################################################################################

class Flower:
    def __init__(self, sm, sd, em, ed):
        self.start = sm * 100 + sd
        self.end = em * 100 + ed

    def __lt__(self, other):
        if self.start == other.start:
            return self.end > other.end
        return self.start < other.start

def solve_v2():
    import sys
    it = iter(map(int, sys.stdin.read().split()))
    try:
        n = next(it)
        flowers = [Flower(next(it), next(it), next(it), next(it)) for _ in range(n)]
        flowers.sort()

        last_end = 301
        count = 0
        i = 0
        
        while last_end <= 1130:
            best_end = 0
            found = False
            while i < n and flowers[i].start <= last_end:
                if flowers[i].end > best_end:
                    best_end = flowers[i].end
                    found = True
                i += 1
            
            if not found:
                print(0)
                return
                
            last_end = best_end
            count += 1
            
        print(count)
    except StopIteration:
        pass

solve_v2()

#######################################################################################

