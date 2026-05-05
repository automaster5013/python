import sys

def solve():
    # 입력 처리 최적화
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    p = [i + 1 for i in range(N) if input_data[i+1] == '1']
    M = len(p)
    if M == 0:
        print(0)
        return

    # 시계 방향(CW) DP 계산
    cw = [0] * (M + 1)
    dq = [0]
    head = 0
    for i in range(1, M + 1):
        x = p[i-1]
        while head + 1 < len(dq) and cw[dq[head]] - dq[head] * x >= cw[dq[head+1]] - dq[head+1] * x:
            head += 1
        best_j = dq[head]
        cw[i] = cw[best_j] + (i - best_j + 1) * x
        if i < M:
            while len(dq) - head >= 2:
                j1, j2 = dq[-2], dq[-1]
                if (cw[j2] - cw[j1]) * (i - j2) >= (cw[i] - cw[j2]) * (j2 - j1):
                    dq.pop()
                else: break
            dq.append(i)

    # 반시계 방향(CCW) DP 계산
    d = [(N + 1 - val) for val in reversed(p)]
    ccw = [0] * (M + 1)
    dq = [0]
    head = 0
    for i in range(1, M + 1):
        x = d[i-1]
        while head + 1 < len(dq) and ccw[dq[head]] - dq[head] * x >= ccw[dq[head+1]] - dq[head+1] * x:
            head += 1
        best_j = dq[head]
        ccw[i] = ccw[best_j] + (i - best_j + 1) * x
        if i < M:
            while len(dq) - head >= 2:
                j1, j2 = dq[-2], dq[-1]
                if (ccw[j2] - ccw[j1]) * (i - j2) >= (ccw[i] - ccw[j2]) * (j2 - j1):
                    dq.pop()
                else: break
            dq.append(i)
            
    # 시계 방향과 반시계 방향의 합 중 최솟값 산출
    ans = min(cw[i] + ccw[M - i] for i in range(M + 1))
    print(ans)

if __name__ == '__main__':
    solve()

###############################################################################################################


