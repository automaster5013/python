def method1():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    s, e = int(data[0]), int(data[1])

    step = 1 if s <= e else -1
    # s부터 e까지 포함하기 위해 e + step을 종료값으로 설정
    for dan in range(s, e + step, step):
        for i in range(1, 10):
            # 식 사이 공백 3개, 결과값은 2자리 우측 정렬
            print(f"{dan} * {i} = {i*dan:>2}", end="   ")
            if i % 3 == 0:
                print()
        print() # 단 사이 한 줄 비우기

method1()

###################################################################

def method2():
    import sys
    line = sys.stdin.readline().split()
    if not line: return
    s, e = map(int, line)

    count = abs(s - e) + 1
    direction = 1 if s <= e else -1

    for i in range(count):
        curr_dan = s + (i * direction)
        # 1~9까지 3개씩 끊어서 출력
        for j in range(1, 10):
            res = curr_dan * j
            suffix = "   " if j % 3 != 0 else "\n"
            sys.stdout.write(f"{curr_dan} * {j} = {res:>2}{suffix}")
        sys.stdout.write("\n")

method2()

###################################################################

def method3():
    import sys
    def print_dan(curr, target, step):
        for i in range(1, 10):
            print(f"{curr} * {i} = {i*curr:>2}", end="   ")
            if i % 3 == 0: print()
        print()
        if curr == target: return
        print_dan(curr + step, target, step)

    data = sys.stdin.read().split()
    if data:
        s, e = map(int, data)
        print_dan(s, e, 1 if s <= e else -1)

method3()

###################################################################

def method4():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    s, e = int(data[0]), int(data[1])

    step = 1 if s <= e else -1
    dans = [d for d in range(s, e + step, step)]
    
    for d in dans:
        lines = [f"{d} * {i} = {i*d:>2}" for i in range(1, 10)]
        for k in range(0, 9, 3):
            print("   ".join(lines[k:k+3]))
        print()

method4()

###################################################################

def method5():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    s, e = map(int, data)

    # 출력 큐 생성
    queue = []
    curr = s
    while True:
        queue.append(curr)
        if curr == e: break
        curr += 1 if s < e else -1

    while queue:
        dan = queue.pop(0)
        output = ""
        for i in range(1, 10):
            output += f"{dan} * {i} = {i*dan:>2}"
            if i % 3 == 0:
                output += "\n"
            else:
                output += "   "
        sys.stdout.write(output + "\n")

method5()

###################################################################

