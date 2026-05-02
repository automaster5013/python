import sys

def ccw(p1, p2, p3):
    """세 점의 방향성을 판별하는 함수 (외적 활용)"""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def dist_sq(p1, p2):
    """두 점 사이의 거리 제곱을 계산하는 함수"""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def solve():
    # 대량의 데이터를 한 번에 읽어와 처리 속도 향상
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    points = []
    ptr = 1
    for _ in range(n):
        points.append((int(input_data[ptr]), int(input_data[ptr+1])))
        ptr += 2
    
    # 1. 볼록 껍질 추출 (Monotone Chain)
    points.sort()
    
    if n <= 2:
        print(dist_sq(points[0], points[-1]))
        return

    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
        
    hull = lower[:-1] + upper[:-1]
    m = len(hull)
    
    # 2. 회전하는 캘리퍼스 알고리즘
    max_d = 0
    j = 1
    for i in range(m):
        # i번째 변에 대해 가장 먼 점 j를 탐색
        while True:
            # i, i+1 벡터와 j, j+1 벡터의 외적을 비교하여 거리 판단
            ni = (i + 1) % m
            nj = (j + 1) % m
            
            # 두 벡터 (hull[ni]-hull[i])와 (hull[nj]-hull[j])의 외적 방향 확인
            vec_i = (hull[ni][0] - hull[i][0], hull[ni][1] - hull[i][1])
            vec_j = (hull[nj][0] - hull[j][0], hull[nj][1] - hull[j][1])
            
            if (vec_i[0] * vec_j[1] - vec_i[1] * vec_j[0]) > 0:
                j = nj
            else:
                break
        
        # 현재 찾은 쌍(i, j)와 (ni, j)의 거리를 확인하여 최댓값 갱신
        max_d = max(max_d, dist_sq(hull[i], hull[j]))
        max_d = max(max_d, dist_sq(hull[(i + 1) % m], hull[j]))

    print(max_d)

if __name__ == "__main__":
    solve()

##########################################################################3

