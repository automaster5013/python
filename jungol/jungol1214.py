import sys

def solve_v1():
    # 데이터를 한 번에 읽어와 토큰화
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    
    n = data[0]
    heights = data[1:]
    # 모든 사각형을 처리하기 위해 마지막에 높이 0을 추가
    heights.append(0)
    
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        # 스택이 비어있지 않고, 현재 높이가 스택 맨 위 높이보다 낮을 때
        while stack and heights[stack[-1]] > heights[i]:
            # 면적을 계산할 사각형의 높이
            h = heights[stack.pop()]
            
            # 너비 계산
            # 스택이 비었다면 현재 인덱스 i가 전체 너비
            # 비지 않았다면 (현재 인덱스 - 1) - (새로운 스택 Top 인덱스)
            w = i if not stack else i - stack[-1] - 1
            
            max_area = max(max_area, h * w)
            
        stack.append(i)
        
    print(max_area)

if __name__ == "__main__":
    solve_v1()

################################################################################

import sys
sys.setrecursionlimit(200000)

def solve_v2():
    # 이 방식은 스택 방식보다 복잡하지만 논리적 사고를 기르기에 좋습니다.
    # 여기서는 이해를 돕기 위해 스택 기반의 간결한 구조를 유지합니다.
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    n, h = data[0], data[1:]
    
    stack = [-1]
    max_a = 0
    h.append(0)
    
    for i in range(len(h)):
        while stack[-1] != -1 and h[stack[-1]] >= h[i]:
            height = h[stack.pop()]
            width = i - stack[-1] - 1
            max_a = max(max_a, height * width)
        stack.append(i)
        
    print(max_a)

solve_v2()

################################################################################

class HistogramAnalyzer:
    def __init__(self, heights):
        self.heights = heights + [0]
        self.stack = []
        self.max_area = 0

    def find_max_rectangle(self):
        for i, h in enumerate(self.heights):
            while self.stack and self.heights[self.stack[-1]] > h:
                height = self.heights[self.stack.pop()]
                width = i if not self.stack else i - self.stack[-1] - 1
                self.max_area = max(self.max_area, height * width)
            self.stack.append(i)
        return self.max_area

def solve_v3():
    import sys
    it = iter(map(int, sys.stdin.read().split()))
    try:
        n = next(it)
        h_list = [next(it) for _ in range(n)]
        analyzer = HistogramAnalyzer(h_list)
        print(analyzer.find_max_rectangle())
    except StopIteration:
        pass

solve_v3()

################################################################################

