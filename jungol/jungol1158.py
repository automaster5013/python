import sys

def solve_v1():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    # 1번째 인덱스부터 마지막까지 순회
    for i in range(1, n):
        target = arr[i]
        j = i - 1
        
        # 정렬된 앞부분을 역순으로 훑으며 target보다 큰 값은 뒤로 밀기
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
            
        # 알맞은 위치에 삽입
        arr[j + 1] = target
        
        # 현재 단계의 리스트 상태 출력
        print(*(arr))

solve_v1()

##############################################################################

def solve_v2():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n):
        target = arr[i]
        
        # 들어갈 위치(pos) 찾기
        pos = i
        for j in range(i - 1, -1, -1):
            if arr[j] > target:
                pos = j
            else:
                break
        
        # 원래 위치에서 빼서 새 위치에 넣기
        arr.insert(pos, arr.pop(i))
        print(" ".join(map(str, arr)))

solve_v2()

##############################################################################

def solve_v3():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n):
        # 현재 원소를 왼쪽 원소와 비교하며 작으면 계속 교체
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                # 더 이상 작지 않으면 정렬된 상태이므로 중단
                break
        print(*(a))

solve_v3()

##############################################################################

def solve_v4():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    for i in range(1, n):
        key = arr[i]
        # key가 들어갈 인덱스 찾기
        idx = i
        while idx > 0 and arr[idx-1] > key:
            idx -= 1
        
        # idx 위치부터 i-1까지 한 칸씩 밀고 key 삽입
        arr = arr[:idx] + [key] + arr[idx:i] + arr[i+1:]
        print(*(arr))

solve_v4()

##############################################################################

import bisect

def solve_v5():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n):
        target = arr.pop(i)
        # 0부터 i까지의 정렬된 부분에서 target이 들어갈 위치 탐색
        idx = bisect.bisect_right(arr[:i], target)
        arr.insert(idx, target)
        print(*(arr))

solve_v5()

##############################################################################




