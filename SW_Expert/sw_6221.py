options = ["가위", "바위", "보"]
man1 = input()
man2 = input()

win_dic = {
    "가위": "보",
    "바위": "가위",
    "보": "바위"
}

if man1 == man2:
    print("Result : Draw")
elif win_dic[man1] == man2:
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")

############################################(방법01)

options = ["가위", "바위", "보"]
m1_idx = options.index(input())
m2_idx = options.index(input())

result = (m1_idx - m2_idx) % 3

if result == 0:
    print("Result : Draw")
elif result == 1:
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")

############################################(방법02)

