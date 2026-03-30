# message = '나는야 전역 변수'        # 전역변수
# print(message)

# def no_secret():
#     print(message)      # '나는야 전역 변수' 출력!!

# no_secret()

##########################################################

message = '나는야 전역 변수'        # 전역변수
print(message)

def no_secret():
    message = '이러면 또 지역변수'        # 지역변수
    print(message)      # '이러면 또 지역변수' 출력!!

no_secret()
print(message)


