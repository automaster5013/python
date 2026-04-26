def solve_v1():
    import sys
    # 명령의 수 입력
    n_input = sys.stdin.readline()
    if not n_input: return
    n = int(n_input)
    
    stack = []
    
    for _ in range(n):
        command = sys.stdin.readline().split()
        
        if command[0] == 'i':
            # "i a" 명령: 스택에 숫자 추가
            stack.append(int(command[1]))
        elif command[0] == 'o':
            # "o" 명령: 스택에서 제거 및 출력
            if not stack:
                print("empty")
            else:
                print(stack.pop())
        elif command[0] == 'c':
            # "c" 명령: 스택 크기 출력
            print(len(stack))

solve_v1()

###############################################################

from collections import deque
import sys

def solve_v2():
    n_str = sys.stdin.readline().strip()
    if not n_str: return
    n = int(n_str)
    
    stack = deque()
    
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        
        if cmd[0] == 'i':
            stack.append(int(cmd[1]))
        elif cmd[0] == 'o':
            if not stack:
                print("empty")
            else:
                # deque에서도 append/pop은 마지막 원소를 다룹니다.
                print(stack.pop())
        elif cmd[0] == 'c':
            print(len(stack))

solve_v2()

###############################################################

class MyStack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        if self.is_empty():
            return "empty"
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return len(self.items) == 0

def solve_v3():
    import sys
    n = int(sys.stdin.readline())
    s = MyStack()
    
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == 'i':
            s.push(int(line[1]))
        elif line[0] == 'o':
            print(s.pop())
        elif line[0] == 'c':
            print(s.size())

solve_v3()

###############################################################

def solve_v4():
    import sys
    n = int(sys.stdin.readline())
    stack = []
    
    # 각 명령에 대응하는 동작 정의
    commands = {
        'o': lambda: print(stack.pop() if stack else "empty"),
        'c': lambda: print(len(stack))
    }
    
    for _ in range(n):
        cmd_line = sys.stdin.readline().split()
        action = cmd_line[0]
        
        if action == 'i':
            stack.append(int(cmd_line[1]))
        else:
            commands[action]()

solve_v4()

###############################################################

def solve_v5():
    import sys
    try:
        input_data = sys.stdin.read().splitlines()
        n = int(input_data[0])
        stack = []
        
        for i in range(1, n + 1):
            cmd = input_data[i].split()
            
            if cmd[0] == 'i':
                stack.append(cmd[1])
            elif cmd[0] == 'c':
                print(len(stack))
            elif cmd[0] == 'o':
                try:
                    print(stack.pop())
                except IndexError:
                    print("empty")
    except EOFError:
        pass

solve_v5()

###############################################################


