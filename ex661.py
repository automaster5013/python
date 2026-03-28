# 중첩 if문 코드 작성 완료 - 2개의 출력문 출력 - 디버깅 완료!

yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print("경고 누적 퇴장")
    else:
        print("휴..조심해야지")     // 휴..조심해야지
else:
    print("주의!")

###########################################################################

yellow_card = 1
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print("경고 누적 퇴장")     // 경고 누적 퇴장
    else:
        print("휴..조심해야지")
else:
    print("주의!")

###########################################################################

yellow_card = 0
foul = False
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print("경고 누적 퇴장")
    else:
        print("휴..조심해야지")
else:
    print("주의!")                 // 주의!
