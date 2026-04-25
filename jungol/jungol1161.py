def hanoi(n, start, end, via):
    # 기저 조건: 원판이 1개일 때 바로 이동
    if n == 1:
        print(f"{n} : {start} -> {end}")
        return

    # 1. n-1개 원판을 보조 기둥(via)으로 이동
    hanoi(n - 1, start, via, end)
    
    # 2. 가장 큰 원판을 목적 기둥(end)으로 이동
    print(f"{n} : {start} -> {end}")
    
    # 3. 보조 기둥에 있던 n-1개 원판을 다시 목적지로 이동
    hanoi(n - 1, via, end, start)

n = int(input())
hanoi(n, 1, 3, 2)

##################################################################

n = int(input())
# (원판수, 출발, 도착, 보조, 진행상태)
# 상태 0: 하위 원판 이동 전, 상태 1: 현재 원판 이동 및 이후 처리
stack = [(n, 1, 3, 2, 0)]

while stack:
    curr_n, start, end, via, state = stack.pop()
    
    if curr_n == 0: continue
    
    if state == 0:
        # 역순으로 쌓아야 정방향으로 실행됨
        stack.append((curr_n, start, end, via, 1))      # 2단계: 현재 원판 이동 대기
        stack.append((curr_n - 1, start, via, end, 0))  # 1단계: 위쪽 n-1개 치우기
    else:
        print(f"{curr_n} : {start} -> {end}")
        stack.append((curr_n - 1, via, end, start, 0))  # 3단계: 치웠던 n-1개 가져오기

##################################################################

n = int(input())
total_moves = 2**n - 1

# 각 원판이 다음에 어디로 갈지를 결정하는 순서 리스트
# n의 홀짝에 따라 방향 순서가 달라짐
if n % 2 == 0:
    dest = {1: [2, 3, 1], 0: [3, 2, 1]} # 원판 번호 % 2 에 따른 목적지 순환
else:
    dest = {1: [3, 2, 1], 0: [2, 3, 1]}

current_pos = [1] * (n + 1) # 모든 원판은 처음에 1번 기둥

for k in range(1, total_moves + 1):
    # 이동할 원판 번호 찾기 (k를 이진수로 썼을 때 끝에 붙은 0의 개수 + 1)
    disk = (k & -k).bit_length()
    
    # 해당 원판의 다음 위치 계산 (순환 구조)
    start = current_pos[disk]
    path = dest[disk % 2]
    # 현재 위치의 인덱스를 찾아 다음 위치로 이동
    next_idx = (path.index(start) + 1) % 3
    end = path[next_idx]
    
    print(f"{disk} : {start} -> {end}")
    current_pos[disk] = end

##################################################################

n = int(input())
pillars = {1: list(range(n, 0, -1)), 2: [], 3: []}

def move_disk(count, start, end, via):
    if count == 1:
        disk = pillars[start].pop()
        # 물리적 제약 조건 검사 (학습용)
        if pillars[end] and pillars[end][-1] < disk:
            raise Exception("Invalid Move!")
        pillars[end].append(disk)
        print(f"{disk} : {start} -> {end}")
        return

    move_disk(count - 1, start, via, end)
    move_disk(1, start, end, via)
    move_disk(count - 1, via, end, start)

move_disk(n, 1, 3, 2)

##################################################################

def solve_hanoi(num_disks):
    def step(d, s, e, v):
        if d > 0:
            yield from step(d - 1, s, v, e)
            yield f"{d} : {s} -> {e}"
            yield from step(d - 1, v, e, s)
    
    # 결과를 하나씩 뽑아서 출력
    for move in step(num_disks, 1, 3, 2):
        print(move)

n = int(input())
solve_hanoi(n)

##################################################################


