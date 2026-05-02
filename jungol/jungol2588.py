import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    k = N // 3
    half = N // 2
    
    # 각 요리를 먹기 위해 필요한 테이블 회전 상태 R 전처리
    def get_r(target_dish, seat_offset):
        return (target_dish - seat_offset) % N

    # 아빠(1), 엄마(k+1), 현이(2k+1)
    p1 = int(input_data[ptr]); ptr += 1
    r1 = [get_r(int(x), 1) for x in input_data[ptr:ptr+p1]]; ptr += p1
    p2 = int(input_data[ptr]); ptr += 1
    r2 = [get_r(int(x), k + 1) for x in input_data[ptr:ptr+p2]]; ptr += p2
    p3 = int(input_data[ptr]); ptr += 1
    r3 = [get_r(int(x), 2 * k + 1) for x in input_data[ptr:ptr+p3]]; ptr += p3

    # 거리 계산 함수 (미리 계산하기 위해 인라인화)
    def dist(a, b):
        d = a - b
        if d < 0: d = -d
        return d if d <= half else N - d

    # 모든 상태 간 거리 미리 계산 (성능의 핵심)
    d01 = [[dist(r1[i], r2[j]) for j in range(p2)] for i in range(p1)]
    d02 = [[dist(r1[i], r3[l]) for l in range(p3)] for i in range(p1)]
    d10 = [[dist(r2[j], r1[i]) for i in range(p1)] for j in range(p2)]
    d12 = [[dist(r2[j], r3[l]) for l in range(p3)] for j in range(p2)]
    d20 = [[dist(r3[l], r1[i]) for i in range(p1)] for l in range(p3)]
    d21 = [[dist(r3[l], r2[j]) for j in range(p2)] for l in range(p3)]
    
    d00 = [dist(r1[i], r1[i+1]) for i in range(p1-1)]
    d11 = [dist(r2[j], r2[j+1]) for j in range(p2-1)]
    d22 = [dist(r3[l], r3[l+1]) for l in range(p3-1)]

    inf = 10**18
    # dp[i][j][l] = [아빠가 마지막, 엄마가 마지막, 현이가 마지막]
    dp = [[[[inf] * 3 for _ in range(p3 + 1)] for _ in range(p2 + 1)] for _ in range(p1 + 1)]

    # 초기 상태 (R=0에서 시작)
    if p1 > 0: dp[1][0][0][0] = dist(0, r1[0])
    if p2 > 0: dp[0][1][0][1] = dist(0, r2[0])
    if p3 > 0: dp[0][0][1][2] = dist(0, r3[0])

    for i in range(p1 + 1):
        dp_i = dp[i]
        for j in range(p2 + 1):
            dp_ij = dp_i[j]
            for l in range(p3 + 1):
                res = dp_ij[l]
                
                # 0: 아빠가 마지막으로 먹음
                v0 = res[0]
                if v0 < inf:
                    if i < p1: # 아빠가 다음 요리
                        cost = v0 + d00[i-1]
                        if cost < dp[i+1][j][l][0]: dp[i+1][j][l][0] = cost
                    if j < p2: # 엄마가 다음 요리
                        cost = v0 + d01[i-1][j]
                        if cost < dp[i][j+1][l][1]: dp[i][j+1][l][1] = cost
                    if l < p3: # 현이가 다음 요리
                        cost = v0 + d02[i-1][l]
                        if cost < dp[i][j][l+1][2]: dp[i][j][l+1][2] = cost

                # 1: 엄마가 마지막으로 먹음
                v1 = res[1]
                if v1 < inf:
                    if i < p1:
                        cost = v1 + d10[j-1][i]
                        if cost < dp[i+1][j][l][0]: dp[i+1][j][l][0] = cost
                    if j < p2:
                        cost = v1 + d11[j-1]
                        if cost < dp[i][j+1][l][1]: dp[i][j+1][l][1] = cost
                    if l < p3:
                        cost = v1 + d12[j-1][l]
                        if cost < dp[i][j][l+1][2]: dp[i][j][l+1][2] = cost

                # 2: 현이가 마지막으로 먹음
                v2 = res[2]
                if v2 < inf:
                    if i < p1:
                        cost = v2 + d20[l-1][i]
                        if cost < dp[i+1][j][l][0]: dp[i+1][j][l][0] = cost
                    if j < p2:
                        cost = v2 + d21[l-1][j]
                        if cost < dp[i][j+1][l][1]: dp[i][j+1][l][1] = cost
                    if l < p3:
                        cost = v2 + d22[l-1]
                        if cost < dp[i][j][l+1][2]: dp[i][j][l+1][2] = cost

    ans = min(dp[p1][p2][p3])
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()

#####################################################################################


