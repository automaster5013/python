import sys

def solve():
    # 대량의 입력을 빠르게 읽기 위해 sys.stdin.read().split() 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        
        phone_list = []
        for _ in range(n):
            phone_list.append(input_data[ptr])
            ptr += 1
            
        # 1. 전화번호를 문자열 사전순으로 정렬
        phone_list.sort()
        
        is_consistent = True
        for i in range(n - 1):
            # 2. 현재 번호가 바로 다음 번호의 접두사인지 확인
            # startswith() 함수는 접두사 여부를 판단하기에 최적입니다.
            if phone_list[i+1].startswith(phone_list[i]):
                is_consistent = False
                break
        
        # 3. 결과 출력
        if is_consistent:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()

#########################################################################

