import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))  # 테스트 케이스 수
    
    for _ in range(t):
        n = int(next(it))  # 숫자의 개수
        phone_list = [next(it) for _ in range(n)]
        
        # 1. 문자열을 사전순으로 정렬합니다.
        phone_list.sort()
        
        is_consistent = True
        # 2. 인접한 두 문자열만 비교합니다.
        for i in range(n - 1):
            # 현재 숫자가 다음 숫자의 접두어인지 확인
            if phone_list[i+1].startswith(phone_list[i]):
                is_consistent = False
                break
        
        if is_consistent:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()

###############################################################



