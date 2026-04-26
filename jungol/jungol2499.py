import sys

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    # 저울추 무게 리스트 (정수로 변환)
    weights = sorted([int(x) for x in input_data[1:]])
    
    # target: 우리가 현재 '만들 수 있는지' 확인하려는 최소 무게
    # 초기값은 1 (가장 작은 양의 정수)
    target = 1
    
    for w in weights:
        # 현재 추가 확인하려는 target보다 크다면, target 무게를 만들 빈틈이 생긴 것임
        if w > target:
            break
        
        # 추가 target보다 작거나 같다면, target까지의 모든 무게를 빈틈없이 채울 수 있음
        # 이제 측정 가능한 범위는 (기존 범위 + w)까지 늘어남
        target += w
        
    print(target)

if __name__ == "__main__":
    solve()

########################################################################################

