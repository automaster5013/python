words = input().split()
# print(words)
first = words[0]
second = words[1]
print(second, first + second)

#########################################(방법01)

inp1, inp2 = input().split()
print(f"{inp2} {inp1}{inp2}")

#########################################(방법02)

print("{1} {0}{1}".format(*input().split()))

#########################################(방법03)

w1, w2 = input().split()
# print(w1, w2)
print(w2, w2+w1)

#########################################(방법04)

