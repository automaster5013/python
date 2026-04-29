S = int(input())
E = int(input())
K = int(input())
# print(S, E, K)

for i in range(S, E + 1, K):
    print(i)

##############################################################(방법01)

S = int(input())
E = int(input())
K = int(input())
# print(S, E, K)

current = S
while current <= E:
    print(current)
    current += K 

##############################################################(방법02)

S, E, K = [int(input()) for _ in range(3)]

print(*range(S, E + 1, K), sep='\n')

##############################################################(방법03)


