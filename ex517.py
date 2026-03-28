# 딕셔너리 예제 연습

person = {'이름':'나귀욤', 
'나이':'7', 
'키':'120', 
'몸무게':'23'}

# print(person['이름'])
# print(person['나이'])
# # print(person['별명'])   # Key 에러발생
# print(person.get('별명'))   # None 출력
# print(person.get('이름'))   # 나귀욤 정상 출력

print(person)
person['최종학력'] = '유치원'
print(person)

person['키'] = 130      # '키'값 수정
print(person)

person.update({'키':140, '몸무게':26})  #키, 몸무게 수정 가능O
print(person)

person.pop('몸무게')  #몸무게 삭제O
print(person)

# person.clear()  #모든 데이터 삭제O
# print(person)

print(person.keys())

print(person.values())

print(person.items())


