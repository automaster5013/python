n = int(input())
divisors = []

# i * i <= n 일 때까지만 반복 (시간 복잡도: O(sqrt(N)))
i = 1
while i * i <= n:
    if n % i == 0:
        divisors.append(i)
        # i와 짝이 되는 약수(n // i)가 i와 다르다면 추가
        if i != n // i:
            divisors.append(n // i)
    i += 1

# 오름차순 정렬 후 출력
divisors.sort()
print(*(divisors))

#############################################################

n = int(input())
small_divisors = []
large_divisors = []

i = 1
while i * i <= n:
    if n % i == 0:
        small_divisors.append(i)
        if i != n // i:
            # 큰 약수는 뒤에서부터 붙여주기 위해 임시 저장
            large_divisors.append(n // i)
    i += 1

# large_divisors는 큰 수부터 들어있으므로 뒤집어서 출력
print(*(small_divisors + large_divisors[::-1]))

#############################################################

n = int(input())
res = set()

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        res.add(i)
        res.add(n // i)

# set은 순서가 없으므로 정렬하여 출력
print(*(sorted(res)))

#############################################################

def get_divisors(n):
    # 작은 약수들 먼저 생성
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
    # 큰 약수들 역순으로 생성
    for i in range(int(n**0.5), 0, -1):
        if n % i == 0:
            pair = n // i
            if pair != i:
                yield pair

n = int(input())
# 제너레이터로부터 값을 하나씩 꺼내어 공백 구분 출력
print(*(get_divisors(n)))

#############################################################

n = int(input())

def find(i, limit, low, high):
    if i > limit:
        return low, high
    
    if n % i == 0:
        low.append(i)
        if i != n // i:
            high.append(n // i)
            
    return find(i + 1, limit, low, high)

# 파이썬 재귀 한도를 고려하여 sqrt(N) 수준까지만 실행
limit = int(n**0.5)
low, high = find(1, limit, [], [])

print(*(low + high[::-1]))

#############################################################


