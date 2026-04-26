import sys
from collections import deque

def solve_v1():
    # 명령의 수 입력
    line = sys.stdin.readline()
    if not line: return
    n = int(line)
    
    queue = deque()
    
    for _ in range(n):
        command = sys.stdin.readline().split()
        
        if command[0] == 'i':
            # "i a" 명령: 큐에 숫자 추가
            queue.append(int(command[1]))
        elif command[0] == 'o':
            # "o" 명령: 가장 앞의 데이터를 빼고 출력
            if not queue:
                print("empty")
            else:
                print(queue.popleft())
        elif command[0] == 'c':
            # "c" 명령: 현재 데이터 개수 출력
            print(len(queue))

solve_v1()

#################################################################

def solve_v2():
    import sys
    input_data = sys.stdin.read().splitlines()
    n = int(input_data[0])
    
    q = []
    
    for i in range(1, n + 1):
        cmd = input_data[i].split()
        
        if cmd[0] == 'i':
            q.append(cmd[1])
        elif cmd[0] == 'o':
            if not q:
                print("empty")
            else:
                # 리스트의 0번 인덱스를 제거하고 반환
                print(q.pop(0))
        elif cmd[0] == 'c':
            print(len(q))

solve_v2()

#################################################################

class MyQueue:
    def __init__(self):
        from collections import deque
        self.items = deque()
        
    def enqueue(self, val):
        self.items.append(val)
        
    def dequeue(self):
        if self.is_empty():
            return "empty"
        return self.items.popleft()
        
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return len(self.items) == 0

def solve_v3():
    import sys
    n = int(sys.stdin.readline())
    q_obj = MyQueue()
    
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == 'i':
            q_obj.enqueue(line[1])
        elif line[0] == 'o':
            print(q_obj.dequeue())
        elif line[0] == 'c':
            print(q_obj.size())

solve_v3()

#################################################################

def solve_v4():
    import sys
    from collections import deque
    
    n = int(sys.stdin.readline())
    queue = deque()
    
    # 동작 정의
    actions = {
        'o': lambda: print(queue.popleft() if queue else "empty"),
        'c': lambda: print(len(queue))
    }
    
    for _ in range(n):
        cmd_line = sys.stdin.readline().split()
        action_type = cmd_line[0]
        
        if action_type == 'i':
            queue.append(cmd_line[1])
        else:
            actions[action_type]()

solve_v4()

#################################################################

def solve_v5():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    
    q = []
    front = 0 # 가장 앞을 가리키는 포인터
    
    ptr = 1
    while ptr < len(input):
        cmd = input[ptr]
        if cmd == 'i':
            q.append(input[ptr+1])
            ptr += 2
        elif cmd == 'o':
            if front == len(q):
                print("empty")
            else:
                print(q[front])
                front += 1 # 논리적으로 제거됨
            ptr += 1
        elif cmd == 'c':
            print(len(q) - front)
            ptr += 1

solve_v5()

#################################################################




