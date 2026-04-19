def solve():
    max_value = -1  # 최댓값을 저장할 변수 (자연수이므로 0보다 작은 값으로 초기화)
    max_index = 0   # 최댓값의 위치를 저장할 변수
    
    # 9개의 숫자가 한 줄에 하나씩 주어지므로 9번 반복
    for i in range(1, 10):
        try:
            # 입력받은 문자열을 정수로 변환
            num = int(input())
            
            # 현재 입력받은 숫자가 기존의 최댓값보다 크다면 갱신
            if num > max_value:
                max_value = num
                max_index = i # 현재 몇 번째 숫자인지(i) 저장
                
        except EOFError:
            break
            
    # 첫째 줄에 최댓값 출력
    print(max_value)
    # 둘째 줄에 최댓값의 위치 출력
    print(max_index)

# 함수 실행
solve()


