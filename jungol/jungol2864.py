import sys
from functools import lru_cache

# 재귀 깊이 제한을 넉넉히 설정합니다.
sys.setrecursionlimit(200000)

def solve():
    # 입력 처리: h1, w1(전체 외곽), h2, w2(제거된 사각형 크기)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    h1, w1, h2, w2 = map(int, input_data)

    # 1. 직사각형 최소 정사각형 분할 DP (50x50)
    # dp_rect[i][j]: i x j 직사각형을 채우는 최소 정사각형 개수
    dp_rect = [[0] * 51 for _ in range(51)]
    for i in range(1, 51):
        for j in range(1, 51):
            if i == j:
                dp_rect[i][j] = 1
                continue
            res = i * j # 최대 개수로 초기화
            # 모든 수평 절단 탐색
            for k in range(1, i // 2 + 1):
                res = min(res, dp_rect[k][j] + dp_rect[i - k][j])
            # 모든 수직 절단 탐색
            for k in range(1, j // 2 + 1):
                res = min(res, dp_rect[i][k] + dp_rect[i][j - k])
            dp_rect[i][j] = res

    # 2. L 모양 종이 최소 분할 DP (메모이제이션)
    # H, W: 전체 크기 / h, w: 제거된(비어있는) 부분의 크기
    @lru_cache(None)
    def get_L(H, W, h, w):
        # 제거된 부분이 없으면 일반 직사각형 결과 반환
        if h <= 0 or w <= 0:
            return dp_rect[H][W]
        
        res = float('inf')
        
        # [수평 절단 시도]
        for y in range(1, H):
            if y < H - h:
                # 아래쪽(꽉 찬 부분)을 자름: (아래: 직사각형) + (위: L 모양)
                res = min(res, dp_rect[y][W] + get_L(H - y, W, h, w))
            elif y == H - h:
                # 꺾이는 경계선을 자름: (아래: 직사각형) + (위: 직사각형)
                res = min(res, dp_rect[H - h][W] + dp_rect[h][W - w])
            else:
                # 위쪽(비어있는 부분을 포함)을 자름: (아래: L 모양) + (위: 직사각형)
                # 이때 위쪽 조각의 가로 길이는 W - w 가 됩니다.
                res = min(res, get_L(y, W, y - (H - h), w) + dp_rect[H - y][W - w])
                
        # [수직 절단 시도]
        for x in range(1, W):
            if x < W - w:
                # 왼쪽(꽉 찬 부분)을 자름: (왼쪽: 직사각형) + (오른쪽: L 모양)
                res = min(res, dp_rect[H][x] + get_L(H, W - x, h, w))
            elif x == W - w:
                # 꺾이는 경계선을 자름: (왼쪽: 직사각형) + (오른쪽: 직사각형)
                res = min(res, dp_rect[H][W - w] + dp_rect[H - h][w])
            else:
                # 오른쪽(비어있는 부분을 포함)을 자름: (왼쪽: L 모양) + (오른쪽: 직사각형)
                # 이때 오른쪽 조각의 세로 길이는 H - h 가 됩니다.
                res = min(res, get_L(H, x, h, x - (W - w)) + dp_rect[H - h][W - x])
                
        return res

    # 문제의 h2, w2를 '제거된 상단 사각형'으로 해석하여 호출
    print(get_L(h1, w1, h2, w2))

if __name__ == "__main__":
    solve()

###########################################################################################



