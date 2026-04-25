n_input = input()
if not n_input.isdigit():
    print("INPUT ERROR")
else:
    n = int(n_input)
    # 홀수 조건 및 범위 체크
    if n % 2 == 0 or n < 1 or n > 100:
        print("INPUT ERROR")
    else:
        mid = n // 2
        # 빈 격자 생성 (행: n개, 열: mid + 1개)
        matrix = [["" for _ in range(mid + 1)] for _ in range(n)]
        
        char_code = 0
        # 오른쪽 열(mid)부터 왼쪽 열(0)까지 역순 진행
        for j in range(mid, -1, -1):
            # 각 열마다 채울 행의 범위는 j부터 n-1-j까지
            for i in range(j, n - j):
                matrix[i][j] = chr(65 + (char_code % 26))
                char_code += 1
        
        # 출력
        for row in matrix:
            # 비어있지 않은 문자만 골라서 출력
            res = [c for c in row if c != ""]
            print(" ".join(res))

#########################################################################

try:
    n = int(input())
    if n % 2 == 0 or n < 1 or n > 100:
        print("INPUT ERROR")
    else:
        mid = n // 2
        for i in range(n):
            row_data = []
            # 각 행 i가 가질 수 있는 열 j의 범위 결정
            # j는 mid부터 시작해서 왼쪽으로 오다가 i의 거리에 막힘
            # 0 <= j <= i 이고 j <= n-1-i 여야 함
            for j in range(mid + 1):
                if j <= i and j <= n - 1 - i:
                    # (i, j)가 몇 번째 문자인지 계산하는 공식:
                    # (오른쪽 열들의 총 개수) + (현재 열에서의 상대 위치)
                    # 총 번호 = (mid - j)^2 + (i - j)
                    order = (mid - j)**2 + (i - j)
                    row_data.append(chr(65 + (order % 26)))
            print(" ".join(row_data))
except:
    print("INPUT ERROR")

#########################################################################

n_raw = input()
if not n_raw.replace('-','').isdigit(): # 음수 처리 포함
    print("INPUT ERROR")
else:
    n = int(n_raw)
    if n % 2 == 0 or n < 1 or n > 100:
        print("INPUT ERROR")
    else:
        mid = n // 2
        triangle = [[] for _ in range(n)]
        char_val = 0
        
        # 오른쪽에서 왼쪽으로 열 단위 생성
        for j in range(mid, -1, -1):
            # i는 위에서 아래로
            for i in range(j, n - j):
                triangle[i].append(chr(65 + (char_val % 26)))
                char_val += 1
        
        # 주의: 위의 순서대로 append하면 리스트 내부는 [A], [B, C], [D, E, F] 순임
        # 하지만 출력은 왼쪽 열부터 보여줘야 하므로 리스트를 뒤집어서 출력
        for row in triangle:
            print(" ".join(row[::-1]))

#########################################################################

import sys # 입력을 위해 sys 사용 가능하나 input()으로 대체

data = input()
if not data.isdigit() or int(data) % 2 == 0 or not (1 <= int(data) <= 100):
    print("INPUT ERROR")
else:
    n = int(data)
    mid = n // 2
    # 총 필요한 문자의 개수는 (mid+1)^2
    total_needed = (mid + 1) ** 2
    alphabet_stream = [chr(65 + (k % 26)) for k in range(total_needed)]
    
    matrix = [[""] * (mid + 1) for _ in range(n)]
    curr = 0
    
    # 열 단위로 잘라서 배치
    for j in range(mid, -1, -1):
        num_in_col = n - 2 * j
        # 해당 열에 들어갈 문자들 추출
        col_chars = alphabet_stream[curr : curr + num_in_col]
        curr += num_in_col
        
        # 행 위치에 맞게 삽입
        for idx, i in enumerate(range(j, n - j)):
            matrix[i][j] = col_chars[idx]
            
    for row in matrix:
        print(" ".join([c for c in row if c]))

#########################################################################

n_str = input()
try:
    n = int(n_str)
    if n % 2 == 0 or n < 1 or n > 100: raise ValueError
except:
    print("INPUT ERROR")
else:
    mid = n // 2
    res = [{} for _ in range(n)] # 각 행을 딕셔너리로 관리
    
    c = mid
    r = mid
    char_cnt = 0
    
    while c >= 0:
        # 현재 열 c의 시작 행 r은 c와 같음
        for r in range(c, n - c):
            res[r][c] = chr(65 + (char_cnt % 26))
            char_cnt += 1
        # 왼쪽 열로 이동
        c -= 1
        
    for i in range(n):
        # 딕셔너리의 키(열 번호) 순서대로 정렬하여 출력
        sorted_keys = sorted(res[i].keys())
        print(" ".join([res[i][k] for k in sorted_keys]))

#########################################################################

