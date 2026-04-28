def bubble_sort(n, arr):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        print(arr)

N = int(input())
nums = list(map(int, input().split()))

bubble_sort(N, nums)

###################################################################(방법01)

def bubble_sort(n, arr):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(arr)

N = int(input())
nums = list(map(int, input().split()))

bubble_sort(N, nums)

###################################################################(방법02)

def bubble_sort(arr, n, current_pass=1):
    if current_pass == n:
        return
    
    for x in range(len(arr) - current_pass):
        if arr[x] > arr[x + 1]:
            arr[x], arr[x + 1] = arr[x + 1], arr[x]
            
    print(arr)
    bubble_sort(arr, n, current_pass + 1)   # 재귀함수 호출

N = int(input())
nums = list(map(int, input().split()))

bubble_sort(nums, N)

###################################################################(방법03)











