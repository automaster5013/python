def hello_k(count):
    if count > 0:
        print("Hello")
        hello_k(count - 1)

N, M = map(int, input().split())

hello_k(N)
print()
hello_k(M)

############################################################(방법01)

def print_hello():
    print("Hello")

N, M = map(int, input().split())
# print(N, M)
for i in range(N):
    print("Hello")
print()
for i in range(M):
    print("Hello")

############################################################(방법01)

