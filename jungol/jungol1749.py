import sys

def solve():
    # 입력 속도 향상
    input = sys.stdin.read().split()
    if not input:
        return
    
    # 한번에 꺼낼 수 있는 구슬 개수
    b = [int(input[0]), int(input[1]), int(input[2])]
    
    # 그룬디 수 계산 (k의 최대 범위는 500)
    max_k = 500
    grundy = [0] * (max_k + 1)
    
    for i in range(1, max_k + 1):
        reachable_grundy = set()
        for move in b:
            if i - move >= 0:
                reachable_grundy.add(grundy[i - move])
        
        # mex 계산: 도달 가능한 상태 중 없는 가장 작은 수
        res = 0
        while res in reachable_grundy:
            res += 1
        grundy[i] = res

    # 5개의 케이스에 대해 승자 결정
    ptr = 3
    for _ in range(5):
        k1 = int(input[ptr])
        k2 = int(input[ptr+1])
        ptr += 2
        
        # 두 통의 그룬디 수가 같으면 B 승리, 다르면 A 승리
        if grundy[k1] == grundy[k2]:
            print("B")
        else:
            print("A")

if __name__ == "__main__":
    solve()

##############################################################

