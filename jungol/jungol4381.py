import sys
import array
import re

# 메모리 절약을 위해 정규식을 이용한 토큰 제너레이터 사용
def get_tokens():
    for line in sys.stdin:
        for match in re.finditer(r'\S+', line):
            yield match.group()

def solve():
    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
        m = int(next(tokens))
    except StopIteration:
        return

    # 'i'는 부호 있는 4바이트 정수 (최대 21억). 
    # 전체 군사력 합이 10억이므로 BIT와 배열 모두 'i'로 충분합니다.
    # 300,000 * 4 bytes * 2 (a, bit) = 약 2.4MB 소모
    a = array.array('i', [0] * (n + 1))
    bit = array.array('i', [0] * (n + 1))

    # 초기 군사력 입력 및 BIT 구축
    for idx in range(1, n + 1):
        val = int(next(tokens))
        a[idx] = val
        curr = idx
        while curr <= n:
            bit[curr] += val
            curr += curr & (-curr)

    # 전쟁 기록 처리
    for _ in range(m):
        try:
            l = int(next(tokens))
            i = int(next(tokens))
            r = int(next(tokens))
            s = int(next(tokens))
            j = int(next(tokens))
            e = int(next(tokens))
        except StopIteration:
            break
            
        # 상류 연합(l~r) 합 계산
        sum1 = 0
        curr = r
        while curr > 0:
            sum1 += bit[curr]
            curr -= curr & (-curr)
        curr = l - 1
        while curr > 0:
            sum1 -= bit[curr]
            curr -= curr & (-curr)
            
        # 하류 연합(s~e) 합 계산
        sum2 = 0
        curr = e
        while curr > 0:
            sum2 += bit[curr]
            curr -= curr & (-curr)
        curr = s - 1
        while curr > 0:
            sum2 -= bit[curr]
            curr -= curr & (-curr)
            
        if sum1 > sum2:
            # 상류 승리: j의 리더 군사력 절반을 i의 리더가 가져감
            loss = (a[j] + 1) // 2
            if loss > 0:
                a[i] += loss
                a[j] -= loss
                # 펜윅 트리 갱신
                curr = i
                while curr <= n:
                    bit[curr] += loss
                    curr += curr & (-curr)
                curr = j
                while curr <= n:
                    bit[curr] -= loss
                    curr += curr & (-curr)
        elif sum2 > sum1:
            # 하류 승리: i의 리더 군사력 절반을 j의 리더가 가져감
            loss = (a[i] + 1) // 2
            if loss > 0:
                a[j] += loss
                a[i] -= loss
                # 펜윅 트리 갱신
                curr = j
                while curr <= n:
                    bit[curr] += loss
                    curr += curr & (-curr)
                curr = i
                while curr <= n:
                    bit[curr] -= loss
                    curr += curr & (-curr)

    # 최종 군사력 출력 (메모리 보존을 위해 반복문 출력)
    for k in range(1, n + 1):
        sys.stdout.write(str(a[k]))
        if k < n:
            sys.stdout.write(" ")
    sys.stdout.write("\n")

if __name__ == '__main__':
    solve()

######################################################################


