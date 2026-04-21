# 1. 입력 받기
n_line = input().strip()
if not n_line:
    exit()
N = int(n_line)

jobs = []
for i in range(1, N + 1):
    # T(소요시간)와 S(보상금)를 입력받음
    t_s = input().split()
    if not t_s:
        continue
    T = int(t_s[0])
    S = int(t_s[1])
    # [소요시간, 보상금, 원래 번호] 저장
    jobs.append([T, S, i])

# 2. 정렬 알고리즘 (버블 정렬 사용)
# 정렬 기준: T1 * S2 와 T2 * S1 을 비교하여 교환
# 비율(S/T)로 비교할 경우 소수점 오차가 생길 수 있어 곱셈으로 비교합니다.
for i in range(N):
    for j in range(0, N - i - 1):
        # 현재 작업(j)과 다음 작업(j+1) 비교
        # T_j * S_{j+1} > T_{j+1} * S_j 이면 순서 교체
        if jobs[j][0] * jobs[j+1][1] > jobs[j+1][0] * jobs[j][1]:
            jobs[j], jobs[j+1] = jobs[j+1], jobs[j]
        
        # 만약 두 비중이 같다면, 문제 조건에 따라 '번호가 작은 것'이 앞에 오도록 함
        elif jobs[j][0] * jobs[j+1][1] == jobs[j+1][0] * jobs[j][1]:
            if jobs[j][2] > jobs[j+1][2]:
                jobs[j], jobs[j+1] = jobs[j+1], jobs[j]

# 3. 결과 출력
# 정렬된 결과에서 원래 번호만 추출하여 공백으로 구분해 출력
result = []
for job in jobs:
    result.append(str(job[2]))

print(" ".join(result))

#####################################################################################

