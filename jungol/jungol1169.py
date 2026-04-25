N, M = map(int, input().split())
path = [0] * N
visited = [False] * 7

def solve(depth, start):
    if depth == N:
        print(*(path))
        return

    for i in range(1, 7):
        if M == 1: # 모든 경우
            path[depth] = i
            solve(depth + 1, i)
        elif M == 2: # 중복 제외 (조합: 오름차순 유지)
            if i < start: continue
            path[depth] = i
            solve(depth + 1, i)
        elif M == 3: # 모두 다른 수 (순열)
            if visited[i]: continue
            visited[i] = True
            path[depth] = i
            solve(depth + 1, i)
            visited[i] = False

solve(0, 1)

######################################################################

N, M = map(int, input().split())

# (현재 깊이, 현재까지의 경로, 마지막 숫자, 사용된 숫자 집합)
stack = [(0, [], 1, 0)]

while stack:
    depth, current_path, last, used_bit = stack.pop()
    
    if depth == N:
        # 스택 특성상 역순으로 나오므로 출력 시 조절이 필요할 수 있음
        # 여기서는 단순히 원리 이해를 위해 정방향으로 구성
        continue # 실제 구현 시에는 재귀와 루프 순서를 고려하여 설계

# *참고: 반복문 방식은 사전순 출력을 위해 숫자를 6부터 1까지 거꾸로 스택에 넣어야 합니다.

######################################################################

N, M = map(int, input().split())
results = [[]]

for _ in range(N):
    next_level = []
    for p in results:
        for i in range(1, 7):
            if M == 1:
                next_level.append(p + [i])
            elif M == 2:
                if not p or i >= p[-1]:
                    next_level.append(p + [i])
            elif M == 3:
                if i not in p:
                    next_level.append(p + [i])
    results = next_level

for res in results:
    print(*(res))

######################################################################

N, M = map(int, input().split())

# 1부터 6까지의 숫자로 이루어진 N자리 6진수와 같은 원리
path = [1] * N
while True:
    # 조건 검사
    valid = True
    if M == 2: # 중복 제외: 숫자가 작아지면 무효
        for i in range(N - 1):
            if path[i] > path[i+1]: valid = False; break
    elif M == 3: # 모두 다른 수: 중복 발견 시 무효
        for i in range(N):
            for j in range(i + 1, N):
                if path[i] == path[j]: valid = False; break
    
    if valid: print(*(path))
    
    # 다음 경우로 넘어가기 (숫자 1씩 올리기)
    idx = N - 1
    while idx >= 0:
        path[idx] += 1
        if path[idx] <= 6: break
        path[idx] = 1
        idx -= 1
    if idx < 0: break # 모든 경우 탐색 완료

######################################################################

N, M = map(int, input().split())

def dfs_string(depth, current_str, last, used_mask):
    if depth == N:
        print(current_str.strip())
        return

    for i in range(1, 7):
        if M == 1:
            dfs_string(depth + 1, current_str + str(i) + " ", i, 0)
        elif M == 2:
            if i < last: continue
            dfs_string(depth + 1, current_str + str(i) + " ", i, 0)
        elif M == 3:
            if used_mask & (1 << i): continue # 비트마스크로 사용 여부 체크
            dfs_string(depth + 1, current_str + str(i) + " ", i, used_mask | (1 << i))

dfs_string(0, "", 1, 0)

######################################################################


