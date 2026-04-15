T_str = input()
if T_str:
    T = int(T_str)
    
    for t in range(1, T + 1):
        n = int(input())
        prices = list(map(int, input().split()))
        
        max_price = 0
        total_profit = 0
        
        for i in range(n - 1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            else:
                total_profit += (max_price - prices[i])
        
        print(f"#{t} {total_profit}")


