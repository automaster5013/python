# 입력 받기
try:
    line = input().split()
    if not line: exit()
    n, m = map(int, line)

    # 범위 체크
    if n < 1 or n > 100 or m < 1 or m > 3:
        print("INPUT ERROR!")
    else:
        if m == 1:
            # 종류 1: 왼쪽 정렬, 증가형
            for i in range(1, n + 1):
                print("*" * i)
        elif m == 2:
            # 종류 2: 왼쪽 정렬, 감소형
            for i in range(n, 0, -1):
                print("*" * i)
        elif m == 3:
            # 종류 3: 중앙 정렬, 피라미드형
            for i in range(1, n + 1):
                # 공백: n-i개, 별: 2*i-1개
                print(" " * (n - i) + "*" * (2 * i - 1))
except:
    print("INPUT ERROR!")

####################################################################

n_m = input().split()
if len(n_m) < 2: 
    print("INPUT ERROR!")
else:
    n, m = int(n_m[0]), int(n_m[1])
    if 1 <= n <= 100 and 1 <= m <= 3:
        for i in range(1, n + 1):
            if m == 1:
                for j in range(i): print("*", end="")
                print()
            elif m == 2:
                for j in range(n - i + 1): print("*", end="")
                print()
            elif m == 3:
                # 공백 루프
                for j in range(n - i): print(" ", end="")
                # 별 루프
                for j in range(2 * i - 1): print("*", end="")
                print()
    else:
        print("INPUT ERROR!")

####################################################################

n_m = input().split()
n, m = (int(n_m[0]), int(n_m[1])) if len(n_m) == 2 else (0, 0)

if not (1 <= n <= 100 and 1 <= m <= 3):
    print("INPUT ERROR!")
else:
    output = []
    for i in range(1, n + 1):
        if m == 1:
            line = "*" * i
        elif m == 2:
            line = "*" * (n - i + 1)
        else:
            line = " " * (n - i) + "*" * (2 * i - 1)
        output.append(line)
    
    # 리스트의 모든 요소를 줄바꿈(\n)으로 합쳐서 한 번에 출력
    print("\n".join(output))

####################################################################

raw = input().split()
if len(raw) == 2 and raw[0].isdigit() and raw[1].isdigit():
    n, m = map(int, raw)
    if 1 <= n <= 100 and 1 <= m <= 3:
        # 각 종류별 규칙 정의
        patterns = {
            1: lambda i: "*" * i,
            2: lambda i: "*" * (n - i + 1),
            3: lambda i: " " * (n - i) + "*" * (2 * i - 1)
        }
        for i in range(1, n + 1):
            print(patterns[m](i))
    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")

####################################################################

def draw(curr, n, m):
    if curr > n:
        return
    
    # 현재 줄 출력
    if m == 1:
        print("*" * curr)
    elif m == 2:
        print("*" * (n - curr + 1))
    elif m == 3:
        print(" " * (n - curr) + "*" * (2 * curr - 1))
    
    # 다음 줄 호출
    draw(curr + 1, n, m)

# 메인 실행부
raw_data = input().split()
try:
    n, m = map(int, raw_data)
    if 1 <= n <= 100 and 1 <= m <= 3:
        draw(1, n, m)
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

####################################################################


