import sys

def solve():
    # 고속 입력을 통해 N, M, Q와 수열 A를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m, q = map(int, input_data[:3])
    a = list(map(int, input_data[3:3+n]))
    queries = input_data[3+n:]

    # 차분 배열 (망각 스케줄링용)
    # 단어가 최대 10,000일(A_i/M)까지 생존할 수 있으므로 넉넉하게 크기 설정
    limit = n + 10005
    diff = [0] * (limit + 1)

    # 1. 각 단어 뭉치별로 망각 계획 세우기
    for i in range(n):
        day = i + 1  # 1-indexed
        count = a[i]
        
        # 매일 M개씩 사라지는 일수
        d_i = (count - 1) // m
        
        if d_i > 0:
            # [day + 1, day + d_i] 기간 동안 매일 M개씩 망각
            diff[day + 1] += m
            if day + d_i + 1 <= limit:
                diff[day + d_i + 1] -= m
        
        # 마지막 남은 잔여 단어가 사라지는 날 (day + d_i + 1)
        remaining = count - (d_i * m)
        if day + d_i + 1 <= limit:
            diff[day + d_i + 1] += remaining
            if day + d_i + 2 <= limit:
                diff[day + d_i + 2] -= remaining

    # 2. 누적합을 통해 각 날짜별 잊어버리는 단어 수(Forgotten) 계산
    forgotten_on_day = [0] * (n + 1)
    current_forget = 0
    for t in range(1, n + 1):
        current_forget += diff[t]
        forgotten_on_day[t] = current_forget

    # 3. 기억하고 있는 단어 수(Remembered) 계산
    # 점화식: Remembered[t] = Remembered[t-1] - Forgotten[t] + A[t]
    remembered_on_day = [0] * (n + 1)
    for t in range(1, n + 1):
        remembered_on_day[t] = remembered_on_day[t-1] - forgotten_on_day[t] + a[t-1]

    # 4. 쿼리 응답
    output = []
    for i in range(0, len(queries), 2):
        type = int(queries[i])
        t = int(queries[i+1])
        
        if type == 1:
            output.append(str(remembered_on_day[t]))
        else:
            output.append(str(forgotten_on_day[t]))

    # 결과 일괄 출력
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

###################################################################################


