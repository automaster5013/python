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

s1 = '나도고등학교'
print(s1.startswith('나도'))    #특정 글자의 시작
print(s1.endswith('초등학교'))    #특정 글자의 끝
print(s1.endswith('고등학교'))    #특정 글자의 끝

s2 = '...나도고등학교...'
print(s2.strip('.'))    #앞뒤로 불필요한 부분 잘라내기

s3 = '.,.나도고등학교.,.'
print(s3.strip('.'))    #앞뒤로 불필요한 부분 잘라내기

s4 = '나도고등학교'
print(s4.replace('고등학교', '고교'))    #'고등학교'를 '고교'로 변환하기

s5 = '나도고교너도고교'
print(s5.replace('고교', '고등학교'))    #'고교'를 '고등학교'로 변환하기

s6 = '나도고등학교'
print(s6.find('학교'))    #'학교'라는 글자는 어디에?
print(s6.find('너도'))    #'너도'라는 글자는 어디에? 없으면 -1 출력
print(s6.center(10, '-'))    #다른 문자들 사이에 가운데로
