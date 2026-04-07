N = int(input())
# print(N)
for i in range(N):
    print(f"Python {i}")

####################################################################(방법01)

N = int(input())
# print(N)
print(*[f"Python {i}" for i in range(N)], sep="\n")

####################################################################(방법02)

N = int(input())
# print(N)
output = "\n".join(map(lambda i: f"Python {i}", range(N)))
print(output)

####################################################################(방법03)

N = int(input())
# print(N)
for i in range(N):
    print("Python {}".format(i))

####################################################################(방법04)

N = int(input())
# print(N)
i = 0
while True:
    if i >= N:
        break
    print(f"Python {i}")
    i += 1

####################################################################(방법05)

N = int(input())
# print(N)
for i in range(N):
    print("Python " + str(i))

####################################################################(방법06)

