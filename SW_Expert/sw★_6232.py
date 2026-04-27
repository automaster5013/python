word = input()
print(word)

if word == word[::-1]:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

##############################################################(방법01)

word = input()
print(word)

is_palindrome = True
length = len(word)

for i in range(length // 2):
    if word[i] != word[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

##############################################################(방법02)


