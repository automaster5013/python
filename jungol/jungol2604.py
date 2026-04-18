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


