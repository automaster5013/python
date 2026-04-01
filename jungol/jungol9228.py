score = int(input())
# print(score)
results = ["FAIL", "PASS"]
print(results[score >= 60])

##########################################(방법01)

score = int(input())
# print(score)
print("PASS" if score >= 60 else "FAIL")

##########################################(방법02)

inp = int(input())
# print(inp)
if inp >= 60:
    print("PASS")
else:
    print("FAIL")

##########################################(방법03)

class P:
    def __init__(self, A):
        self.A = A

    def OK(self):
        if 60 <= self.A:
            print("PASS")
        else:
            print("FAIL")

a = int(input())
p = P(a)
p.OK()

##########################################(방법04)

print("PASS" if int(input()) >= 60 else "FAIL")

##########################################(방법05)

