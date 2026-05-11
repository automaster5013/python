import sys

# 파이썬 3.11 이상의 대규모 정수 문자열 변환 제한(ValueError)을 해제합니다.
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(20000000)

def solve():
    # 빠른 입출력을 위해 sys.stdin.read를 사용합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T_cases = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T_cases):
        N = int(input_data[idx])
        S = input_data[idx+1]
        idx += 2
        
        # 1. p 찾기 (처음 1이 등장하는 위치)
        p = S.find('1')
        if p == -1: # 문자열에 '1'이 하나도 없다면 결과는 '0'
            out.append("0")
            continue
            
        s1 = S[p:]
        L = N - p
        
        # 2. K 찾기 (s1에서 1이 연속되는 길이)
        K = s1.find('0')
        if K == -1: # s1 전체가 '1'로만 이루어진 경우
            if p > 0:
                # S 전체에 '0'이 존재했다면, s2로 '0'을 골라 값 유지 가능
                out.append(s1)
            else:
                # S 전체가 '1'뿐이라면, 가장 짧은 '1'을 s2로 골라 끝 비트만 0으로 바꿈
                out.append(s1[:-1] + '0')
            continue
            
        T = s1[K:]
        
        # 3. Z0 찾기 (T에서 제일 앞쪽부터 연속되는 0의 길이)
        Z0 = T.find('1')
        if Z0 == -1:
            Z0 = len(T)
            
        # 4. 결정적인 최적의 시작 위치 유도
        if K >= Z0:
            i = p + K - Z0
        else:
            i = p
            
        # 5. 최적의 s2 추출 및 XOR 결과 연산
        s2_len = L - K
        s2 = S[i : i + s2_len]
        
        # O(N)의 최적화된 파이썬 내장 C루틴 활용 (정수 변환 후 XOR -> 다시 문자열)
        xor_val = int(T, 2) ^ int(s2, 2)
        res_suffix = bin(xor_val)[2:].zfill(s2_len)
        
        res = s1[:K] + res_suffix
        out.append(res)

    print('\n'.join(out))

if __name__ == '__main__':
    solve()

##################################################################################################


