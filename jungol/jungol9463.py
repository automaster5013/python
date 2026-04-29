def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        print(*(arr))

data = list(map(int, input().split()))
bubble_sort(data)

#####################################################################(방법01)

def bubble_sort(arr, n):
    if n == 1:
        return

    for j in range(len(arr) - (len(arr) - n + 1)):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print(*(arr))
    
    bubble_sort(arr, n - 1)

nums = list(map(int, input().split()))
bubble_sort(nums, len(nums))

#####################################################################(방법02)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        print(*(arr))

nums = list(map(int, input().split()))
bubble_sort(nums)

#####################################################################(방법03)

class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def sort_and_log(self):
        d = self.data
        for i in range(len(d) - 1):
            self._pass(len(d) - i)
            print(*(d))

    def _pass(self, limit):
        for j in range(limit - 1):
            if self.data[j] < self.data[j + 1]:
                self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

inp_data = list(map(int, input().split()))
sorter = BubbleSorter(inp_data)
sorter.sort_and_log()

#####################################################################(방법04)

lst = list(map(int,input().split()))
# print(lst)

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

    print(*lst)

#####################################################################(방법05)



