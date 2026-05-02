import sys

# 재귀 깊이 설정 (N=1024일 때 최대 깊이는 10으로 충분합니다)
sys.setrecursionlimit(10000)

def solve():
    # 모든 입력을 읽어와 N과 데이터 문자열을 분리합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    data_str = input_data[1]
    
    # 복원할 N x N 격자 초기화
    grid = [[0] * n for _ in range(n)]
    
    # 문자열을 가리킬 포인터 (인덱스)
    ptr = 0

    def decompress(r, c, size):
        nonlocal ptr
        
        # 현재 위치의 문자 확인 후 포인터 이동
        char = data_str[ptr]
        ptr += 1
        
        if char == 'X':
            # 영역을 4등분하여 재귀 호출
            half = size // 2
            decompress(r, c, half)              # 좌상 (Top-Left)
            decompress(r, c + half, half)       # 우상 (Top-Right)
            decompress(r + half, c, half)       # 좌하 (Bottom-Left)
            decompress(r + half, c + half, half)# 우하 (Bottom-Right)
        else:
            # '0' 또는 '1'이면 해당 영역을 채움
            val = int(char)
            for i in range(r, r + size):
                for j in range(c, c + size):
                    grid[i][j] = val

    # 복원 시작
    decompress(0, 0, n)
    
    # 결과 출력
    print(n)
    # 대용량 출력을 위해 join을 사용하여 속도를 높입니다.
    output = []
    for row in grid:
        output.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

#########################################################################


