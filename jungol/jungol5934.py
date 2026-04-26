# 입력 처리
try:
    n_in = input()
    if not n_in: exit()
    n = int(n_in)

    # 범위 및 홀수 체크
    if not (1 <= n <= 100 and n % 2 == 1):
        print("INPUT ERROR!")
    else:
        mid = n // 2
        # 1. 상단 및 중간 줄 (0 ~ mid)
        for i in range(mid + 1):
            print(" " * i + "*" * (mid + 1 - i))
        
        # 2. 하단 줄 (mid + 1 ~ n-1)
        for i in range(1, mid + 1):
            # 공백은 항상 mid개로 고정, 별은 2개부터 (mid+1)개까지 증가
            print(" " * mid + "*" * (i + 1))
except:
    print("INPUT ERROR!")

#########################################################################

n_raw = input()
if not n_raw.isdigit():
    print("INPUT ERROR!")
else:
    n = int(n_raw)
    if 1 <= n <= 100 and n % 2 == 1:
        mid = n // 2
        for i in range(n):
            if i <= mid:
                # 상단: 공백 증가, 별 감소
                spaces, stars = i, mid + 1 - i
            else:
                # 하단: 공백 고정, 별 증가
                spaces, stars = mid, i - mid + 1
            print(" " * spaces + "*" * stars)
    else:
        print("INPUT ERROR!")

#########################################################################

n_val = input()
try:
    n = int(n_val)
    if 1 <= n <= 100 and n % 2 == 1:
        mid = n // 2
        # 상단과 하단의 규칙을 리스트 두 개로 만들어 합침
        top = [" " * i + "*" * (mid + 1 - i) for i in range(mid + 1)]
        bottom = [" " * mid + "*" * (i + 1) for i in range(1, mid + 1)]
        
        print("\n".join(top + bottom))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

#########################################################################

n_str = input()
if n_str.replace('-','').isdigit():
    n = int(n_str)
    if 1 <= n <= 100 and n % 2 == 1:
        m = n // 2
        for i in range(n):
            if i <= m:
                # i=0일 때 m+1, i=m일 때 1이 되는 수식
                print(" " * i + "*" * (m + 1 - i))
            else:
                # 하단은 규칙이 완전히 달라지므로 고정 공백 사용
                print(" " * m + "*" * (i - m + 1))
    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")

#########################################################################

n_data = input()
try:
    n = int(n_data)
    if 1 <= n <= 100 and n % 2 == 1:
        mid = n // 2
        sp, st = 0, mid + 1 # 초기 공백 0, 별 mid+1
        
        for i in range(n):
            print(" " * sp + "*" * st)
            if i < mid:
                # 중간 전까지는 공백 늘리고 별 줄임
                sp += 1
                st -= 1
            else:
                # 중간 이후부터는 공백 고정, 별 늘림
                sp = mid
                st += 1
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

#########################################################################


