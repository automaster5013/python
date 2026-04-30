import sys

def solve():
    # 입력 처리 (길이가 길므로 sys.stdin 사용)
    s = sys.stdin.readline().strip()
    if not s:
        return
    
    a_pending = 0       # B를 기다리는 A의 수
    b_free = 0          # 아무와도 짝이 없는 B의 수
    b_used_for_a = 0    # A와 짝을 맺은 B의 수
    total_pairs = 0     # 현재까지 맺어진 총 쌍의 수
    
    for char in s:
        if char == 'A':
            # A가 나오면 나중에 나올 B를 기다립니다.
            a_pending += 1
            
        elif char == 'B':
            # B가 나왔을 때, 기다리는 A가 있다면 일단 짝을 맺습니다.
            if a_pending > 0:
                a_pending -= 1
                b_used_for_a += 1
                total_pairs += 1
            else:
                # 기다리는 A가 없다면 일단 자유 상태로 둡니다.
                b_free += 1
                
        elif char == 'C':
            # C는 무조건 앞에 있는 B가 필요합니다.
            if b_free > 0:
                # 1순위: 자유 상태인 B와 짝을 맺습니다.
                b_free -= 1
                total_pairs += 1
            elif b_used_for_a > 0:
                # 2순위: 이미 A와 짝인 B를 가로챕니다.
                b_used_for_a -= 1
                # 가로채기를 당한 A는 다시 B를 기다리는 상태가 됩니다.
                a_pending += 1
                # 전체 쌍의 수는 변하지 않지만(AB -> BC), 
                # A를 해방시켜 나중에 나올 B와 결합할 가능성을 열어둡니다.
                
    print(total_pairs)

if __name__ == "__main__":
    solve()

#########################################################################

