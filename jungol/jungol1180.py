import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(2000)

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    total_count = 0
    ans_list = []
    # 현재까지의 경로를 저장할 리스트
    path = ['1']
    
    # 숫자별 문자열 및 자릿수 미리 계산
    num_strs = [str(i) for i in range(n + 1)]
    # . 연산 시 곱해줄 배수 (10 미만은 10, 10 이상은 100)
    multipliers = [10 if i < 10 else 100 for i in range(n + 1)]

    def dfs(depth, current_sum, last_val, last_op):
        nonlocal total_count
        
        # 모든 숫자를 다 사용했을 때
        if depth == n + 1:
            # 마지막 남은 숫자를 정산하여 0인지 확인
            if current_sum + (last_op * last_val) == 0:
                total_count += 1
                if total_count <= 20:
                    ans_list.append(" ".join(path))
            return

        # 1. '+' 연산자 (사전순 1순위)
        path.append('+')
        path.append(num_strs[depth])
        # 이전까지의 결과를 합산하고 새로운 숫자 시작
        dfs(depth + 1, current_sum + last_op * last_val, depth, 1)
        path.pop()
        path.pop()

        # 2. '-' 연산자 (사전순 2순위)
        path.append('-')
        path.append(num_strs[depth])
        # 이전까지의 결과를 합산하고 새로운 숫자를 빼기 위해 부호 -1 전달
        dfs(depth + 1, current_sum + last_op * last_val, depth, -1)
        path.pop()
        path.pop()

        # 3. '.' 연산자 (사전순 3순위)
        path.append('.')
        path.append(num_strs[depth])
        # 합계는 유지하고 현재 숫자를 이어 붙임
        new_val = last_val * multipliers[depth] + depth
        dfs(depth + 1, current_sum, new_val, last_op)
        path.pop()
        path.pop()

    # 초기 상태: 1번 소부터 시작, 합계 0, 현재 값 1, 부호 +
    dfs(2, 0, 1, 1)

    # 결과 출력
    for s in ans_list:
        print(s)
    print(total_count)

if __name__ == "__main__":
    solve()

#######################################################################


