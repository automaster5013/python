import sys

def solve():
    # 빠른 입출력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    L = int(input_data[1])
    
    rays = []
    idx = 2
    for _ in range(N):
        sx = int(input_data[idx])
        sy = int(input_data[idx+1])
        dx = int(input_data[idx+2])
        dy = int(input_data[idx+3])
        idx += 4
        
        # 방향 벡터
        vx = dx - sx
        vy = dy - sy
        
        # 박스 경계에 닿을 때까지 걸리는 시간(t) 구하기
        tx = float('inf')
        if vx > 0:
            tx = (L - sx) / vx
        elif vx < 0:
            tx = -sx / vx
            
        ty = float('inf')
        if vy > 0:
            ty = (L - sy) / vy
        elif vy < 0:
            ty = -sy / vy
            
        # x, y 경계 중 더 빨리 닿는 시간이 박스를 벗어나는 시간
        t_end = min(tx, ty)
        rays.append((sx, sy, vx, vy, t_end))
        
    ans = 0
    # 오차 범위 1e-6을 고려하여 넉넉하면서도 안전한 Epsilon 설정
    EPS = 1e-8
    
    # N개의 선분 중 임의의 2개를 뽑아 교차 여부 확인 O(N^2)
    for i in range(N):
        sx1, sy1, vx1, vy1, tend1 = rays[i]
        for j in range(i + 1, N):
            sx2, sy2, vx2, vy2, tend2 = rays[j]
            
            # 외적(Cross Product)을 통해 평행 여부 확인 (정수 연산이라 오차 없음)
            cross = vx1 * vy2 - vy1 * vx2
            
            if cross != 0:
                # 크래머 공식을 사용한 교차점의 매개변수 t1, t2 도출
                num1 = (sx2 - sx1) * vy2 - (sy2 - sy1) * vx2
                num2 = (sx2 - sx1) * vy1 - (sy2 - sy1) * vx1
                t1 = num1 / cross
                t2 = num2 / cross
                
                # 교점이 박스 내부에 존재하는 유효한 시간인지 확인
                if -EPS <= t1 <= tend1 + EPS and -EPS <= t2 <= tend2 + EPS:
                    ans += 1
            else:
                # 두 직선이 평행할 경우, 일직선(Collinear) 상에 있는지 확인
                cross2 = vx1 * (sy2 - sy1) - vy1 * (sx2 - sx1)
                if cross2 == 0: # 일직선 상에 위치함
                    # x축(또는 y축)으로 투영하여 두 선분의 범위가 겹치는지 판단
                    if vx1 != 0:
                        min1 = min(sx1, sx1 + tend1 * vx1)
                        max1 = max(sx1, sx1 + tend1 * vx1)
                        min2 = min(sx2, sx2 + tend2 * vx2)
                        max2 = max(sx2, sx2 + tend2 * vx2)
                    else:
                        min1 = min(sy1, sy1 + tend1 * vy1)
                        max1 = max(sy1, sy1 + tend1 * vy1)
                        min2 = min(sy2, sy2 + tend2 * vy2)
                        max2 = max(sy2, sy2 + tend2 * vy2)
                    
                    # 두 구간이 조금이라도 겹치면(혹은 한 점에서 만나면) 교차 처리
                    if max(min1, min2) <= min(max1, max2) + EPS:
                        ans += 1

    print(ans)

if __name__ == '__main__':
    solve()

############################################################################################


