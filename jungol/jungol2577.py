import sys

def solve():
    # 1. 스트림 입력을 위한 제너레이터 설정
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield int(word)
    
    gen = get_input()
    
    try:
        n = next(gen)
        d = next(gen)
        k = next(gen)
        c = next(gen)
    except StopIteration:
        return

    # 2. 벨트 정보 입력 (문자열 리스트 생성을 피함)
    # 300만 개의 정수 리스트는 약 80~100MB 정도를 차지합니다.
    belt = [next(gen) for _ in range(n)]

    # 각 초밥 종류별 개수 카운팅
    eat_count = [0] * (d + 1)
    
    # 3. 초기 윈도우 설정 (0번부터 k-1번까지)
    current_variety = 0
    for i in range(k):
        sushi = belt[i]
        if eat_count[sushi] == 0:
            current_variety += 1
        eat_count[sushi] += 1
        
    # 쿠폰 초밥 포함 여부 체크
    max_variety = current_variety + (1 if eat_count[c] == 0 else 0)
    
    # 4. 슬라이딩 윈도우 수행
    # 인덱스 i는 현재 윈도우에서 '빠질' 초밥의 위치입니다.
    for i in range(n):
        # (1) 왼쪽 초밥 제거 (belt[i])
        out_sushi = belt[i]
        eat_count[out_sushi] -= 1
        if eat_count[out_sushi] == 0:
            current_variety -= 1
            
        # (2) 오른쪽 초밥 추가 (belt[(i + k) % n])
        # 나머지 연산을 사용하여 원형 벨트를 물리적 복사 없이 구현
        in_sushi = belt[(i + k) % n]
        if eat_count[in_sushi] == 0:
            current_variety += 1
        eat_count[in_sushi] += 1
        
        # (3) 최댓값 갱신
        res = current_variety + (1 if eat_count[c] == 0 else 0)
        if res > max_variety:
            max_variety = res
            
    sys.stdout.write(str(max_variety) + '\n')

if __name__ == "__main__":
    solve()

#########################################################################

