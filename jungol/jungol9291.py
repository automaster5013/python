trump = input()
# print(trump)
print(trump * 20)

##########################################################(방법01)

trump = input()
# print(trump)
print(*[trump] * 20, sep='')

##########################################################(방법02)

trump = input()
# print(trump)
for i in range(20):
    print(trump, end='')
print()

##########################################################(방법03)

trump = input()
# print(trump)
result = "".join(trump for i in range(20))
print(result)

##########################################################(방법04)

trump = input()
# print(trump)
i = 0
while i < 20:
    print(trump, end='')
    i += 1
print()

##########################################################(방법05)

inp = input()
# print(inp)
print(inp[0])
for i in range(20):
    print(inp[0], end='')

##########################################################(방법06)

print(input()*20)

##########################################################(방법07)

