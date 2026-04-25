# 입력 받기
n = int(input())
# map 객체를 리스트로 변환 (O(N))
ages = list(map(int, input().split()))

# 1. 내장 정렬 (Timsort 이용, O(N log N))
ages.sort()

# 2. 선형 탐색 (O(N))
min_diff = 10**9 + 7 # 충분히 큰 값으로 초기화

for i in range(n - 1):
    diff = ages[i + 1] - ages[i]
    if diff < min_diff:
        min_diff = diff
    
    # 조기 종료(Early Exit): 나이가 같은 경우(0)보다 작은 차이는 없음
    if min_diff == 0:
        break

print(min_diff)

###########################################################################

def merge_sort_iterative(arr):
    n = len(arr)
    width = 1
    while width < n:
        for i in range(0, n, width * 2):
            # 두 구간을 병합: [i:i+width]와 [i+width:i+2*width]
            left, right = i, min(i + width, n)
            end = min(i + 2 * width, n)
            
            merged = []
            l, r = left, right
            while l < right and r < end:
                if arr[l] < arr[r]:
                    merged.append(arr[l]); l += 1
                else:
                    merged.append(arr[r]); r += 1
            merged.extend(arr[l:right])
            merged.extend(arr[r:end])
            arr[left:end] = merged
        width *= 2
    return arr

n = int(input())
ages = list(map(int, input().split()))
sorted_ages = merge_sort_iterative(ages)

ans = sorted_ages[1] - sorted_ages[0]
for i in range(1, n - 1):
    diff = sorted_ages[i+1] - sorted_ages[i]
    if diff < ans: ans = diff
print(ans)

###########################################################################

def heapify(arr, n, i):
    smallest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] < arr[smallest]: smallest = l
    if r < n and arr[r] < arr[smallest]: smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

n = int(input())
ages = list(map(int, input().split()))

# 1. 최소 힙 생성 (Build Heap)
for i in range(n // 2 - 1, -1, -1):
    heapify(ages, n, i)

# 2. 하나씩 꺼내며 비교
min_diff = 2 * 10**9
prev = -1
for i in range(n):
    # 루트(최솟값) 추출
    curr = ages[0]
    if prev != -1:
        min_diff = min(min_diff, curr - prev)
    
    # 마지막 요소를 루트로 보내고 다시 힙화
    ages[0] = ages[n - 1 - i]
    heapify(ages, n - 1 - i, 0)
    prev = curr
    if min_diff == 0: break

print(min_diff)

###########################################################################

n = int(input())
ages = list(map(int, input().split()))

# 32비트 정수 범위 내에서 정렬
for bit in range(31):
    # 0번 버킷과 1번 버킷으로 분리
    zero_bucket = []
    one_bucket = []
    for x in ages:
        if (x >> bit) & 1:
            one_bucket.append(x)
        else:
            zero_bucket.append(x)
    ages = zero_bucket + one_bucket # 안정 정렬 유지

# 정렬된 결과에서 차이 계산
min_diff = ages[1] - ages[0]
for i in range(1, n - 1):
    d = ages[i+1] - ages[i]
    if d < min_diff: min_diff = d
print(min_diff)

###########################################################################

def find_min_diff(arr):
    # 기저 사례: 요소가 2개면 그 차이를 반환
    if len(arr) == 2: return abs(arr[0] - arr[1])
    if len(arr) < 2: return 2 * 10**9

    mid = len(arr) // 2
    # 왼쪽과 오른쪽에서의 최솟값 (정렬되어 있다고 가정)
    d = min(find_min_diff(arr[:mid]), find_min_diff(arr[mid:]))
    
    # 경계 부분 확인: 왼쪽 구역의 최대값과 오른쪽 구역의 최소값 비교
    cross_diff = arr[mid] - arr[mid-1]
    return min(d, cross_diff)

n = int(input())
ages = list(map(int, input().split()))
ages.sort() # 분할 정복을 위해 정렬 선행

print(find_min_diff(ages))

###########################################################################


