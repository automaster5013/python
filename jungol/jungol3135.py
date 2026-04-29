import sys
from array import array

def solve():
    # 1. 제너레이터를 이용한 메모리 효율적 입력
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield int(word)
    
    reader = get_input()
    
    try:
        n = next(reader)
    except StopIteration:
        return
    
    # 2. array.array 사용 (타입 'q'는 8바이트 정수, 누적 합이 커질 수 있으므로 권장)
    # 리스트보다 메모리 사용량을 1/4 이하로 줄여줍니다.
    prefix_sum = array('q', [0] * (n + 1))
    
    for i in range(1, n + 1):
        # 이전 합에 현재 숫자를 더함
        prefix_sum[i] = prefix_sum[i-1] + next(reader)
        
    try:
        q = next(reader)
    except StopIteration:
        return

    # 3. 출력 최적화: 리스트에 담지 않고 즉시 출력
    # sys.stdout.write는 print보다 빠르며, 메모리 점유가 낮습니다.
    out = sys.stdout
    for _ in range(q):
        try:
            s = next(reader)
            e = next(reader)
            # O(1) 구간 합 계산
            result = prefix_sum[e] - prefix_sum[s-1]
            out.write(str(result) + '\n')
        except StopIteration:
            break

if __name__ == "__main__":
    solve()

######################################################################################


