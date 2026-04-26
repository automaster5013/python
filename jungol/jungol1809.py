import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    heights = list(map(int, input_data[1:]))
    
    # 결과를 담을 배열 (0으로 초기화)
    ans = [0] * n
    # (높이, 번호)를 담을 스택
    stack = [] 
    
    for i in range(n):
        curr_h = heights[i]
        
        # 스택에 나보다 작은 탑들은 신호를 수신할 수 없으므로 제거
        while stack and stack[-1][0] < curr_h:
            stack.pop()
            
        # 스택에 남아있는 탑이 있다면, 그 탑이 내 신호를 받는 탑임
        if stack:
            ans[i] = stack[-1][1]
            
        # 현재 탑을 스택에 추가 (번호는 1번부터이므로 i+1)
        stack.append((curr_h, i + 1))
        
    # 결과 출력
    print(*(ans))

if __name__ == "__main__":
    solve_v1()

###########################################################################

import sys

def solve_v2():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    
    stack = []
    results = []
    
    for i in range(n):
        # 스택 맨 위 인덱스의 높이가 현재 높이보다 낮으면 제거
        while stack and h[stack[-1]] < h[i]:
            stack.pop()
            
        if not stack:
            results.append(0)
        else:
            results.append(stack[-1] + 1) # 1-based index
            
        stack.append(i)
        
    sys.stdout.write(" ".join(map(str, results)) + "\n")

solve_v2()

###########################################################################

class TowerSystem:
    def __init__(self, heights):
        self.heights = heights
        self.stack = [] # (height, id)

    def get_receivers(self):
        results = []
        for i, h in enumerate(self.heights, 1):
            while self.stack and self.stack[-1][0] < h:
                self.stack.pop()
            
            if not self.stack:
                results.append(0)
            else:
                results.append(self.stack[-1][1])
            
            self.stack.append((h, i))
        return results

def solve_v3():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    h_list = [int(x) for x in data[1:]]
    
    system = TowerSystem(h_list)
    print(*(system.get_receivers()))

solve_v3()

###########################################################################

import sys

def get_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)

def solve_v4():
    tokens = get_tokens()
    try:
        n = next(tokens)
        stack = [] # (height, id)
        ans = []
        
        for i in range(1, n + 1):
            h = next(tokens)
            while stack and stack[-1][0] < h:
                stack.pop()
            
            ans.append(stack[-1][1] if stack else 0)
            stack.append((h, i))
            
        print(*(ans))
    except StopIteration:
        pass

solve_v4()

###########################################################################

def solve_v5():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    h = [int(x) for x in data[1:]]
    
    res = [0] * n
    stack = [] # 아직 수신 탑을 찾지 못한 탑들의 인덱스
    
    # 이번에는 오른쪽에서 왼쪽으로 가며 '수신자'가 아닌 '송신자'를 스택에 담음
    for i in range(n - 1, -1, -1):
        # 현재 탑 i가 스택에 있는 탑들의 신호를 받아줄 수 있는지 확인
        while stack and h[stack[-1]] < h[i]:
            target_idx = stack.pop()
            res[target_idx] = i + 1
        stack.append(i)
        
    print(*(res))

solve_v5()

###########################################################################


