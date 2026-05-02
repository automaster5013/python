import sys

def ccw(p1, p2, p3):
    """세 점의 방향성을 계산하는 함수"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    res = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
    if res > 0: return 1
    if res < 0: return -1
    return 0

def is_intersect(s1, s2):
    """두 선분이 완전히 교차하는지 판별하는 함수"""
    p1, p2 = s1
    p3, p4 = s2
    
    res1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    res2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    
    # 두 선분의 끝점들이 서로 반대편에 있어야 완전 교차임 (< 0)
    return res1 < 0 and res2 < 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    segments = []
    
    idx = 1
    for _ in range(n):
        x1 = int(input_data[idx])
        y1 = int(input_data[idx+1])
        x2 = int(input_data[idx+2])
        y2 = int(input_data[idx+3])
        segments.append(((x1, y1), (x2, y2)))
        idx += 4
        
    count = 0
    # 모든 선분 쌍에 대해 교차 여부 확인
    for i in range(n):
        for j in range(i + 1, n):
            if is_intersect(segments[i], segments[j]):
                count += 1
                
    print(count)

if __name__ == "__main__":
    solve()

#############################################################3


