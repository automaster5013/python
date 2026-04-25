# 입력 받기
n = int(input())
# 대량의 데이터를 한꺼번에 읽어 리스트로 변환
x = sorted(list(map(int, input().split())))

if n % 2 != 0:
    # 홀수일 경우: 정확히 가운데 값
    print(x[n // 2])
else:
    # 짝수일 경우: x[n//2 - 1]부터 x[n//2] 사이의 모든 값이 최솟값 보장
    val1 = x[n // 2 - 1]
    val2 = x[n // 2]
    
    if val1 == val2:
        print(val1)
    else:
        # 두 값이 다르면 오름차순으로 두 좌표 출력
        print(val1, val2)

###########################################################################

n = int(input())
coords = list(map(int, input().split()))

# 1. 빈도수 계산
freq = {}
for c in coords:
    freq[c] = freq.get(c, 0) + 1

# 2. 좌표 정렬 (유니크한 좌표들만)
unique_coords = sorted(freq.keys())

# 3. 누적 빈도가 n/2를 넘어서는 지점 탐색
results = []
accumulated = 0
target_low = (n + 1) / 2
target_high = (n / 2) + 1

for c in unique_coords:
    current_count = freq[c]
    # 이전 누적합과 현재를 더했을 때 중앙 범위를 포함하는지 확인
    if accumulated < target_low <= accumulated + current_count:
        results.append(c)
    elif accumulated < target_high <= accumulated + current_count:
        if c not in results:
            results.append(c)
    
    accumulated += current_count
    if accumulated >= target_high:
        break

print(*(sorted(results)))

###########################################################################

n = int(input())
x = sorted(list(map(int, input().split())))

left = 0
right = n - 1

# 양 끝에서 하나씩 좁혀 들어감
while right - left > 1:
    left += 1
    right -= 1

# 마지막에 남은 후보들 중 유니크한 좌표만 출력
if left == right:
    print(x[left])
else:
    if x[left] == x[right]:
        print(x[left])
    else:
        print(x[left], x[right])

###########################################################################

n = int(input())
x = sorted(list(map(int, input().split())))

# 중앙 후보군 추출 (인덱스 계산 최적화)
# n=5이면 x[2:3], n=8이면 x[3:5]
mid_idx = n // 2
if n % 2 == 1:
    candidates = x[mid_idx : mid_idx + 1]
else:
    candidates = x[mid_idx - 1 : mid_idx + 1]

# 중복 제거 후 오름차순 정렬 출력
ans = sorted(list(set(candidates)))
print(*(ans))

###########################################################################

n = int(input())
x = sorted(list(map(int, input().split())))

# 각 좌표가 '중앙 지점'으로서의 자격이 있는지 검사
# 왼쪽 사람 수(i)와 오른쪽 사람 수(n - 1 - i)의 차이가 1 이하여야 함
ans = []
for i in range(n):
    left_count = i
    right_count = n - 1 - i
    
    # 균형 조건: 어느 한쪽이 과반수를 넘지 않아야 함
    if left_count <= n / 2 and right_count <= n / 2:
        if not ans or ans[-1] != x[i]:
            ans.append(x[i])

print(*(ans))

###########################################################################


