import sys

def solve_v1():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(n - 1):
        min_idx = i
        # 정렬되지 않은 부분에서 최솟값 탐색
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 최솟값을 찾은 위치와 현재 위치 i를 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # 현재 단계의 배열 상태 출력
        print(*(arr))

solve_v1()

######################################################################

def solve_v2():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n - 1):
        # i번째 이후의 부분 배열에서 최솟값 찾기
        sub_min = min(arr[i:])
        # 최솟값이 위치한 인덱스 찾기 (부분 배열에서의 상대 인덱스 + i)
        min_idx = arr[i:].index(sub_min) + i
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(" ".join(map(str, arr)))

solve_v2()

######################################################################

def solve_v3():
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n - 1):
        target = i
        for j in range(i + 1, n):
            if nums[j] < nums[target]:
                target = j
        
        # 파이썬 특유의 튜플 언패킹을 이용한 스왑
        nums[i], nums[target] = nums[target], nums[i]
        
        # 리스트 컴프리헨션으로 문자열 변환 후 출력
        print(' '.join([str(x) for x in nums]))

solve_v3()

######################################################################

def find_min_index(arr, start):
    min_val = arr[start]
    min_idx = start
    for k in range(start + 1, len(arr)):
        if arr[k] < min_val:
            min_val = arr[k]
            min_idx = k
    return min_idx

def solve_v4():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    for i in range(n - 1):
        m_idx = find_min_index(arr, i)
        arr[i], arr[m_idx] = arr[m_idx], arr[i]
        print(*(arr))

solve_v4()

######################################################################

def solve_v5():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n - 1):
        # 현재 위치 i를 기준으로 최소값 인덱스 갱신
        curr_min_idx = i
        for j, val in enumerate(a[i+1:], start=i+1):
            if val < a[curr_min_idx]:
                curr_min_idx = j
        
        a[i], a[curr_min_idx] = a[curr_min_idx], a[i]
        print(*(a))

solve_v5()

######################################################################

