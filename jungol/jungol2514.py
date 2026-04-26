def solve_v1():
    s = input().strip()
    koi_count = 0
    ioi_count = 0
    
    # 3글자씩 확인해야 하므로 전체 길이 - 2까지만 반복
    for i in range(len(s) - 2):
        target = s[i:i+3]
        if target == "KOI":
            koi_count += 1
        elif target == "IOI":
            ioi_count += 1
            
    print(koi_count)
    print(ioi_count)

solve_v1()

##################################################################

def solve_v2():
    s = input().strip()
    koi = 0
    ioi = 0
    
    for i in range(len(s) - 2):
        # s[i:]가 "KOI"로 시작하는지 체크
        if s.startswith("KOI", i):
            koi += 1
        if s.startswith("IOI", i):
            ioi += 1
            
    print(koi)
    print(ioi)

solve_v2()

##################################################################

import re

def solve_v3():
    s = input().strip()
    
    # (?=...)는 해당 위치에서 패턴이 시작되는지만 확인하고 인덱스를 소비하지 않음
    koi_matches = re.findall(r'(?=KOI)', s)
    ioi_matches = re.findall(r'(?=IOI)', s)
    
    print(len(koi_matches))
    print(len(ioi_matches))

solve_v3()

##################################################################

def solve_v4():
    s = input().strip()
    
    # 세 개의 반복자를 지그재그로 묶어 3개씩 쌍을 만듦
    # 예: (s[0], s[1], s[2]), (s[1], s[2], s[3])...
    windows = zip(s, s[1:], s[2:])
    
    koi = 0
    ioi = 0
    for w in windows:
        # w는 ('K', 'O', 'I')와 같은 형태
        joined = "".join(w)
        if joined == "KOI": koi += 1
        if joined == "IOI": ioi += 1
        
    print(koi)
    print(ioi)

solve_v4()

##################################################################

def solve_v5():
    s = input().strip()
    
    # 조건을 만족할 때마다 1을 더함
    koi = sum(1 for i in range(len(s)-2) if s[i:i+3] == "KOI")
    ioi = sum(1 for i in range(len(s)-2) if s[i:i+3] == "IOI")
    
    print(koi)
    print(ioi)

solve_v5()

##################################################################


