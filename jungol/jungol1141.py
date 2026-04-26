import sys

def solve_v1():
    # 고속 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    heights = [int(x) for x in input[1:]]
    
    stack = []
    total_count = 0
    
    for h in heights:
        # 스택이 비어있지 않고, 맨 위의 소가 현재 소보다 작거나 같으면
        # 현재 소 때문에 앞을 못 보게 되므로 제거
        while stack and stack[-1] <= h:
            stack.pop()
        
        # 스택에 남아있는 소들은 현재 소(h)를 볼 수 있는 소들임
        total_count += len(stack)
        
        # 현재 소를 스택에 추가
        stack.append(h)
        
    print(total_count)

if __name__ == "__main__":
    solve_v1()

############################################################################

from collections import deque
import sys

def solve_v2():
    it = iter(sys.stdin.read().split())
    try:
        n = int(next(it))
        stack = deque()
        ans = 0
        
        for _ in range(n):
            h = int(next(it))
            while stack and stack[-1] <= h:
                stack.pop()
            
            ans += len(stack)
            stack.append(h)
            
        print(ans)
    except StopIteration:
        pass

solve_v2()

############################################################################

class CowManager:
    def __init__(self):
        self.stack = []
        self.total_seen = 0

    def add_cow(self, height):
        while self.stack and self.stack[-1] <= height:
            self.stack.pop()
        self.total_seen += len(self.stack)
        self.stack.append(height)

def solve_v3():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    
    manager = CowManager()
    n = int(data[0])
    for i in range(1, n + 1):
        manager.add_cow(int(data[i]))
        
    print(manager.total_seen)

solve_v3()

############################################################################

import sys

def get_heights():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)

def solve_v4():
    gen = get_heights()
    try:
        n = next(gen)
        stack = []
        result = 0
        
        for _ in range(n):
            curr_h = next(gen)
            while stack and stack[-1] <= curr_h:
                stack.pop()
            result += len(stack)
            stack.append(curr_h)
            
        sys.stdout.write(str(result) + '\n')
    except StopIteration:
        pass

solve_v4()

############################################################################

def solve_v5():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    h = [int(x) for x in data[1:]]
    
    # 각 소가 오른쪽에서 처음으로 자기보다 크거나 같은 소를 만나는 인덱스
    right_wall = [n] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and h[stack[-1]] < h[i]:
            stack.pop()
        if stack:
            right_wall[i] = stack[-1]
        stack.append(i)
    
    # 볼 수 있는 소의 수 = (벽의 인덱스 - 현재 인덱스 - 1)
    ans = sum(right_wall[i] - i - 1 for i in range(n))
    print(ans)

solve_v5()

############################################################################

