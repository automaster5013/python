def solve_v1():
    # 1. 키와 암호문 입력
    key = input().strip()
    cipher_text = input()
    
    # 알파벳 순서 (a-z)
    alphabet_low = "abcdefghijklmnopqrstuvwxyz"
    alphabet_up = alphabet_low.upper()
    
    # 변환 테이블 생성 (암호문의 'a' 위치에 키의 글자를 매핑)
    trans_table = str.maketrans(alphabet_low + alphabet_up, key + key.upper())
    
    # 번역 실행
    print(cipher_text.translate(trans_table))

solve_v1()

#################################################################################

def solve_v2():
    key = input().strip()
    text = input()
    result = []
    
    for char in text:
        if 'a' <= char <= 'z':
            # 소문자: 키의 (char - 'a')번째 글자 선택
            result.append(key[ord(char) - ord('a')])
        elif 'A' <= char <= 'Z':
            # 대문자: 키의 (char - 'A')번째 글자를 대문자로 변환
            result.append(key[ord(char) - ord('A')].upper())
        else:
            # 공백 및 기타 문자: 그대로 유지
            result.append(char)
            
    print("".join(result))

solve_v2()

#################################################################################

def solve_v3():
    key = input().strip()
    cipher = input()
    
    # 각 문자에 대해 조건별로 처리하여 리스트 생성 후 합치기
    ans = "".join([
        key[ord(c)-97] if 97 <= ord(c) <= 122 else 
        key[ord(c)-65].upper() if 65 <= ord(c) <= 90 else c 
        for c in cipher
    ])
    
    print(ans)

solve_v3()

#################################################################################

def solve_v4():
    key = input().strip()
    cipher = input()
    
    # 매핑 딕셔너리 구축
    mapping = {chr(i + 97): key[i] for i in range(26)}
    mapping.update({chr(i + 65): key[i].upper() for i in range(26)})
    
    # 딕셔너리에 있으면 변환, 없으면(공백 등) 그대로 유지
    print("".join(mapping.get(c, c) for c in cipher))

solve_v4()

#################################################################################

def solve_v5():
    key = input().strip()
    text = input()
    
    def decrypt(c):
        if c.islower():
            return key[ord(c) - ord('a')]
        if c.isupper():
            return key[ord(c) - ord('A')].upper()
        return c
    
    print("".join(map(decrypt, text)))

solve_v5()

#################################################################################

