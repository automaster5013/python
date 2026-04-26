def solve_standard():
    try:
        n = int(input())
        # 조건: 1~50 사이의 홀수
        if 1 <= n <= 50 and n % 2 != 0:
            for i in range(n):
                # 1. 왼쪽 공백 생성 (2 * i개)
                indent = " " * (2 * i)
                # 2. 숫자 리스트 생성 후 공백으로 합치기
                content = " ".join([str(i)] * (2 * (n - i) - 1))
                print(indent + content)
        else:
            print("INPUT ERROR!")
    except ValueError:
        print("INPUT ERROR!")

solve_standard()

######################################################################

def solve_nested():
    data = input().split()
    if not data or not data[0].isdigit():
        print("INPUT ERROR!"); return
    
    n = int(data[0])
    if 1 <= n <= 50 and n % 2 != 0:
        for i in range(n):
            # 공백 출력
            for _ in range(2 * i):
                print(" ", end="")
            
            # 숫자 출력
            count = 2 * (n - i) - 1
            for j in range(count):
                print(i, end="")
                # 마지막 숫자 뒤에는 공백을 붙이지 않음
                if j < count - 1:
                    print(" ", end="")
            print()
    else:
        print("INPUT ERROR!")

solve_nested()

######################################################################

def solve_buffered():
    try:
        n = int(input())
        if not (1 <= n <= 50 and n % 2 != 0):
            print("INPUT ERROR!"); return
            
        output = []
        for i in range(n):
            indent = " " * (2 * i)
            # 리스트 컴프리헨션으로 행 데이터 생성
            row_data = [str(i) for _ in range(2 * (n - i) - 1)]
            output.append(indent + " ".join(row_data))
            
        # 모든 행을 줄바꿈 문자로 합쳐 한 번에 출력
        print("\n".join(output))
    except:
        print("INPUT ERROR!")

solve_buffered()

######################################################################

def draw_row(current_row, total_n):
    # 기저 사례: 모든 행을 다 그렸을 때
    if current_row == total_n:
        return
    
    indent = " " * (2 * current_row)
    count = 2 * (total_n - current_row) - 1
    content = " ".join([str(current_row)] * count)
    print(indent + content)
    
    # 다음 행 호출
    draw_row(current_row + 1, total_n)

def solve_recursive():
    try:
        val = input()
        n = int(val)
        if 1 <= n <= 50 and n % 2 != 0:
            draw_row(0, n)
        else:
            print("INPUT ERROR!")
    except:
        print("INPUT ERROR!")

solve_recursive()

######################################################################

def solve_matrix():
    try:
        n = int(input())
        if not (1 <= n <= 50 and n % 2 != 0):
            print("INPUT ERROR!"); return
            
        # 결과물은 최대 가로 2n-1개의 숫자가 들어가는 형태 (공백 포함 시 더 넓음)
        # 여기서는 각 행의 문자열을 미리 조립하는 방식을 취함
        grid = [None] * n
        
        for i in range(n):
            # 행 인덱스 i를 사용하여 해당 줄의 특성 정의
            num_elements = 2 * (n - i) - 1
            row_str = " " * (2 * i)
            
            # 각 요소를 배치
            for j in range(num_elements):
                row_str += str(i)
                if j < num_elements - 1:
                    row_str += " "
            grid[i] = row_str
            
        for row in grid:
            print(row)
    except:
        print("INPUT ERROR!")

solve_matrix()

######################################################################

def solve():
    raw = input().split()
    if not raw or not raw[0].isdigit():
        print("INPUT ERROR!"); return
        
    n = int(raw[0])
    if 1 <= n <= 50 and n % 2 == 1:
        mid = n // 2 + 1
        rows = []
        
        # 중간까지 각 줄을 리스트로 생성
        for i in range(1, mid + 1):
            row = [str(j) for j in range(1, i + 1)]
            rows.append(" ".join(row))
            
        # 상단 출력
        for r in rows:
            print(r)
        # 하단 출력 (마지막 줄 제외하고 역순)
        for r in rows[-2::-1]:
            print(r)
    else:
        print("INPUT ERROR!")

solve()

######################################################################

try:
    n = int(input())
    if 1 <= n <= 50 and n % 2 == 1:
        m = n // 2
        for i in range(n):
            # m - |m - i|는 0, 1, 2, ..., m, ..., 1, 0 순서로 변함
            # 여기에 1을 더해 개수를 맞춤
            count = m - abs(m - i) + 1
            nums = [str(j) for j in range(1, count + 1)]
            print(" ".join(nums))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

######################################################################

line = input().split()
try:
    n = int(line[0])
    if 1 <= n <= 50 and n % 2 == 1:
        current_row = []
        mid = n // 2 + 1
        
        for i in range(1, n + 1):
            if i <= mid:
                # 중간 전까지는 숫자 추가
                current_row.append(str(i))
            else:
                # 중간 이후부터는 마지막 숫자 제거
                current_row.pop()
            print(" ".join(current_row))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

######################################################################

def triangle_gen(n):
    mid = n // 2
    for i in range(n):
        # 대칭 구조의 높이(k) 계산
        k = mid - abs(mid - i) + 1
        yield " ".join(str(x) for x in range(1, k + 1))

try:
    n_in = int(input())
    if 1 <= n_in <= 50 and n_in % 2 == 1:
        # 제너레이터로부터 한 줄씩 받아서 출력
        for row in triangle_gen(n_in):
            print(row)
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

######################################################################


