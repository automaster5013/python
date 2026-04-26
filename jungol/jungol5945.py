try:
    data = input().split()
    if not data: exit()
    n = int(data[0])

    # 조건: 1~50 사이의 홀수여야 함
    if 1 <= n <= 50 and n % 2 == 1:
        current_num = 1
        for i in range(1, n + 1):
            # i번째 줄에 들어갈 i개의 숫자 생성
            row = []
            for _ in range(i):
                row.append(current_num)
                current_num += 1
            
            # 짝수 줄이면 리스트를 뒤집음
            if i % 2 == 0:
                row.reverse()
            
            # 리스트 요소를 공백으로 구분하여 출력
            print(*(row))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

##########################################################

n_raw = input().split()
if n_raw and n_raw[0].isdigit():
    n = int(n_raw[0])
    if 1 <= n <= 50 and n % 2 == 1:
        num = 1
        for i in range(1, n + 1):
            if i % 2 != 0:
                # 홀수 행: 정방향 출력
                for _ in range(i):
                    print(num, end=" ")
                    num += 1
            else:
                # 짝수 행: (현재 시작값 + i - 1)부터 시작해서 역순 출력
                start_val = num
                for j in range(start_val + i - 1, start_val - 1, -1):
                    print(j, end=" ")
                num += i # 다음 행을 위해 숫자 건너뜀
            print()
    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")

##########################################################

try:
    n = int(input())
    if 1 <= n <= 50 and n % 2 == 1:
        curr = 1
        for i in range(1, n + 1):
            # i개의 숫자를 리스트 컴프리헨션으로 생성
            row = [curr + j for j in range(i)]
            curr += i
            
            # 슬라이싱으로 지그재그 처리
            display = row if i % 2 != 0 else row[::-1]
            print(" ".join(map(str, display)))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

##########################################################

def number_gen():
    i = 1
    while True:
        yield i
        i += 1

def solve():
    try:
        n = int(input())
        if not (1 <= n <= 50 and n % 2 == 1):
            print("INPUT ERROR!")
            return
        
        gen = number_gen()
        for i in range(1, n + 1):
            # 제너레이터에서 i개만큼 추출
            line = [next(gen) for _ in range(i)]
            if i % 2 == 0:
                line = line[::-1]
            print(*(line))
    except:
        print("INPUT ERROR!")

solve()

##########################################################

def number_gen():
    i = 1
    while True:
        yield i
        i += 1

def solve():
    try:
        n = int(input())
        if not (1 <= n <= 50 and n % 2 == 1):
            print("INPUT ERROR!")
            return
        
        gen = number_gen()
        for i in range(1, n + 1):
            # 제너레이터에서 i개만큼 추출
            line = [next(gen) for _ in range(i)]
            if i % 2 == 0:
                line = line[::-1]
            print(*(line))
    except:
        print("INPUT ERROR!")

solve()

##########################################################


