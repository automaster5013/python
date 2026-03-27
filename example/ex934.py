def get_price(is_vip):     # is_vip = True        # True: 단골손님, False: 일반손님
    if is_vip == True:
        return 10000    # 단골손님
    else:
        return 15000    # 일반손님

price = get_price(True)
print(f'커트 가격은 {price} 원입니다')

price = get_price(False)
print(f'커트 가격은 {price} 원입니다')








