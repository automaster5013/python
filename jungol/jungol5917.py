import sys
from collections import deque

def solve_v1():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input: return
    
    N = int(input[0])
    T = int(input[1])
    
    # 공간 1: 세척 대기 (1번이 맨 위)
    space1 = deque(range(1, N + 1))
    # 공간 2: 세척 완료 (스택)
    space2 = []
    # 공간 3: 건조 완료 (스택)
    space3 = []
    
    idx = 2
    for _ in range(T):
        C = int(input[idx])
        D = int(input[idx+1])
        idx += 2
        
        if C == 1: # 씻기: 1 -> 2
            for _ in range(D):
                if space1:
                    space2.append(space1.popleft())
        else: # 건조: 2 -> 3
            for _ in range(D):
                if space2:
                    space3.append(space2.pop())
                    
    # 건조가 완료된 공간 3은 아래에서 위로 쌓인 순서입니다.
    # 문제 출력은 위에서 아래로이므로 뒤집어서 출력합니다.
    for plate in reversed(space3):
        print(plate)

solve_v1()

#################################################################

from collections import deque
import sys

def solve_v2():
    input_data = sys.stdin.read().split()
    N, T = int(input_data[0]), int(input_data[1])
    
    s1 = deque(range(1, N + 1)) # 공간 1 (Queue)
    s2 = []                     # 공간 2 (Stack)
    s3 = []                     # 공간 3 (Stack)
    
    idx = 2
    for _ in range(T):
        c, d = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        
        if c == 1:
            for _ in range(d):
                s2.append(s1.popleft())
        else:
            for _ in range(d):
                s3.append(s2.pop())
                
    # 최종 결과: 스택의 맨 위(마지막 원소)부터 출력
    while s3:
        sys.stdout.write(str(s3.pop()) + '\n')

solve_v2()

#################################################################

class Kitchen:
    def __init__(self, n):
        self.dirty = list(range(n, 0, -1)) # 스택으로 쓰기 위해 역순 저장
        self.washed = []
        self.dried = []

    def wash(self, count):
        for _ in range(count):
            self.washed.append(self.dirty.pop())

    def dry(self, count):
        for _ in range(count):
            self.dried.append(self.washed.pop())

    def get_result(self):
        return self.dried[::-1]

def solve_v3():
    import sys
    input_data = sys.stdin.read().split()
    n, t = int(input_data[0]), int(input_data[1])
    kitchen = Kitchen(n)
    
    pos = 2
    for _ in range(t):
        c, d = int(input_data[pos]), int(input_data[pos+1])
        pos += 2
        if c == 1: kitchen.wash(d)
        else: kitchen.dry(d)
        
    for p in kitchen.get_result():
        print(p)

solve_v3()

#################################################################

def solve_v4():
    import sys
    it = iter(sys.stdin.read().split())
    N, T = int(next(it)), int(next(it))
    
    # 인덱스 접근을 최적화하기 위해 리스트 사용
    s1 = list(range(1, N+1))
    s2, s3 = [], []
    
    # 명령 매핑
    actions = {
        1: lambda d: [s2.append(s1.pop(0)) for _ in range(d)],
        2: lambda d: [s3.append(s2.pop()) for _ in range(d)]
    }
    
    for _ in range(T):
        actions[int(next(it))](int(next(it)))
        
    sys.stdout.write('\n'.join(map(str, s3[::-1])) + '\n')

solve_v4()

#################################################################

def solve_v5():
    import sys
    input = sys.stdin.read().split()
    N, T = int(input[0]), int(input[1])
    
    # dirty 포인터
    d_ptr = 0
    washed = []
    dried = []
    
    ptr = 2
    for _ in range(T):
        cmd, num = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        
        if cmd == 1:
            for i in range(num):
                # 접시 번호는 d_ptr + 1
                washed.append(d_ptr + 1)
                d_ptr += 1
        else:
            for i in range(num):
                dried.append(washed.pop())
                
    # dried는 스택이므로 위에서 아래로 출력하려면 역순
    sys.stdout.write('\n'.join(map(str, dried[::-1])) + '\n')

solve_v5()

#################################################################





