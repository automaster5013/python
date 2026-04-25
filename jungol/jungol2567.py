# 입력 받기
n, p = map(int, input().split())

history = []
curr = n

# 현재 숫자가 이전에 나온 적이 없을 때까지 반복
while curr not in history:
    history.append(curr)
    # 다음 항 계산: (이전 항 * n) % p
    curr = (curr * n) % p

# 사이클의 길이 = 전체 길이 - 반복이 시작된 지점의 인덱스
print(len(history) - history.index(curr))

###############################################################

n, p = map(int, input().split())

# {숫자: 나타난 순서} 저장
visited = {}
curr = n
order = 0

while curr not in visited:
    visited[curr] = order
    curr = (curr * n) % p
    order += 1

# 현재 순서(전체 개수)에서 처음 발견된 순서를 빼면 사이클의 길이
print(order - visited[curr])

###############################################################

n, p = map(int, input().split())

# 숫자의 범위가 최대 1000이므로 1001 크기의 배열 준비 (-1로 초기화)
check = [-1] * 1001
curr = n
count = 0

while check[curr] == -1:
    check[curr] = count
    curr = (curr * n) % p
    count += 1

print(count - check[curr])

###############################################################

n, p = map(int, input().split())

# 수열을 생성하는 함수 정의
def get_next(val):
    return (val * n) % p

# 1. 만나는 지점 찾기
tortoise = get_next(n)
hare = get_next(get_next(n))

while tortoise != hare:
    tortoise = get_next(tortoise)
    hare = get_next(get_next(hare))

# 2. 사이클의 시작점 찾기
tortoise = n
while tortoise != hare:
    tortoise = get_next(tortoise)
    hare = get_next(hare)

# 3. 사이클의 길이 측정
length = 1
hare = get_next(tortoise)
while tortoise != hare:
    hare = get_next(hare)
    length += 1

print(length)

###############################################################

n, p = map(int, input().split())

def find_cycle(curr, path):
    # 만약 현재 숫자가 이미 경로에 있다면 길이 반환
    for i in range(len(path)):
        if path[i] == curr:
            return len(path) - i
    
    # 경로에 현재 숫자 추가 후 다음 단계 진행
    path.append(curr)
    return find_cycle((curr * n) % p, path)

# 초기값 n과 빈 리스트로 시작
print(find_cycle(n, []))

###############################################################


