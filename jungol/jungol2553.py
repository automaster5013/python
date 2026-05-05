
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a, b, c = map(int, input_data[1:4])
    x = list(map(int, input_data[4:]))
    
    s = [0] * (n + 1)
    for i in range(n):
        s[i+1] = s[i] + x[i]
        
    dp = [0] * (n + 1)
    
    dq = [] 
    
    def get_y(idx, val):
        m = -2 * a * s[idx]
        k = dp[idx] + a * s[idx]**2 - b * s[idx]
        return m * val + k

    def intersect(idx1, idx2):
        m1, k1 = -2 * a * s[idx1], dp[idx1] + a * s[idx1]**2 - b * s[idx1]
        m2, k2 = -2 * a * s[idx2], dp[idx2] + a * s[idx2]**2 - b * s[idx2]
        return (k2 - k1) / (m1 - m2)

    dq.append(0)
    head = 0 
    
    for i in range(1, n + 1):
        while head + 1 < len(dq) and intersect(dq[head], dq[head+1]) <= s[i]:
            head += 1
            
        best_j = dq[head]
        dp[i] = a * s[i]**2 + b * s[i] + c + get_y(best_j, s[i])
        
        while head + 1 < len(dq) and intersect(dq[-2], dq[-1]) >= intersect(dq[-1], i):
            dq.pop()
        dq.append(i)
        
    print(dp[n])

if __name__ == "__main__":
    solve()

#############################################################################################


