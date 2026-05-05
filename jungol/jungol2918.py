import sys
import random

def solve():
    # 입력을 빠르게 읽어오기 위해 처리합니다.
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    
    s1 = input_data[0]
    s2 = input_data[1]
    
    n, m = len(s1), len(s2)
    
    # 1. 각 알파벳(a-z)에 대해 64비트 랜덤 가중치 부여
    # 해시 충돌 방지를 위해 충분히 큰 난수를 사용합니다.
    char_weights = [random.getrandbits(64) for _ in range(26)]
    
    # 2. 첫 번째 문자열의 모든 구간 해시 계산 및 저장
    # sets_s1[length] = {해시값1, 해시값2, ...}
    sets_s1 = [set() for _ in range(n + 1)]
    for i in range(n):
        current_hash = 0
        for j in range(i, n):
            # 문자의 가중치를 더해 애너그램 해시 생성
            current_hash += char_weights[ord(s1[j]) - ord('a')]
            sets_s1[j - i + 1].add(current_hash)
            
    # 3. 두 번째 문자열의 모든 구간을 검사하며 최장 길이 갱신
    max_len = 0
    for i in range(m):
        current_hash = 0
        for j in range(i, m):
            current_hash += char_weights[ord(s2[j]) - ord('a')]
            length = j - i + 1
            
            # s1에 같은 성분을 가진 동일 길이의 구간이 존재하는지 확인
            if length <= n and current_hash in sets_s1[length]:
                if length > max_len:
                    max_len = length
                    
    print(max_len)

if __name__ == "__main__":
    solve()

#####################################################################



