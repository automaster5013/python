import sys
from collections import deque

def solve_v1():
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    queue = deque()
    total_time = 0
    
    idx = 1
    while idx < len(input):
        cmd = input[idx]
        
        if cmd == 'call':
            val = int(input[idx + 1])
            queue.append(val)
            total_time += val
            idx += 2
        elif cmd == 'wait':
            wait_time = int(input[idx + 1])
            total_time -= wait_time
            # 시간 흐름 처리
            while wait_time > 0 and queue:
                if queue[0] > wait_time:
                    queue[0] -= wait_time
                    wait_time = 0
                else:
                    wait_time -= queue.popleft()
            # 대기열이 비었는데 시간이 남았다면 total_time은 0이 되어야 함
            if total_time < 0: total_time = 0
            idx += 2
        elif cmd == 'check':
            print(f"{len(queue)} people {total_time} minutes")
            idx += 1

solve_v1()

###############################################################################

def solve_v2():
    import sys
    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    queue = []
    
    for i in range(1, n + 1):
        line = lines[i].split()
        cmd = line[0]
        
        if cmd == 'call':
            queue.append(int(line[1]))
        elif cmd == 'wait':
            t = int(line[1])
            while t > 0 and queue:
                if queue[0] > t:
                    queue[0] -= t
                    t = 0
                else:
                    t -= queue.pop(0)
        elif cmd == 'check':
            print(f"{len(queue)} people {sum(queue)} minutes")

solve_v2()

###############################################################################

class CallCenter:
    def __init__(self):
        self.queue = []
        self.total = 0

    def add_call(self, time):
        self.queue.append(time)
        self.total += time

    def pass_time(self, x):
        actual_wait = min(x, self.total)
        self.total -= actual_wait
        while x > 0 and self.queue:
            if self.queue[0] > x:
                self.queue[0] -= x
                x = 0
            else:
                x -= self.queue.pop(0)

    def status(self):
        return f"{len(self.queue)} people {self.total} minutes"

def solve_v3():
    import sys
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    cc = CallCenter()
    for _ in range(n):
        cmd = next(it)
        if cmd == 'call': cc.add_call(int(next(it)))
        elif cmd == 'wait': cc.pass_time(int(next(it)))
        else: print(cc.status())

solve_v3()

###############################################################################

def solve_v4():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    
    q = []
    front = 0
    ptr = 1
    
    for _ in range(n):
        cmd = data[ptr]
        if cmd == 'call':
            q.append(int(data[ptr+1]))
            ptr += 2
        elif cmd == 'wait':
            w = int(data[ptr+1])
            ptr += 2
            while w > 0 and front < len(q):
                if q[front] > w:
                    q[front] -= w
                    w = 0
                else:
                    w -= q[front]
                    front += 1
        else: # check
            rem_time = sum(q[front:])
            print(f"{len(q) - front} people {rem_time} minutes")
            ptr += 1

solve_v4()

###############################################################################

def solve_v5():
    import sys
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    q = []
    
    def do_call(): q.append(int(next(it)))
    def do_check(): print(f"{len(q)} people {sum(q)} minutes")
    def do_wait():
        w = int(next(it))
        while w > 0 and q:
            if q[0] > w: q[0] -= w; w = 0
            else: w -= q.pop(0)
            
    cmds = {'call': do_call, 'check': do_check, 'wait': do_wait}
    for _ in range(n):
        cmds[next(it)]()

solve_v5()

###############################################################################


