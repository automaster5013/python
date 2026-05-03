import sys

def solve():
    # 입력을 라인 단위로 읽어 처리합니다.
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        n = int(line)
        
        # p를 1로 두고 범위를 좁혀나가는 대신, 
        # n을 9와 2로 번갈아가며 나누어 1 이하가 되는 시점을 찾습니다.
        while True:
            # Stan의 차례: 9로 나눕니다.
            n /= 9
            if n <= 1:
                print("Stan wins.")
                break
            
            # Ollie의 차례: 2로 나눕니다.
            n /= 2
            if n <= 1:
                print("Ollie wins.")
                break

if __name__ == "__main__":
    solve()

####################################################################

