import sys

def solve():
    # 입력 처리 가속
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    target = list(map(int, input_data[1:]))

    # 이웃 관계 확인 함수 (원형 고려: 1과 N은 이웃)
    def is_neighbor(a, b, n):
        return abs(a - b) == 1 or (a == 1 and b == n) or (a == n and b == 1)

    # s1이 [1..n]을 k1만큼 왼쪽으로 민 결과인지 확인 (O(N))
    def get_k1(arr, n):
        idx_of_one = -1
        for i in range(n):
            if arr[i] == 1:
                idx_of_one = i
                break
        if idx_of_one == -1: return -1
        
        # 1부터 순서대로 숫자가 이어지는지 검증
        for i in range(n):
            if arr[(idx_of_one + i) % n] != i + 1:
                return -1
        
        # k1-왼쪽 밀기 시 '1'의 위치는 (n - k1) % n
        k1 = (n - idx_of_one) % n
        # 문제 조건: 1 <= k < n
        if 1 <= k1 < n:
            return k1
        return -1

    # 3단계 조작(k2-왼쪽 밀기)을 되돌림 (1 <= k2 < n)
    for k2 in range(1, n):
        # k2-왼쪽 밀기를 되돌리는 것은 k2-오른쪽 밀기와 같음
        s2 = target[n-k2:] + target[:n-k2]
        
        # 이웃 관계가 깨진 지점(breaks) 찾기
        breaks = []
        for i in range(n):
            if not is_neighbor(s2[i], s2[(i + 1) % n], n):
                breaks.append(i)
        
        # 구간 뒤집기 경계 후보 선정
        # 관계가 깨진 지점 i에 대해 i 또는 i+1이 구간의 끝일 확률이 큼
        cand = {0, n - 1}
        for b in breaks:
            cand.add(b)
            cand.add((b + 1) % n)
        
        cand_list = sorted(list(cand))
        
        # p, q 후보 조합 시도 (후보가 매우 적어 연산량 급감)
        for i in range(len(cand_list)):
            for j in range(i + 1, len(cand_list)):
                p_idx, q_idx = cand_list[i], cand_list[j]
                
                # 구간 뒤집기 수행
                sub_rev = s2[p_idx : q_idx + 1][::-1]
                s1 = s2[:p_idx] + sub_rev + s2[q_idx + 1:]
                
                # 1단계 조작(k1-왼쪽 밀기) 확인
                k1 = get_k1(s1, n)
                if k1 != -1:
                    print(k1)
                    print(f"{p_idx + 1} {q_idx + 1}")
                    print(k2)
                    return

if __name__ == "__main__":
    solve()

##########################################################################

