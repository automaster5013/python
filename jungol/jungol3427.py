import sys

def solve():
    # 입력 속도 최적화
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    # 1. 각 색깔별 전체 공의 개수 카운트
    total_r = s.count('R')
    total_b = n - total_r
    
    # 만약 한 종류의 공만 있다면 이동할 필요가 없음
    if total_r == 0 or total_b == 0:
        print(0)
        return

    # 2. 각 방향 끝에 연속된 공의 개수 구하기
    # 왼쪽 끝에서 연속된 공 체크
    left_count = 0
    for i in range(n):
        if s[i] == s[0]:
            left_count += 1
        else:
            break
            
    # 오른쪽 끝에서 연속된 공 체크
    right_count = 0
    for i in range(n - 1, -1, -1):
        if s[i] == s[-1]:
            right_count += 1
        else:
            break

    # 3. 4가지 케이스 계산
    res = []
    
    # 케이스 1 & 2: 빨간 공을 옮기는 경우
    if s[0] == 'R':
        res.append(total_r - left_count) # 빨간 공 왼쪽으로 (왼쪽 끝이 R인 경우)
        res.append(total_b)              # 파란 공 오른쪽으로 (이때 파란 공은 왼쪽 끝에 없으므로 전체가 이동)
    else:
        res.append(total_r)              # 빨간 공 왼쪽으로
        res.append(total_b - left_count) # 파란 공 왼쪽으로

    if s[-1] == 'R':
        res.append(total_r - right_count) # 빨간 공 오른쪽으로
        res.append(total_b)               # 파란 공 왼쪽으로
    else:
        res.append(total_r)               # 빨간 공 오른쪽으로
        res.append(total_b - right_count) # 파란 공 오른쪽으로

    # 4. 최솟값 출력
    print(min(res))

solve()

#############################################################################################################

