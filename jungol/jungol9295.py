S, E = map(int,input().split())
# print(S, E)
print(*range(S, E + 1), sep='   ')

################################################(방법01)

S, E = map(int, input().split())
# print(S, E)
result = '   '.join(map(str, range(S, E + 1)))
print(result)

################################################(방법02)

S, E = map(int, input().split())
# print(S, E)
for i in range(S, E + 1):
    prefix = '   ' if i > S else ''
    print(f"{prefix}{i}", end='')

print()

################################################(방법03)

S, E = map(int, input().split())
# print(S, E)
output = ""
for i in range(S, E + 1):
    output += str(i) + "   "

print(output.rstrip())

################################################(방법04)

S, E = map(int(input().split()))
# print(S, E)

for x in range(S, E+1):
    print(x, "  ", end='')

################################################(방법05)

S,E=map(int,input().split())

for i in range(S,E+1):
    print(i,end="   ")

################################################(방법06)

