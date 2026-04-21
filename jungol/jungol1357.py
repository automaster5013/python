def solve():
    # 1. 입력 처리
    try:
        line = input().split()
        if not line:
            return
        n = int(line[0])
    except EOFError:
        return

    # 각 목록(A, B, C, D)을 저장할 리스트
    a_list = [0] * n
    b_list = [0] * n
    c_list = [0] * n
    d_list = [0] * n

    for i in range(n):
        row = list(map(int, input().split()))
        a_list[i] = row[0]
        b_list[i] = row[1]
        c_list[i] = row[2]
        d_list[i] = row[3]

    # 2. A와 B의 모든 합 조합을 딕셔너리에 빈도수와 함께 저장
    # 시간 복잡도: O(n^2)
    sum_ab = {}
    for a in a_list:
        for b in b_list:
            s = a + b
            if s in sum_ab:
                sum_ab[s] += 1
            else:
                sum_ab[s] = 1

    # 3. C와 D의 모든 합을 구하며 -(c+d)가 존재하는지 확인
    # 시간 복잡도: O(n^2)
    count = 0
    for c in c_list:
        for d in d_list:
            target = -(c + d)
            if target in sum_ab:
                count += sum_ab[target]

    # 4. 결과 출력
    print(count)

# 프로그램 실행
solve()

#########################################################################

