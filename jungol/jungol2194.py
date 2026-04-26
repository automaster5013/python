import sys

def solve():
    # 데이터를 한 번에 읽어와 토큰화합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 주(Week) 수
    s = int(input_data[1]) # 주당 보관 비용
    
    total_cost = 0
    # 현재까지 알려진 1리터당 최소 비용 (첫 주는 무조건 첫 주 가격)
    # 초기값은 첫 주의 가격으로 설정합니다.
    current_min_price = float('inf')
    
    idx = 2
    for _ in range(n):
        c_i = int(input_data[idx])   # 이번 주 가격
        y_i = int(input_data[idx+1]) # 이번 주 필요량
        idx += 2
        
        # 1. 이번 주 우유를 확보하는 가장 저렴한 단가 갱신
        # (이번 주에 새로 사기 vs 지난주까지의 최저가 + 보관비)
        current_min_price = min(current_min_price + s, c_i)
        
        # 2. 최저 단가로 필요한 양만큼 비용 합산
        total_cost += current_min_price * y_i
        
    # 최종 최소 비용 출력
    print(total_cost)

if __name__ == "__main__":
    solve()

#####################################################################

