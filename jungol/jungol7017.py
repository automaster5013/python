import sys

def solve():
    # 대량의 입력을 빠르게 읽기 위해 sys.stdin 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))
    
    total_ops = 0
    current_x = 0  # 현재 원소에 적용되어야 할 2의 지수(연산 횟수)
    
    for i in range(n - 1):
        v1 = a[i]
        v2 = a[i+1]
        
        if v1 < v2:
            # v1에 2를 몇 번 곱해야 v2를 넘어가는지(slack) 계산
            g = 0
            temp = v1
            while temp * 2 <= v2:
                temp *= 2
                g += 1
            # 이전 원소의 연산 횟수에서 여유분(g)만큼 줄일 수 있음
            current_x = max(0, current_x - g)
            
        elif v1 > v2:
            # v2에 2를 최소 몇 번 곱해야 v1 이상이 되는지 계산
            l = 0
            temp = v2
            while temp < v1:
                temp *= 2
                l += 1
            # 이전 원소의 연산 횟수에 추가분(l)만큼 더함
            current_x = current_x + l
        
        # v1 == v2 인 경우 current_x는 변하지 않음
        total_ops += current_x
        
    print(total_ops)

if __name__ == "__main__":
    solve()

#######################################################################

