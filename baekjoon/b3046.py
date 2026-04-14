# S = (R1 + R2)/2
R1, S = map(int, input().split())
# print(R1, S)
R2 = 2 * S - R1
print(R2)

############################################################(방법01)

class AverageSolv:
    def __init__(self, R1, S):
        self.R1 = R1
        self.S = S

    def get_R2(self):
        return (self.S * 2) - self.R1

R1, S = map(int, input().split())
solv = AverageSolv(R1, S)
print(solv.get_R2())

############################################################(방법02)

R1, S = map(int, input().split())
# print(R1, S)

R2 = 2 * S - R1
print(R2)

############################################################(방법03)

