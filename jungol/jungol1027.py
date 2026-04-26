import sys

def solve():
    # 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])

    def is_good(seq):
        """현재 수열이 좋은 수열인지 확인하는 함수"""
        length = len(seq)
        # 부분 수열의 길이 k는 1부터 전체 길이의 절반까지
        for k in range(1, length // 2 + 1):
            # 뒤에서부터 k길이의 두 부분 수열이 같은지 비교
            if seq[-k:] == seq[-2*k:-k]:
                return False
        return True

    def backtrack(current_seq):
        # 목표 길이 N에 도달하면 수열 반환
        if len(current_seq) == n:
            print(current_seq)
            return True
        
        # 작은 수부터 찾아야 하므로 1, 2, 3 순서로 시도
        for num in ['1', '2', '3']:
            next_seq = current_seq + num
            if is_good(next_seq):
                # 다음 단계로 진행하고, 성공 시 즉시 종료 (조기 종료)
                if backtrack(next_seq):
                    return True
        return False

    # 빈 수열에서 시작
    backtrack("")

if __name__ == "__main__":
    solve()

###########################################################################

