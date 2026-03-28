def get_price(is_vip=False): # True: 단골손님, False: 일반손님 ---> Default Parameter
    if is_vip == True:
        return 10000 #단골손님
    else:
        return 15000 #일반손님

price1 = get_price(True) #단골손님
print(price1)
price2 = get_price() #일반손님
print(price2)
price3 = get_price() #일반손님
print(price3)
price4 = get_price() #일반손님
print(price4)

#####################################################################################

