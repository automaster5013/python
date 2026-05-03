import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(2000)

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])  # 방학 일수
    m = int(input_data[1])  # 갈 수 없는 날 수
    
    unavailable = [False] * (n + 1)
    if m > 0:
        days = list(map(int, input_data[2:]))
        for d in days:
            unavailable[d] = True

    # 2. 메모이제이션 테이블 초기화
    # dp[날짜][쿠폰수]
    memo = [[-1] * (n + 6) for _ in range(n + 6)]

    def get_min_cost(day, coupons):
        # 방학 기간을 넘어가면 종료
        if day > n:
            return 0
        
        # 이미 계산된 결과가 있으면 반환
        if memo[day][coupons] != -1:
            return memo[day][coupons]

        # 리조트에 갈 수 없는 날인 경우
        if unavailable[day]:
            memo[day][coupons] = get_min_cost(day + 1, coupons)
            return memo[day][coupons]

        # 3. 4가지 경우의 수 중 최솟값 찾기
        res = float('inf')
        
        # 경우 1: 1일권 구매
        res = min(res, get_min_cost(day + 1, coupons) + 10000)
        
        # 경우 2: 3일권 구매 (연속 3일, 쿠폰 1장)
        res = min(res, get_min_cost(day + 3, coupons + 1) + 25000)
        
        # 경우 3: 5일권 구매 (연속 5일, 쿠폰 2장)
        res = min(res, get_min_cost(day + 5, coupons + 2) + 37000)
        
        # 경우 4: 쿠폰 3장 사용 (비용 0)
        if coupons >= 3:
            res = min(res, get_min_cost(day + 1, coupons - 3))

        memo[day][coupons] = res
        return res

    # 결과 출력
    print(get_min_cost(1, 0))

if __name__ == "__main__":
    solve()

########################################################################

