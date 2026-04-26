import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    # 빌딩 높이 (1번부터 시작하도록 인덱스 조정)
    heights = [0] + [int(x) for x in input_data[1:]]
    
    ans = [0] * (n + 1)
    stack = [] # 아직 높은 빌딩을 못 찾은 빌딩의 '번호'를 담는 스택
    
    for i in range(1, n + 1):
        # 스택이 있고, 현재 빌딩이 스택 맨 위 빌딩보다 높다면
        while stack and heights[stack[-1]] < heights[i]:
            # 스택의 빌딩에게 현재 빌딩 번호를 알려주고 탈출!
            target_idx = stack.pop()
            ans[target_idx] = i
        
        # 현재 빌딩도 스택에 추가
        stack.append(i)
        
    # 결과 출력 (1번부터 N번까지)
    sys.stdout.write('\n'.join(map(str, ans[1:])) + '\n')

if __name__ == "__main__":
    solve_v1()

#######################################################################

import sys

def solve_v2():
    input = sys.stdin.read().split()
    n = int(input[0])
    h = [int(x) for x in input[1:]]
    
    ans = [0] * n
    stack = [] # 오른쪽에서 만난 빌딩들 중 '가능성 있는' 후보들
    
    # 오른쪽에서 왼쪽으로 이동
    for i in range(n - 1, -1, -1):
        # 나보다 작거나 같은 빌딩은 가려져서 안 보이므로 후보에서 제거
        while stack and h[stack[-1]] <= h[i]:
            stack.pop()
        
        # 스택에 남은 가장 위의 빌딩이 나보다 큰 가장 가까운 빌딩임
        if stack:
            ans[i] = stack[-1] + 1 # 1번부터 시작하는 번호 보정
            
        stack.append(i)
        
    print('\n'.join(map(str, ans)))

solve_v2()

#######################################################################

class BuildingManager:
    def __init__(self, heights):
        self.heights = heights
        self.n = len(heights)
        self.results = [0] * self.n

    def find_nearest_taller(self):
        stack = []
        for i in range(self.n):
            while stack and self.heights[stack[-1]] < self.heights[i]:
                prev_idx = stack.pop()
                self.results[prev_idx] = i + 1
            stack.append(i)
        return self.results

def solve_v3():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    h_list = [int(x) for x in data[1:]]
    
    manager = BuildingManager(h_list)
    for res in manager.find_nearest_taller():
        sys.stdout.write(f"{res}\n")

solve_v3()

#######################################################################

from collections import deque
import sys

def get_heights():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)

def solve_v4():
    gen = get_heights()
    try:
        n = next(gen)
        ans = [0] * (n + 1)
        stack = deque()
        
        # 높이 데이터를 리스트로 미리 저장 (비교를 위해 필요)
        h = [0] + [next(gen) for _ in range(n)]
        
        for i in range(1, n + 1):
            while stack and h[stack[-1]] < h[i]:
                ans[stack.pop()] = i
            stack.append(i)
            
        sys.stdout.write('\n'.join(map(str, ans[1:])) + '\n')
    except StopIteration:
        pass

solve_v4()

#######################################################################

def solve_v5():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    
    # {인덱스: 높이} 매핑
    h_map = {i+1: int(val) for i, val in enumerate(data[1:])}
    ans = {i: 0 for i in range(1, n + 1)}
    stack = []
    
    for i in range(1, n + 1):
        curr_h = h_map[i]
        while stack and h_map[stack[-1]] < curr_h:
            ans[stack.pop()] = i
        stack.append(i)
        
    for i in range(1, n + 1):
        sys.stdout.write(f"{ans[i]}\n")

solve_v5()

#######################################################################





