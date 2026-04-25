n = int(input())

for i in range(1, n + 1):
    if i % 2 != 0: # 홀수 행 (1, 3, 5...)
        for j in range(1, n + 1):
            print(j, end=" ")
    else: # 짝수 행 (2, 4, 6...)
        for j in range(n, 0, -1):
            print(j, end=" ")
    print() # 한 행 종료 후 줄바꿈

#################################################

n = int(input())
base = [i for i in range(1, n + 1)]

for i in range(n):
    if i % 2 == 0:
        # 홀수 번째 행 (인덱스는 0, 2...)
        print(*base)
    else:
        # 짝수 번째 행 (인덱스는 1, 3...)
        print(*base[::-1])

#################################################

n = int(input())

for i in range(n):
    for j in range(1, n + 1):
        if i % 2 == 0:
            print(j, end=" ")
        else:
            # 짝수 행일 때: n, n-1, ..., 1 순서로 계산
            print(n - j + 1, end=" ")
    print()

#################################################

n = int(input())

# 두 가지 타입의 행을 문자열로 미리 생성
row_forward = " ".join(str(i) for i in range(1, n + 1))
row_backward = " ".join(str(i) for i in range(n, 0, -1))

for i in range(n):
    if i % 2 == 0:
        print(row_forward)
    else:
        print(row_backward)

#################################################

n = int(input())

for k in range(n * n):
    row = k // n
    col = k % n
    
    if row % 2 == 0:
        # 정방향: 1, 2, 3...
        val = col + 1
    else:
        # 역방향: n, n-1, n-2...
        val = n - col
        
    print(val, end=" ")
    
    # 열의 끝에 도달하면 줄바꿈
    if col == n - 1:
        print()

#################################################


