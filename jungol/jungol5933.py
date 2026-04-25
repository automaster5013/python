n = int(input())

for i in range(1, n + 1): # 행(Row): 1부터 n까지
    for j in range(1, n + 1): # 열(Column): 1부터 n까지
        # 현재 행 번호와 열 번호를 곱한 결과 출력
        print(i * j, end=" ")
    print() # 한 행이 끝나면 줄바꿈

###########################################################

n = int(input())

for i in range(1, n + 1):
    # i행에 들어갈 숫자들을 리스트로 생성 [i*1, i*2, ..., i*n]
    row = [i * j for j in range(1, n + 1)]
    # 리스트를 풀어헤쳐(Unpacking) 출력
    print(*row)

###########################################################

n = int(input())

for i in range(1, n + 1):
    current_val = 0
    for j in range(n):
        current_val += i # 매 칸마다 행 번호(i)만큼 더함
        print(current_val, end=" ")
    print()

###########################################################

n = int(input())

for k in range(n * n):
    # 행 번호: k // n, 열 번호: k % n
    row = (k // n) + 1
    col = (k % n) + 1
    
    print(row * col, end=" ")
    
    # 열의 끝(n번째 칸)에 도달하면 줄바꿈
    if col == n:
        print()

###########################################################

n = int(input())

for i in range(1, n + 1):
    # 각 숫자를 계산 후 문자열로 변환하여 리스트 생성
    row_str = []
    for j in range(1, n + 1):
        row_str.append(str(i * j))
    
    # 리스트 요소들을 공백으로 묶어 한 번에 출력
    print(" ".join(row_str))

###########################################################

