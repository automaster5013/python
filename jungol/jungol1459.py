n = int(input())
adj = [0] * (n + 1)
for i in range(1, n + 1):
    adj[i] = int(input())

result = []

def dfs(start, current, visited):
    # 이미 방문한 노드에 도달했을 때, 그게 시작점이면 사이클 완성!
    if adj[current] == start:
        return True
    if adj[current] in visited:
        return False
    
    visited.add(adj[current])
    return dfs(start, adj[current], visited)

for i in range(1, n + 1):
    if dfs(i, i, {i}):
        result.append(i)

print(len(result))
for x in result:
    print(x)

######################################################################

n = int(input())
arr = [0] * (n + 1)
in_degree = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())
    in_degree[arr[i]] += 1

# 진입 차수가 0인 노드들을 담을 큐(리스트)
queue = [i for i in range(1, n + 1) if in_degree[i] == 0]
removed = [False] * (n + 1)

idx = 0
while idx < len(queue):
    curr = queue[idx]
    removed[curr] = True
    target = arr[curr]
    in_degree[target] -= 1
    if in_degree[target] == 0:
        queue.append(target)
    idx += 1

# 삭제되지 않고 남은 노드들이 사이클의 구성원
ans = [i for i in range(1, n + 1) if not removed[i]]
print(len(ans))
for x in ans:
    print(x)

######################################################################

n = int(input())
f = {i: int(input()) for i in range(1, n + 1)}

# 처음엔 모든 숫자를 후보로 시작
current_set = set(range(1, n + 1))

while True:
    # 현재 집합에 속한 숫자들이 가리키는 값들의 집합 추출
    next_set = {f[x] for x in current_set}
    
    # 두 집합이 일치하면 수렴한 것임
    if next_set == current_set:
        break
    
    # 가리킴을 받지 못한 숫자들이 걸러진 새로운 집합으로 갱신
    current_set = next_set

ans = sorted(list(current_set))
print(len(ans))
for x in ans:
    print(x)

######################################################################

n = int(input())
table = [0] + [int(input()) for _ in range(n)]

# 각 노드 i가 N번 이동했을 때 도달하는 위치를 찾음
# 사이클 외부에 있는 노드는 N번 이동하면 무조건 사이클 안으로 들어오게 됨
reachable_after_n = set()
for i in range(1, n + 1):
    curr = i
    for _ in range(n):
        curr = table[curr]
    reachable_after_n.add(curr)

# 찾아낸 사이클 내부 노드들로부터 다시 사이클 전체를 복원
final_set = set()
for start_node in reachable_after_n:
    curr = start_node
    while curr not in final_set:
        final_set.add(curr)
        curr = table[curr]

ans = sorted(list(final_set))
print(len(ans))
for x in ans:
    print(x)

######################################################################

n = int(input())
adj = [0] * (n + 1)
for i in range(1, n + 1):
    adj[i] = int(input())

is_cycle = [False] * (n + 1)
checked = [False] * (n + 1)

for i in range(1, n + 1):
    if checked[i]: continue
    
    path = []
    curr = i
    while not checked[curr]:
        checked[curr] = True
        path.append(curr)
        curr = adj[curr]
    
    # curr가 현재 탐색 중인 경로(path) 안에 있다면 사이클 발견!
    if curr in path:
        cycle_start_idx = path.index(curr)
        for j in range(cycle_start_idx, len(path)):
            is_cycle[path[j]] = True

ans = [i for i in range(1, n + 1) if is_cycle[i]]
print(len(ans))
for x in ans:
    print(x)

######################################################################


