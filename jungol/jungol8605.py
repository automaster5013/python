import sys

def solve():
    # 대량의 데이터를 빠르게 읽어오기 위해 sys.stdin.read() 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 거울의 수
    s = int(input_data[1]) # 초기 위치
    
    # 거울 위치 리스트 (이미 정렬된 상태로 주어짐)
    a = list(map(int, input_data[2:]))
    
    # 1. 계수가 -2인 그룹과 +2인 그룹으로 나눌 기준점(mid) 설정
    # N이 짝수면 N//2, N이 홀수면 (N-1)//2 개가 마이너스 그룹이 됨
    mid = n // 2
    
    # 2. 작은 쪽 그룹(low)과 큰 쪽 그룹(high)의 합 계산
    sum_low = sum(a[:mid])
    sum_high = sum(a[mid:])
    
    # 3. N의 홀짝에 따른 공식 적용
    # N이 짝수: 2 * (Sum_High - Sum_Low) + S
    # N이 홀수: 2 * (Sum_High - Sum_Low) - S
    if n % 2 == 0:
        ans = 2 * (sum_high - sum_low) + s
    else:
        ans = 2 * (sum_high - sum_low) - s
        
    # 결과 출력 (64비트 이상의 큰 정수도 파이썬은 자동으로 처리함)
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()

######################################################################






