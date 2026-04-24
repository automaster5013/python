n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            # 짝수 행: 정방향 (i*m + j + 1)
            num = i * m + j + 1
        else:
            # 홀수 행: 역방향 (i*m + (m-1-j) + 1)
            num = i * m + (m - j)
        print(num, end=' ')
    print() # 줄바꿈

######################################################

n, m = map(int, input().split())

for i in range(n):
    # 일단 해당 행의 숫자를 순서대로 생성
    row = list(range(i * m + 1, (i + 1) * m + 1))
    
    # 홀수 행이면 리스트를 뒤집음
    if i % 2 != 0:
        row = row[::-1]
    
    # 언패킹(*)을 사용해 공백 구분 출력
    print(*row)

######################################################

n, m = map(int, input().split())

current_num = 1
for i in range(n):
    row = []
    if i % 2 == 0:
        # 정방향: 뒤에다 하나씩 추가 (Append)
        for _ in range(m):
            row.append(current_num)
            current_num += 1
    else:
        # 역방향: 앞에다 하나씩 추가 (Prepend)
        for _ in range(m):
            row.insert(0, current_num)
            current_num += 1
    print(*row)

######################################################

n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        # 짝수행: i*m + 1 부터 시작, 1씩 증가
        start, end, step = i * m + 1, (i + 1) * m + 1, 1
    else:
        # 홀수행: (i+1)*m 부터 시작, 1씩 감소
        start, end, step = (i + 1) * m, i * m, -1
        
    for num in range(start, end, step):
        print(num, end=' ')
    print()

######################################################

n, m = map(int, input().split())

row = 0
while row < n:
    if row % 2 == 0:
        col = 0
        while col < m:
            print(row * m + col + 1, end=' ')
            col += 1
    else:
        col = m - 1
        while col >= 0:
            print(row * m + col + 1, end=' ')
            col -= 1
    print() # 한 행 종료
    row += 1

######################################################


