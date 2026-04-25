# 입력 받기
n = int(input())
meetings = []

for i in range(1, n + 1):
    # input().split()을 사용해 공백 기준 분리
    s, e = map(int, input().split())
    # (회의 길이, 시작 시간, 원본 인덱스) 순으로 저장
    meetings.append((e - s, s, i))

# Timsort (O(N log N))를 사용한 다중 조건 정렬
meetings.sort()

# 결과 출력
for m in meetings:
    print(m[2])

###############################################################

def merge_sort(arr):
    n = len(arr)
    step = 1
    while step < n:
        for left in range(0, n, step * 2):
            mid = left + step
            right = min(left + step * 2, n)
            if mid < right:
                # 두 구간 병합 로직
                l_idx, r_idx = left, mid
                merged = []
                while l_idx < mid and r_idx < right:
                    # (길이, 시작시간) 비교
                    if arr[l_idx][0] < arr[r_idx][0] or (arr[l_idx][0] == arr[r_idx][0] and arr[l_idx][1] < arr[r_idx][1]):
                        merged.append(arr[l_idx]); l_idx += 1
                    else:
                        merged.append(arr[r_idx]); r_idx += 1
                merged.extend(arr[l_idx:mid])
                merged.extend(arr[r_idx:right])
                arr[left:right] = merged
        step *= 2

# (입력부와 출력부는 방식 1과 동일)

###############################################################

n = int(input())
packed_data = []

for i in range(1, n + 1):
    s, e = map(int, input().split())
    duration = e - s
    # 길이를 30비트 왼쪽으로 밀고 시작 시간을 더함 (10^9 < 2^30)
    # 결과적으로 하나의 정수 안에서 [길이(상위)][시작시간(하위)] 구조가 됨
    key = (duration << 30) | s
    packed_data.append((key, i))

# 단일 키 정렬이므로 튜플 비교보다 빠를 수 있음
packed_data.sort()

for data in packed_data:
    print(data[1])

###############################################################

n = int(input())
meetings = []
for i in range(1, n + 1):
    s, e = map(int, input().split())
    meetings.append([s, e, e - s, i]) # 시작, 끝, 길이, 인덱스

# 1단계: 낮은 순위인 '시작 시간'으로 정렬
meetings.sort(key=lambda x: x[0])

# 2단계: 높은 순위인 '회의 길이'로 다시 정렬 (안정 정렬이므로 시작 시간 순서가 유지됨)
meetings.sort(key=lambda x: x[2])

for m in meetings:
    print(m[3])

###############################################################

def heapify(arr, n, i):
    smallest = i
    l, r = 2 * i + 1, 2 * i + 2
    
    for child in (l, r):
        if child < n:
            # (길이, 시작시간) 비교 로직
            if arr[child][0] < arr[smallest][0] or (arr[child][0] == arr[smallest][0] and arr[child][1] < arr[smallest][1]):
                smallest = child
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

# 정렬 로직 생략 (일반적인 Heap Sort 구조에 위 비교 로직 적용)

###############################################################



