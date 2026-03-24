lang = 'PYTHON'
print(lang)
print(lang[0])
print(lang[-1])
print(lang[:3])
print(lang[2:])

num = 3
num += 2    # num = num + 2
print(num)

num -= 1
print(num)
num *= 2
print(num)
num /= 4
print(num)

snack = '꿀꽈배기'
print(len(snack))

snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)

print('-' * 10)
print('NadoCording')
print('*' * 20)

letter = 'how are YOU?'
print(letter.lower())   #모두 소문자
print(letter.upper())   #모두 대문자
print(letter.capitalize())  #전체 문장에서 첫글자만 대문자
print(letter.title())       #단어의 첫글자만 대문자
print(letter.swapcase())    #대소문자를 뒤바꾸기(반전)
print(letter.split())       #문자열 나누기

str1 = letter.split()       #문자열을 나누고 첫글자만 대문자로 만들기
print(str1[0].capitalize())
print(str1[1].capitalize())
print(str1[2].capitalize())

letter = 'how are YOU?'
print(letter.count('how'))  #특정 단어의 수

letter = 'how are you?'
print(letter.count('o'))    #특정 글자의 수
