def solve():
    # 현재 기차에 타고 있는 사람 수
    current_people = 0
    # 역들 중 가장 사람이 많았을 때의 수
    max_people = 0
    
    # 총 4개의 역을 순서대로 확인
    for _ in range(4):
        try:
            # 각 역에서 내린 사람(out_p)과 탄 사람(in_p) 입력 받기
            data = input().split()
            if not data:
                break
            
            out_p = int(data[0]) # 내린 사람 수
            in_p = int(data[1])  # 탄 사람 수
            
            # 1. 내린 사람 수만큼 빼고, 탄 사람 수만큼 더함
            # 문제 조건에 따라 내릴 사람이 다 내린 후에 사람이 탄다.
            current_people = current_people - out_p + in_p
            
            # 2. 현재 인원이 역대 최다 인원보다 많으면 갱신
            if current_people > max_people:
                max_people = current_people
                
        except EOFError:
            break
            
    # 최종 결과 출력
    print(max_people)

# 함수 실행
solve()

