import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    bit = []
    S = 0

    while ptr < len(input_data):
        cmd = input_data[ptr]
        
        if cmd == '0':
            # 0 S: 기지국 영역 크기 초기화
            S = int(input_data[ptr + 1])
            # BIT는 1-based 인덱싱을 사용하므로 (S+1) 크기로 생성합니다.
            bit = [[0] * (S + 1) for _ in range(S + 1)]
            ptr += 2
            
        elif cmd == '1':
            # 1 X Y A: (X, Y) 위치에 A개 추가
            x = int(input_data[ptr + 1]) + 1
            y = int(input_data[ptr + 2]) + 1
            a = int(input_data[ptr + 3])
            
            i = x
            while i <= S:
                j = y
                while j <= S:
                    bit[i][j] += a
                    j += j & (-j)
                i += i & (-i)
            ptr += 4
            
        elif cmd == '2':
            # 2 L B R T: 영역 [L, B] ~ [R, T]의 전화 개수 합산
            l = int(input_data[ptr + 1])
            b = int(input_data[ptr + 2])
            r = int(input_data[ptr + 3])
            t = int(input_data[ptr + 4])
            
            # 구간 합 계산 함수 (Inclusion-Exclusion Principle 사용)
            def get_sum(x_idx, y_idx):
                res = 0
                i = x_idx + 1
                while i > 0:
                    j = y_idx + 1
                    while j > 0:
                        res += bit[i][j]
                        j -= j & (-j)
                    i -= i & (-i)
                return res

            # 영역 합 = sum(R, T) - sum(L-1, T) - sum(R, B-1) + sum(L-1, B-1)
            ans = get_sum(r, t) - get_sum(l - 1, t) - get_sum(r, b - 1) + get_sum(l - 1, b - 1)
            sys.stdout.write(str(ans) + '\n')
            ptr += 5
            
        elif cmd == '3':
            # 3: 프로그램 종료
            break
        else:
            ptr += 1

if __name__ == "__main__":
    solve()

###################################################################################################


