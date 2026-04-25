data = list(map(int, input().split()))
k = data[0]
s = data[1:]

# 선택할 개수가 6개로 고정되어 있으므로 6중 루프가 가능합니다.
for i in range(k - 5):
    for j in range(i + 1, k - 4):
        for l in range(j + 1, k - 3):
            for m in range(l + 1, k - 2):
                for n in range(m + 1, k - 1):
                    for p in range(n + 1, k):
                        print(s[i], s[j], s[l], s[m], s[n], s[p])

######################################################################

data = list(map(int, input().split()))
k, s = data[0], data[1:]
path = [0] * 6

def combine(depth, start):
    # 기저 조건: 6개를 모두 뽑았을 때
    if depth == 6:
        print(*(path))
        return

    # 현재 위치(start)부터 마지막까지 탐색
    for i in range(start, k):
        path[depth] = s[i]
        combine(depth + 1, i + 1)

combine(0, 0)

######################################################################

data = list(map(int, input().split()))
k, s = data[0], data[1:]

def get_combinations(arr, r):
    # 0개를 뽑는다면 빈 리스트 반환
    if r == 0: return [[]]
    # 남은 원소보다 뽑아야 할 개수가 많으면 불가능
    if len(arr) < r: return []
    
    res = []
    # 1. 첫 번째 원소를 포함하는 경우
    for c in get_combinations(arr[1:], r - 1):
        res.append([arr[0]] + c)
    # 2. 첫 번째 원소를 포함하지 않는 경우
    for c in get_combinations(arr[1:], r):
        res.append(c)
    return res

for comb in get_combinations(s, 6):
    print(*(comb))

######################################################################

data = list(map(int, input().split()))
k, s = data[0], data[1:]

# 초기 인덱스: [0, 1, 2, 3, 4, 5]
indices = list(range(6))

while True:
    # 현재 인덱스에 해당하는 숫자 출력
    print(*(s[i] for i in indices))
    
    # 오른쪽 끝부터 보면서 1씩 올릴 수 있는 인덱스 찾기
    target = -1
    for i in range(5, -1, -1):
        # i번째 인덱스가 가질 수 있는 최대값은 k - 6 + i
        if indices[i] < k - 6 + i:
            target = i
            break
    
    if target == -1: break # 더 이상 올릴 인덱스가 없으면 종료
    
    indices[target] += 1
    # 바뀐 인덱스 오른쪽을 순차적으로 채움
    for j in range(target + 1, 6):
        indices[j] = indices[j-1] + 1

######################################################################

data = list(map(int, input().split()))
k, s = data[0], data[1:]

# 모든 가능한 비트 조합 탐색 (사전순 출력을 위해 역순 처리 등 고려 가능)
# 여기서는 조합의 특성상 큰 수부터 비트를 켜서 검사합니다.
for i in range((1 << k) - 1, -1, -1):
    cnt = 0
    temp_comb = []
    for j in range(k):
        if (i >> (k - 1 - j)) & 1:
            cnt += 1
            temp_comb.append(s[j])
    
    if cnt == 6:
        print(*(temp_comb))

######################################################################



