
# 1. (선택)정렬

# 2. (삽입)정렬

# 3. (버블)정렬

######################################################################

def selection_sort():
    n = int(input())
    # print(n)
    nums = list(map(int, input().split()))

    for i in range(n - 1):
        target = i
        for j in range(i + 1, n):
            if nums[j] < nums[target]:
                target = j
        
        nums[i], nums[target] = nums[target], nums[i]
        
        print(' '.join([str(x) for x in nums]))

selection_sort()

######################################################################(방법01)

def selection_sort():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n - 1):
        sub_min = min(arr[i:])
        min_idx = arr[i:].index(sub_min) + i
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(" ".join(map(str, arr)))

selection_sort()

######################################################################(방법02)

def selection_sort():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n - 1):
        curr_min_idx = i
        for j, val in enumerate(a[i+1:], start=i+1):
            if val < a[curr_min_idx]:
                curr_min_idx = j
        
        a[i], a[curr_min_idx] = a[curr_min_idx], a[i]
        print(*(a))

selection_sort()

######################################################################(방법03)

def find_min_index(arr, start):
    min_val = arr[start]
    min_idx = start
    for k in range(start + 1, len(arr)):
        if arr[k] < min_val:
            min_val = arr[k]
            min_idx = k
    return min_idx

def selection_sort():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    for i in range(n - 1):
        m_idx = find_min_index(arr, i)
        arr[i], arr[m_idx] = arr[m_idx], arr[i]
        print(*(arr))

selection_sort()

######################################################################(방법03)

import sys

def selection_sort():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(*(arr))

selection_sort()

######################################################################(방법05)


