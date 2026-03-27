
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

###########################################################################(방법01)

score = int(input())
print({10:'A', 9:'A', 8:'B', 7:'C', 6:'D'}.get(score // 10, 'F'))

###########################################################################(방법02)

score = int(input())

if 100>= score and score >= 90:
    print('A')
elif 90 > score and score >= 80:
    print('B')
elif 80 > score and score >= 70:
    print('C')
elif 70 > score and score >= 60:
    print('D')
else:
    print('F')

###########################################################################(방법03)
