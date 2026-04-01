# num1 = 6
# num2 = 0
# try:
#     print('num1 / num2')
#     result = num1 / num2
#     print(num1, '/', num2, ' = ', end = ' ')
#     print(f'연산 결과는 {result}입니다')
# except:
#     print('에러가 발생했어요')
# else:
#     print('정상 동작했어요')
# finally:
#     print('수행 종료')

# # if else문과 비교!!

#################################################################

num1 = 6
num2 = 0
try:
    print('num1 / num2')
    result = num1 / num2
    print(num1, '/', num2, ' = ', end = ' ')
    print(f'연산 결과는 {result}입니다')
except Exception as err:
    print('에러가 발생했어요 : ', err)
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')

# if else문과 비교!!

#################################################################


