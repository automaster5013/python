def solution(price):
    if price >= 500000:
        price *= 0.8
    elif price >= 300000:
        price *= 0.9
    elif price >= 100000:
        price *= 0.95
        
    return int(price)

p1 = 150000
p2 = 580000

print(solution(p1))
print(solution(p2))

##########################################

def solution(price):
    if 100000 <= price < 300000:
        return int(price * 0.95)
    elif 300000 <= price < 500000:
        return int(price * 0.90)
    elif price >= 500000:
        return int(price * 0.80)
    else:
        return int(price)

p1 = 150000
p2 = 580000

print(solution(p1))
print(solution(p2))

###############################################################

def solution(price):
    if price >= 500000: return int(price*0.8)
    if price >= 300000: return int(price*0.9)
    if price >= 100000: return int(price*0.95)
    return price

###############################################################

def solution(price):
    rate = 0.8 if price >= 500000 else 0.9 if price >= 300000 else 0.95 if price >= 100000 else 1
    return int(price * rate)

###############################################################











































