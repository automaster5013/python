import sys

def solve():
    # 입력 받기
    line = sys.stdin.readline().strip()
    if not line:
        return
    try:
        n = int(line)
    except ValueError:
        return

    ans_set = set()

    # X를 A, d, B로 나눕니다.
    # X = A * 10^(k+1) + d * 10^k + B
    # Y = A * 10^k + B
    # N = X + Y = 10^k * (11A + d) + 2B
    
    # N이 최대 10^9이므로 k는 0부터 10까지면 충분합니다.
    for k in range(11):
        p10 = 10**k
        rem = n % p10
        
        # 0 <= 2B < 2 * 10^k 조건을 만족하는 2B의 후보는 두 가지입니다.
        # 1) 2B = rem
        # 2) 2B = rem + 10^k
        for val_2b in [rem, rem + p10]:
            if val_2b % 2 == 0:
                b = val_2b // 2
                if b < p10:
                    # (11A + d) 값을 구합니다.
                    target = (n - 2 * b) // p10
                    if target >= 0:
                        a, d = divmod(target, 11)
                        if d < 10:
                            # 후보 X 계산
                            x = a * (p10 * 10) + d * p10 + b
                            x_s = str(x)
                            
                            # 조건 검증:
                            # 1. 첫 자릿수는 0이 아니어야 함 (x_s[0] != '0')
                            # 2. 첫 번째 수는 두 자리 이상의 수 (x >= 10)
                            # 3. 실제로 k번째 자릿수를 제거할 수 있을 만큼 자릿수가 있어야 함 (len >= k+1)
                            if x >= 10 and x_s[0] != '0' and len(x_s) >= k + 1:
                                y_val = a * p10 + b
                                # Y는 X보다 자릿수가 하나 적어야 함 (zfill 사용)
                                y_s = str(y_val).zfill(len(x_s) - 1)
                                
                                # 최종 수식 확인
                                if x + int(y_s) == n:
                                    ans_set.add((x, y_s))

    # X의 오름차순으로 정렬
    sorted_ans = sorted(list(ans_set))
    
    # 결과 출력
    print(len(sorted_ans))
    for x, y_s in sorted_ans:
        print(f"{x} + {y_s} = {n}")

if __name__ == "__main__":
    solve()

###############################################################################################################



