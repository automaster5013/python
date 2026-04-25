N, M = map(int, input().split())
path = [0] * N

def solve(depth, current_sum):
    # 기저 조건: N번 모두 던졌을 때
    if depth == N:
        if current_sum == M:
            print(*(path))
        return

    # 주사위 눈 1~6까지 시도
    for i in range(1, 7):
        path[depth] = i
        solve(depth + 1, current_sum + i)

solve(0, 0)

###########################################################

N, M = map(int, input().split())
path = [0] * N

def solve_optimized(depth, current_sum):
    # 가지치기: 현재 합이 M을 넘거나, 남은 주사위로 M을 만들 수 없는 경우
    remaining_dice = N - depth
    if current_sum > M or current_sum + remaining_dice * 6 < M or current_sum + remaining_dice * 1 > M:
        return

    if depth == N:
        if current_sum == M:
            print(*(path))
        return

    for i in range(1, 7):
        path[depth] = i
        solve_optimized(depth + 1, current_sum + i)

solve_optimized(0, 0)

###########################################################

N, M = map(int, input().split())

# (현재 깊이, 현재 합, 현재까지의 경로)
# 스택은 LIFO이므로 숫자를 6부터 1까지 거꾸로 넣어야 예제와 같이 작은 수부터 출력됩니다.
stack = [(0, 0, [])]

while stack:
    depth, current_sum, current_path = stack.pop()
    
    if depth == N:
        if current_sum == M:
            print(*(current_path))
        continue
        
    # 작은 숫자가 먼저 출력되도록 6부터 1까지 스택에 쌓음
    for i in range(6, 0, -1):
        if current_sum + i <= M: # 간단한 가지치기 포함
            stack.append((depth + 1, current_sum + i, current_path + [i]))

###########################################################

N, M = map(int, input().split())
# 처음에는 빈 경로와 합계 0으로 시작
results = [([], 0)]

for _ in range(N):
    next_level = []
    for path, current_sum in results:
        for i in range(1, 7):
            if current_sum + i <= M: # 유효한 범위 내에서만 확장
                next_level.append((path + [i], current_sum + i))
    results = next_level

# 최종 결과 중 합이 M인 것만 출력
for path, total in results:
    if total == M:
        print(*(path))

###########################################################

N, M = map(int, input().split())
path = []

def solve_backward(remaining_n, remaining_m):
    # 남은 주사위가 없는데 남은 목표 합이 0이면 성공
    if remaining_n == 0:
        if remaining_m == 0:
            print(*(path))
        return

    for i in range(1, 7):
        # 이번 눈이 남은 목표치보다 작거나 같을 때만 진행
        if remaining_m >= i:
            path.append(i)
            solve_backward(remaining_n - 1, remaining_m - i)
            path.pop() # 백트래킹: 돌아올 때 마지막 눈 제거

solve_backward(N, M)

###########################################################





