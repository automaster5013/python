# 입력 처리
n, k = map(int, input().split())
target = list(map(int, input().split()))

# 예외 처리: 오름차순이 아니거나 중복이 있는 경우
is_valid = True
if len(target) != k: is_valid = False
for i in range(k - 1):
    if target[i] >= target[i+1]: is_valid = False
for x in target:
    if x < 1 or x > n: is_valid = False

if not is_valid:
    print("None")
else:
    count = 0
    found_rank = -1

    def generate(depth, start, path):
        global count, found_rank
        if depth == k:
            count += 1
            if path == target:
                found_rank = count
            return

        for i in range(start, n + 1):
            if found_rank != -1: return # 이미 찾았으면 중단
            generate(depth + 1, i + 1, path + [i])

    generate(0, 1, [])
    print(found_rank if found_rank != -1 else "None")

#################################################################################

def nCr(n, r):
    if r < 0 or r > n: return 0
    if r == 0 or r == n: return 1
    if r > n // 2: r = n - r
    
    num, den = 1, 1
    for i in range(r):
        num = num * (n - i)
        den = den * (i + 1)
    return num // den

n, k = map(int, input().split())
target = list(map(int, input().split()))

# 유효성 검사
if any(target[i] >= target[i+1] for i in range(k-1)):
    print("None")
else:
    rank = 1
    current_start = 1
    # 각 자리수별로 타겟 숫자보다 작은 숫자가 올 경우의 수를 합산
    for i in range(k):
        for val in range(current_start, target[i]):
            # val을 선택했을 때 남은 자리(k-1-i)를 
            # 남은 숫자(n-val) 중에서 뽑는 경우의 수
            rank += nCr(n - val, k - 1 - i)
        current_start = target[i] + 1
    
    print(rank)

#################################################################################

n, k = map(int, input().split())
target = list(map(int, input().split()))

# 유효성 검사
if any(target[i] >= target[i+1] for i in range(k-1)):
    print("None")
else:
    indices = list(range(1, k + 1))
    count = 1
    found = False

    while True:
        if indices == target:
            found = True
            break
        
        # 다음 조합 생성 (사전순)
        idx = k - 1
        while idx >= 0 and indices[idx] == n - k + idx + 1:
            idx -= 1
        
        if idx < 0: break # 모든 조합 탐색 완료
        
        indices[idx] += 1
        for j in range(idx + 1, k):
            indices[j] = indices[idx] + (j - idx)
        count += 1
    
    print(count if found else "None")

#################################################################################

n, k = map(int, input().split())
target = list(map(int, input().split()))

if any(target[i] >= target[i+1] for i in range(k-1)):
    print("None")
else:
    all_combos = []
    # 1<<n 은 2^n을 의미
    for i in range(1, 1 << n):
        # 켜진 비트의 개수 확인
        bits = []
        for j in range(n):
            if (i >> (n - 1 - j)) & 1:
                bits.append(j + 1)
        
        if len(bits) == k:
            all_combos.append(bits)
    
    # 생성된 조합들을 사전순 정렬
    all_combos.sort()
    
    try:
        print(all_combos.index(target) + 1)
    except ValueError:
        print("None")

#################################################################################

n, k = map(int, input().split())
target = list(map(int, input().split()))

def get_all_combinations(start, r):
    if r == 0: return [[]]
    res = []
    for i in range(start, n + 1):
        for suffix in get_all_combinations(i + 1, r - 1):
            res.append([i] + suffix)
    return res

if any(target[i] >= target[i+1] for i in range(k-1)):
    print("None")
else:
    combos = get_all_combinations(1, k)
    rank = 0
    for i in range(len(combos)):
        if combos[i] == target:
            rank = i + 1
            break
    print(rank if rank > 0 else "None")

#################################################################################


