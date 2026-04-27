
n = int(input())
# print(n)
r, g, b = map(int, input().split())

for x in range(n - 1):
    nr, ng, nb = map(int, input().split())
    
    r, g, b = nr + min(g, b), ng + min(r, b), nb + min(r, g)

print(min(r, g, b))

##############################################################################

n = int(input())
# print(n)
lst = []
for x in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1, n):
    lst[i][0] += lst[i-1][1] if lst[i-1][1] < lst[i-1][2] else lst[i-1][2]
    
    lst[i][1] += lst[i-1][0] if lst[i-1][0] < lst[i-1][2] else lst[i-1][2]
    
    lst[i][2] += lst[i-1][0] if lst[i-1][0] < lst[i-1][1] else lst[i-1][1]

res = lst[n-1][0]
for val in lst[n-1]:
    if val < res:
        res = val

print(res)

##############################################################################

import sys
N = int(sys.stdin.readline().strip())
R = G = B = 0

for t in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    if t == 0:
        R, G, B = r, g, b
    else:
        n_R = r + min(G, B)
        n_G = g + min(R, B)
        n_B = b + min(R, G)
        R, G, B = n_R, n_G, n_B

print(min(R, G, B))

##############################################################################








