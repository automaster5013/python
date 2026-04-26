import sys

def solve_v1():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    total_moves = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # 앞의 원소가 현재 key보다 크면 한 칸씩 뒤로 밀어냄
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            total_moves += 1 # 이동 발생 카운트
            j -= 1
        
        arr[j + 1] = key
        
    print(total_moves)

solve_v1()

########################################################################

def solve_v2():
    n = int(input())
    a = list(map(int, input().split()))
    moves = 0
    
    for i in range(1, n):
        key = a[i]
        target_idx = i
        
        # 들어갈 자리를 찾으면서 이동 횟수를 미리 계산하지 않고
        # 탐색이 끝난 후 인덱스 차이만큼 더해줌
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        
        # 원래 인덱스 i에서 바뀐 인덱스 j+1까지의 거리만큼 이동 발생
        moves += (i - (j + 1))
        a[j+1] = key
        
    print(moves)

solve_v2()

########################################################################

def solve_v3():
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = 0
    sorted_part = [arr[0]]
    
    for i in range(1, n):
        key = arr[i]
        # 현재까지 정렬된 원소들 중 key보다 큰 녀석들의 개수 = 밀려날 횟수
        moves = len([x for x in sorted_part if x > key])
        total += moves
        
        # 다음 단계를 위해 정렬 상태 유지하며 삽입
        import bisect
        bisect.insort(sorted_part, key)
        
    print(total)

solve_v3()

########################################################################

def solve_v4():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    ans = 0
    for i in range(1, n):
        curr = arr[i]
        # 들어갈 위치 탐색
        dest = i
        for j in range(i):
            if arr[j] > curr:
                dest = j
                break
        
        # 이동 횟수 누적 (i번 위치에서 dest번 위치로 가기 위해 i-dest개가 밀림)
        if dest < i:
            ans += (i - dest)
            arr.pop(i)
            arr.insert(dest, curr)
            
    print(ans)

solve_v4()

########################################################################

def solve_v5():
    # 삽입 정렬의 총 이동 횟수 = Inversion Count
    n = int(input())
    arr = list(map(int, input().split()))
    
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            # 앞에 있는 놈이 뒤에 있는 놈보다 크면 언젠가는 이동해야 함
            if arr[i] > arr[j]:
                inversions += 1
                
    print(inversions)

solve_v5()

########################################################################


