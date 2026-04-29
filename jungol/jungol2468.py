import sys

def get_next_larger(n):
    c = n
    c0 = 0 # 오른쪽 끝의 연속된 0의 개수
    c1 = 0 # 그 다음 연속된 1의 개수
    
    # 트레일링 제로 세기
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
    # 그 다음 연속된 1 세기
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
        
    # 01 패턴을 찾을 수 없는 경우 (예: 111000...)
    if c0 + c1 >= 62 or c0 + c1 == 0:
        return 0
        
    p = c0 + c1 # 바꿀 01 패턴 중 0의 위치
    
    res = n | (1 << p)        # 0을 1로 바꿈
    res &= ~((1 << p) - 1)    # p보다 오른쪽 비트를 모두 0으로 클리어
    res |= (1 << (c1 - 1)) - 1 # (c1-1)개의 1을 가장 오른쪽에 채움
    return res

def get_next_smaller(n):
    c = n
    c1 = 0 # 오른쪽 끝의 연속된 1의 개수
    c0 = 0 # 그 다음 연속된 0의 개수
    
    # 트레일링 원 세기
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    
    if c == 0: return 0 # 10 패턴을 찾을 수 없음
    
    # 그 다음 연속된 0 세기
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
        
    if c == 0: return 0 # 10 패턴을 찾을 수 없음
    
    p = c0 + c1 # 바꿀 10 패턴 중 1의 위치
    
    res = n & ~(1 << p)       # 1을 0으로 바꿈
    res |= (1 << p) - 1       # p보다 오른쪽을 일단 1로 다 채움
    res &= ~((1 << (c0 - 1)) - 1) # (c0-1)개의 0을 가장 오른쪽에 채움 (1들을 왼쪽으로 밀기)
    return res

def solve():
    try:
        line = sys.stdin.readline()
        if not line: return
        a = int(line.strip())
        
        smaller = get_next_smaller(a)
        larger = get_next_larger(a)
        
        print(f"{smaller} {larger}")
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

############################################################################################

