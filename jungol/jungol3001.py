import sys
import gc

def solve():
    # 빠른 입출력을 위한 통째 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    T = int(input_data[1])
    
    # 캐시 히트율을 높이기 위해 속성을 분리한 리스트 사용
    stars_x = [0] * N
    stars_y = [0] * N
    stars_dx = [0] * N
    stars_dy = [0] * N
    
    idx = 2
    for i in range(N):
        stars_x[i] = int(input_data[idx])
        stars_y[i] = int(input_data[idx+1])
        stars_dx[i] = int(input_data[idx+2])
        stars_dy[i] = int(input_data[idx+3])
        idx += 4
        
    memo = {}
    
    def get_max_dist_sq(t):
        if t in memo: return memo[t]
        
        # 1. zip을 활용한 초고속 좌표 생성 및 정렬 (C-level 속도)
        pts = sorted([(x + dx*t, y + dy*t) for x, y, dx, dy in zip(stars_x, stars_y, stars_dx, stars_dy)])
        
        # 2. 볼록 껍질 (Monotone Chain) - 극단적 인라인 최적화
        hull = []
        hull_append = hull.append
        hull_pop = hull.pop
        
        for p in pts:
            px, py = p
            while len(hull) >= 2:
                l1x, l1y = hull[-1]
                l2x, l2y = hull[-2]
                # CCW 연산 인라인화
                if (l1x - l2x) * (py - l2y) - (l1y - l2y) * (px - l2x) <= 0:
                    hull_pop()
                else:
                    break
            hull_append(p)
            
        lower_len = len(hull)
        for p in reversed(pts):
            px, py = p
            while len(hull) > lower_len:
                l1x, l1y = hull[-1]
                l2x, l2y = hull[-2]
                if (l1x - l2x) * (py - l2y) - (l1y - l2y) * (px - l2x) <= 0:
                    hull_pop()
                else:
                    break
            hull_append(p)
            
        hull_pop() # 마지막 중복 점 제거
        n = len(hull)
        
        # 점이 1~2개뿐인 예외 상황 초고속 탈출
        if n <= 1:
            memo[t] = 0
            return 0
        if n == 2:
            ans = (hull[0][0] - hull[1][0])**2 + (hull[0][1] - hull[1][1])**2
            memo[t] = ans
            return ans
            
        # 3. 회전하는 캘리퍼스 (Rotating Calipers) 최적화
        max_d = 0
        j = 1
        
        # 인덱스 접근 횟수를 줄이기 위해 리스트 분리
        hx = [p[0] for p in hull]
        hy = [p[1] for p in hull]
        
        for i in range(n):
            ni = i + 1
            if ni == n: ni = 0 # 나머지(%) 연산 배제
            
            vx = hx[ni] - hx[i]
            vy = hy[ni] - hy[i]
            
            while True:
                nj = j + 1
                if nj == n: nj = 0
                
                wjx = hx[nj] - hx[j]
                wjy = hy[nj] - hy[j]
                
                cp = vx * wjy - vy * wjx
                if cp > 0:
                    j = nj
                elif cp == 0:
                    # 완벽한 평행선의 경우 예외 거리 처리
                    d1 = (hx[ni] - hx[nj])**2 + (hy[ni] - hy[nj])**2
                    if d1 > max_d: max_d = d1
                    d2 = (hx[i] - hx[nj])**2 + (hy[i] - hy[nj])**2
                    if d2 > max_d: max_d = d2
                    j = nj
                else:
                    break
                    
            d1 = (hx[i] - hx[j])**2 + (hy[i] - hy[j])**2
            if d1 > max_d: max_d = d1
            d2 = (hx[ni] - hx[j])**2 + (hy[ni] - hy[j])**2
            if d2 > max_d: max_d = d2
            
        memo[t] = max_d
        return max_d

    # 4. 볼록 함수 특징을 이용한 이분 탐색 (Binary Search)
    low = 0
    high = T
    ans_t = T
    
    while low <= high:
        mid = (low + high) >> 1  # // 2 보다 미세하게 빠른 비트 연산 적용
        
        # T일차 도달 시 검색 종료
        if mid == T:
            ans_t = T
            break
            
        fm = get_max_dist_sq(mid)
        fm_next = get_max_dist_sq(mid + 1)
        
        # 다음 시간에 거리가 늘어나거나 같다면, 정답은 같거나 더 이전 시간에 있음
        if fm_next >= fm:
            ans_t = mid
            high = mid - 1
        else:
            low = mid + 1
            
    # 정답 출력
    print(ans_t)
    print(get_max_dist_sq(ans_t))

if __name__ == '__main__':
    # 잦은 튜플 생성으로 인한 프레임 드랍을 막기 위해 가비지 컬렉터 일시 정지
    gc.disable() 
    solve()

#####################################################################################33



