# 입력 처리
n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)] # 조립 관계 (부품 -> 상위부품)
in_degree = [0] * (n + 1)      # 나를 필요로 하는 부품의 수
needs = [[] for _ in range(n + 1)] # 나를 구성하는 부품 (상위 -> 하위)
is_basic = [True] * (n + 1)    # 기본 부품 여부

for _ in range(m):
    x, y, k = map(int, input().split())
    needs[x].append((y, k))
    in_degree[y] += 1
    is_basic[x] = False # 다른 부품을 필요로 하면 기본 부품이 아님

# 필요한 부품의 총 개수를 저장할 배열
required = [0] * (n + 1)
required[n] = 1 # 완제품 1개를 만드는 것이 목표

# 위상 정렬을 위한 큐 (라이브러리 없이 리스트로 구현)
queue = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

head = 0
while head < len(queue):
    curr = queue[head]
    head += 1
    
    # curr를 구성하는 하위 부품들(y)에게 개수 전달
    for y, k in needs[curr]:
        required[y] += required[curr] * k
        in_degree[y] -= 1
        if in_degree[y] == 0:
            queue.append(y)

# 결과 출력: 기본 부품만 번호 순서대로
for i in range(1, n + 1):
    if is_basic[i]:
        print(i, required[i])

####################################################################

n = int(input())
m = int(input())
recipe = [[] for _ in range(n + 1)]
is_basic = [True] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    recipe[x].append((y, k))
    is_basic[x] = False

memo = {}

def get_basic_parts(item):
    # 기본 부품이면 자기 자신 1개 반환
    if is_basic[item]:
        return {item: 1}
    
    # 이미 계산한 적이 있다면 결과 반환
    if item in memo:
        return memo[item]
    
    total_needed = {}
    for sub_item, count in recipe[item]:
        # 하위 부품이 필요한 기본 부품 목록을 가져옴
        sub_basic_parts = get_basic_parts(sub_item)
        for part_id, part_count in sub_basic_parts.items():
            total_needed[part_id] = total_needed.get(part_id, 0) + part_count * count
            
    memo[item] = total_needed
    return total_needed

results = get_basic_parts(n)
# 정렬하여 출력
for p_id in sorted(results.keys()):
    print(p_id, results[p_id])

####################################################################

n = int(input())
m = int(input())

# matrix[i][j]: i를 만드는 데 j가 몇 개 필요한가?
matrix = [[0] * (n + 1) for _ in range(n + 1)]
is_intermediate = [False] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    matrix[x][y] = k
    is_intermediate[x] = True

required = [0] * (n + 1)
required[n] = 1

# 부품 번호가 큰 것부터 처리 (일반적으로 완제품 번호가 가장 큼)
# 하지만 순서가 보장되지 않을 수 있으므로 '중간 부품'들만 골라 여러 번 반복하거나
# 위상 정렬 순서로 처리하는 것이 안전함
for i in range(n, 0, -1):
    if required[i] > 0 and is_intermediate[i]:
        for j in range(1, n + 1):
            if matrix[i][j] > 0:
                required[j] += required[i] * matrix[i][j]
                # 중간 부품의 수량은 기본 부품 계산에 쓰인 뒤 0으로 비움 (중복 계산 방지)
        required[i] = 0 

for i in range(1, n + 1):
    if required[i] > 0:
        print(i, required[i])

####################################################################

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
parents_count = [0] * (n + 1)
is_basic = [True] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    adj[x].append((y, k))
    parents_count[y] += 1
    is_basic[x] = False

required = [0] * (n + 1)
required[n] = 1
processed = [0] * (n + 1) # 나를 필요로 하는 부품 중 처리가 끝난 수

# 완제품부터 시작하여 하위로 전파
stack = [n]
while stack:
    curr = stack.pop()
    for y, k in adj[curr]:
        required[y] += required[curr] * k
        processed[y] += 1
        # 나를 지목한 모든 상위 부품의 계산이 끝났을 때만 아래로 이동
        if processed[y] == parents_count[y]:
            stack.append(y)

for i in range(1, n + 1):
    if is_basic[i]:
        print(i, required[i])

####################################################################

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
basic = [True] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))
    basic[x] = False

# dp[i] = {기본부품번호: 개수, ...}
dp = [{} for _ in range(n + 1)]

def solve(u):
    if basic[u]:
        return {u: 1}
    if dp[u]:
        return dp[u]
    
    res = {}
    for v, k in graph[u]:
        sub_res = solve(v)
        for part, count in sub_res.items():
            res[part] = res.get(part, 0) + count * k
    dp[u] = res
    return res

final_parts = solve(n)
for part_num in sorted(final_parts.keys()):
    print(part_num, final_parts[part_num])

####################################################################


