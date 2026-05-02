import sys

def solve():
    # 전체 입력을 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a = int(input_data[0])
    b = int(input_data[1])
    
    d = b - a
    
    # g: |d|의 가장 큰 홀수 약수
    if d == 0:
        g = 0
    else:
        g = abs(d)
        while g % 2 == 0:
            g //= 2
            
    results = []
    
    # 5개의 목표 점에 대해 판별
    for i in range(5):
        p = int(input_data[2 + 2*i])
        q = int(input_data[3 + 2*i])
        D = q - p
        
        # 조건에 따른 판별 (차이의 부호 및 배수 조건)
        if d == 0:
            if D == 0:
                results.append("Y")
            else:
                results.append("N")
        elif d > 0:
            if D > 0 and D % g == 0:
                results.append("Y")
            else:
                results.append("N")
        else: # d < 0 인 경우
            if D < 0 and (-D) % g == 0:
                results.append("Y")
            else:
                results.append("N")
                
    # 일괄 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()

###########################################################

