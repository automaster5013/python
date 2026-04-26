import sys

def solve_v1():
    # 입력 받기
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    # 버블 정렬 시작 (N-1단계 반복)
    for i in range(n - 1):
        # 뒤에서부터 i개는 이미 정렬되어 확정된 상태
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # 인접한 두 수의 자리를 바꿈 (Swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        # 각 단계가 끝날 때마다 결과 출력
        print(*(arr))

solve_v1()

#####################################################################

def solve_v2():
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        
        # 단계별 출력
        print(" ".join(map(str, nums)))
        # 만약 교환이 한 번도 안 일어났다면 이미 정렬된 것이지만, 
        # 문제 요구사항에 따라 N-1번 끝까지 수행하는 것이 안전합니다.

solve_v2()

#####################################################################

def solve_v3():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    step_end = n - 1
    while step_end > 0:
        for j in range(step_end):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        
        print(*(a))
        step_end -= 1

solve_v3()

#####################################################################

def bubble_pass(arr, last_idx):
    if last_idx == 0:
        return
    
    for j in range(last_idx):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
    print(*(arr))
    # 다음 단계 수행 (확정된 마지막 칸 제외)
    bubble_pass(arr, last_idx - 1)

def solve_v4():
    import sys
    sys.setrecursionlimit(2000) # 재귀 깊이 설정
    line1 = sys.stdin.readline()
    if not line1: return
    n = int(line1)
    nums = list(map(int, sys.stdin.readline().split()))
    
    bubble_pass(nums, n - 1)

solve_v4()

#####################################################################

class BubbleSorter:
    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def sort_and_print(self):
        for step in range(self.n - 1):
            self._single_pass(self.n - 1 - step)
            print(*(self.data))

    def _single_pass(self, end_idx):
        for j in range(end_idx):
            if self.data[j] > self.data[j+1]:
                self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

def solve_v5():
    n = int(input())
    arr = list(map(int, input().split()))
    sorter = BubbleSorter(arr)
    sorter.sort_and_print()

solve_v5()

#####################################################################


