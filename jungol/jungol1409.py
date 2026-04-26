import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(2000)

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 벽장 개수
    open1 = int(input_data[1]) # 초기 열린 벽장 1
    open2 = int(input_data[2]) # 초기 열린 벽장 2
    
    m = int(input_data[3]) # 사용할 벽장의 개수
    targets = [int(x) for x in input_data[4:]] # 사용할 벽장 순서
    
    # 메모이제이션을 위한 테이블 (3차원 배열 또는 딕셔너리)
    memo = {}

    def get_min_moves(idx, o1, o2):
        # 모든 벽장을 다 사용한 경우
        if idx == m:
            return 0
        
        state = (idx, o1, o2)
        if state in memo:
            return memo[state]
        
        target = targets[idx]
        
        # 선택 1: 첫 번째 열린 공간을 target으로 이동
        move1 = abs(target - o1) + get_min_moves(idx + 1, target, o2)
        
        # 선택 2: 두 번째 열린 공간을 target으로 이동
        move2 = abs(target - o2) + get_min_moves(idx + 1, o1, target)
        
        # 두 선택 중 최솟값을 저장
        memo[state] = min(move1, move2)
        return memo[state]

    # 결과 출력
    print(get_min_moves(0, open1, open2))

if __name__ == "__main__":
    solve()

##########################################################################

