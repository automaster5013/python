def solve():
    # 1. 입력 처리: 앞뒤 공백을 제거하여 정수로 변환
    try:
        import sys
        # sys.stdin.read().split()을 쓰면 대량의 공백이나 줄바꿈도 안전하게 처리됩니다.
        raw_data = sys.stdin.read().split()
        if not raw_data:
            return
        n = int(raw_data[0])
    except (ValueError, EOFError):
        # 숫자가 아니거나 입력이 없는 경우
        print("INPUT ERROR!")
        return

    # 2. 조건 검사: 1~100 사이의 양의 홀수여야 함
    if 1 <= n <= 100 and n % 2 == 1:
        mid = n // 2
        
        # 3. 별 출력 루프
        for i in range(n):
            if i <= mid:
                # 상단(중간 포함): 공백은 i개, 별은 2*i+1개
                spaces = i
                stars = 2 * i + 1
            else:
                # 하단: 공백은 (n-1-i)개, 별은 2*(n-1-i)+1개
                # 대칭성을 이용하여 n-1-i를 기준으로 계산
                spaces = n - 1 - i
                stars = 2 * (n - 1 - i) + 1
            
            # 4. 출력: 줄 끝에 공백이 생기지 않도록 주의
            print(" " * spaces + "*" * stars)
    else:
        # 범위를 벗어나거나 짝수인 경우
        print("INPUT ERROR!")

if __name__ == "__main__":
    solve()

############################################################################

def solve_math():
    try:
        raw = input().split()
        if not raw: return
        n = int(raw[0])
        
        if 1 <= n <= 100 and n % 2 == 1:
            mid = n // 2
            for i in range(n):
                # 중심(mid)으로부터의 거리를 이용한 역전파 계산
                # distance: mid에서 얼마나 떨어져 있는가 (mid, mid-1, ..., 0, ..., mid)
                dist = abs(mid - i)
                # k는 실제 출력될 행의 '상대적 인덱스' (0, 1, 2, 3, 2, 1, 0 순서)
                k = mid - dist
                
                print(" " * k + "*" * (2 * k + 1))
        else:
            print("INPUT ERROR!")
    except:
        print("INPUT ERROR!")

solve_math()

############################################################################

def solve_mirror():
    line = input().split()
    if not line or not line[0].isdigit():
        print("INPUT ERROR!"); return
    
    n = int(line[0])
    if 1 <= n <= 100 and n % 2 == 1:
        mid = n // 2
        # 1. 중간(mid) 줄까지만 리스트에 담기
        rows = [" " * i + "*" * (2 * i + 1) for i in range(mid + 1)]
        
        # 2. 윗부분(rows)과 아랫부분(rows를 뒤집은 것)을 합쳐서 출력
        # rows[:-1][::-1]은 중간 줄을 제외한 나머지를 거꾸로 뒤집은 리스트
        full_triangle = rows + rows[:-1][::-1]
        
        print("\n".join(full_triangle))
    else:
        print("INPUT ERROR!")

solve_mirror()

############################################################################

def solve_simulation():
    try:
        n = int(input())
        if not (1 <= n <= 100 and n % 2 == 1):
            raise ValueError
            
        sp, st = 0, 1 # 시작 공백 0개, 별 1개
        step = 1      # 증가/감소 방향
        
        for i in range(n):
            print(" " * sp + "*" * st)
            
            # 중간 줄에 도달하면 방향을 바꿈
            if i == n // 2:
                step = -1
            
            sp += step
            st += 2 * step
            
    except:
        print("INPUT ERROR!")

solve_simulation()

############################################################################

def row_factory(n):
    mid = n // 2
    for i in range(n):
        # 현재 행의 대칭 계수 계산
        k = mid - abs(mid - i)
        yield " " * k + "*" * (2 * k + 1)

def solve_functional():
    data = input().split()
    try:
        n = int(data[0])
        if 1 <= n <= 100 and n % 2 == 1:
            # factory에서 생성된 줄들을 하나씩 꺼내어 출력
            for row in row_factory(n):
                print(row)
        else:
            print("INPUT ERROR!")
    except:
        print("INPUT ERROR!")

solve_functional()

############################################################################

