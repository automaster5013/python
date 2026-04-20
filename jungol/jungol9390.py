hour = int(input())
minute = int(input())
# print(hour, minute)

print(f"{hour:02d}:{minute:02d}")

##################################################################(방법01)

h = int(input())
m = int(input())
# print(h, m)

# 중괄호 안에 포맷팅 규칙을 넣고 format 함수로 값을 전달
print("{:02d}:{:02d}".format(h, m))

##################################################################(방법02)

hour = int(input())
minute = int(input())
# print(hour, minute)

# %02d를 사용하여 형식을 지정
print("%02d:%02d" % (hour, minute))

##################################################################(방법03)

h = input()
m = input()
# print(h, m)

# zfill(2)는 문자열이 2자리가 될 때까지 왼쪽에 '0'을 채움
print(h.zfill(2) + ":" + m.zfill(2))

##################################################################(방법04)

time = int(input())
minute = int(input())
# print(hour, minute)

print(f"{hour:02d}:{minute:02d}")

##################################################################(방법05)

