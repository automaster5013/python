def solve():
    # 1. 그릇의 모양을 나타내는 괄호 문자열 입력 받기
    try:
        dishes = input().strip()
        if not dishes:
            return
    except EOFError:
        return

    # 2. 첫 번째 그릇은 항상 바닥에 놓이므로 높이는 10cm로 시작
    total_height = 10
    
    # 3. 두 번째 그릇부터 마지막 그릇까지 순서대로 확인
    # 인덱스 1부터 문자열 끝까지 반복
    for i in range(1, len(dishes)):
        # 현재 그릇(dishes[i])과 바로 직전의 그릇(dishes[i-1])을 비교
        if dishes[i] == dishes[i-1]:
            # 같은 방향이면 5cm 증가
            total_height += 5
        else:
            # 반대 방향이면 10cm 증가
            total_height += 10
            
    # 4. 최종 높이 출력
    print(total_height)

# 함수 실행
solve()

########################################################################

def solve_v1():
    s = input().strip()
    if not s: return
    
    # 첫 그릇은 항상 10
    height = 10
    
    # 두 번째 그릇부터 끝까지 확인
    for i in range(1, len(s)):
        # 앞의 그릇과 방향이 같으면 5, 다르면 10 추가
        if s[i] == s[i-1]:
            height += 5
        else:
            height += 10
            
    print(height)

solve_v1()

########################################################################

def solve_v2():
    s = input().strip()
    
    # 첫 번째 그릇 높이 10으로 시작
    total = 10
    
    # zip(s, s[1:])를 하면 (1번째, 2번째), (2번째, 3번째)... 쌍이 생성됨
    for prev, curr in zip(s, s[1:]):
        total += 5 if prev == curr else 10
        
    print(total)

solve_v2()

########################################################################

def solve_v3():
    s = input().strip()
    # 10(첫 그릇) + [나머지 그릇들의 가산점들]
    result = 10 + sum(5 if s[i] == s[i-1] else 10 for i in range(1, len(s)))
    print(result)

solve_v3()

########################################################################

def solve_v4():
    plates = input().strip()
    ans = 0
    last = ""
    
    for p in plates:
        if p == last:
            ans += 5 # 같은 방향
        else:
            ans += 10 # 다른 방향 (첫 그릇도 여기에 해당됨)
        last = p
        
    print(ans)

solve_v4()

########################################################################

def solve_v5():
    s = input().strip()
    # {일치여부: 더할 높이}
    weights = {True: 5, False: 10}
    
    h = 10
    for i in range(1, len(s)):
        # s[i] == s[i-1] 결과값(True/False)을 키로 사용
        h += weights[s[i] == s[i-1]]
        
    print(h)

solve_v5()

########################################################################

