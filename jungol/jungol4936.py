import sys
from bisect import bisect_right

def solve():
    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))

    left_raw  = [a[i] - i for i in range(N)]
    right_raw = [a[i] + i for i in range(N)]

    all_L = sorted(set(left_raw))
    all_R = sorted(set(right_raw))
    SZ_L, SZ_R = len(all_L), len(all_R)

    cntL = [0]*(SZ_L+1); sumL = [0]*(SZ_L+1)
    cntR = [0]*(SZ_R+1); sumR = [0]*(SZ_R+1)

    def updL(rv, d):
        i = bisect_right(all_L, rv)
        while i <= SZ_L: cntL[i]+=d; sumL[i]+=d*rv; i+=i&-i

    def updR(rv, d):
        i = bisect_right(all_R, rv)
        while i <= SZ_R: cntR[i]+=d; sumR[i]+=d*rv; i+=i&-i

    def qL(i):
        c=s=0
        while i>0: c+=cntL[i]; s+=sumL[i]; i-=i&-i
        return c,s

    def qR(i):
        c=s=0
        while i>0: c+=cntR[i]; s+=sumR[i]; i-=i&-i
        return c,s

    updL(left_raw[0], 1)
    for i in range(1,N): updR(right_raw[i], 1)

    tL_sum = left_raw[0]
    tR_sum = sum(right_raw[1:])
    ans = float('inf')

    for t in range(N):
        tL_cnt = t+1
        tR_cnt = N-t-1
        h_min = 1 + max(t, N-1-t)
        target = (N+1)>>1

        lo = all_L[0]+t
        if tR_cnt: lo = min(lo, all_R[0]-t)
        hi = all_L[-1]+t
        if tR_cnt: hi = max(hi, all_R[-1]-t)

        while lo < hi:
            mid = (lo+hi)>>1
            cL,_ = qL(bisect_right(all_L, mid-t))
            cR,_ = qR(bisect_right(all_R, mid+t))
            if cL+cR >= target: hi=mid
            else: lo=mid+1
        h = max(lo, h_min)

        # 왼쪽 b[i] = left_raw[i] + t
        # sum|b[i]-h| = sum|(raw+t)-h| = sum|raw-(h-t)|
        cLle, sLle = qL(bisect_right(all_L, h-t))
        cLgt = tL_cnt - cLle
        sLgt = tL_sum - sLle
        # b<=h: h - (raw+t) = h - raw - t
        # b>h:  (raw+t) - h = raw + t - h
        costL = h*cLle - (sLle + cLle*t) + (sLgt + cLgt*t) - h*cLgt

        # 오른쪽 b[i] = right_raw[i] - t
        # sum|(raw-t)-h| = sum|raw-(h+t)|
        cRle, sRle = qR(bisect_right(all_R, h+t))
        cRgt = tR_cnt - cRle
        sRgt = tR_sum - sRle
        costR = h*cRle - (sRle - cRle*t) + (sRgt - cRgt*t) - h*cRgt

        if costL+costR < ans: ans = costL+costR

        if t+1 < N:
            updR(right_raw[t+1], -1)
            updL(left_raw[t+1],  1)
            tR_sum -= right_raw[t+1]
            tL_sum += left_raw[t+1]

    print(ans)

solve()

#########################################################################
