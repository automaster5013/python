import sys

# 깊은 탐색을 위해 재귀 한도를 넉넉히 설정합니다.
sys.setrecursionlimit(10000)

def solve():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽습니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 양 끝에 0과 n+1이라는 가상의 숫자를 붙여 경계 조건을 단순화합니다.
    # 실제 데이터는 인덱스 1부터 n까지 위치하게 됩니다.
    initial_board = [0] + [int(x) for x in input_data[1:]] + [n + 1]

    def get_breaks(arr):
        """연속성(차이가 1)이 깨진 지점의 '인덱스'를 모두 찾습니다."""
        breaks = []
        for i in range(n + 1):
            if abs(arr[i] - arr[i+1]) != 1:
                # i번과 i+1번 사이의 연결이 끊어졌음을 의미합니다.
                breaks.append(i)
        return breaks

    def backtrack(curr_arr, depth, path):
        breaks = get_breaks(curr_arr)
        
        # [가지치기] 현재 끊긴 지점의 수가 남은 기회(3-depth)로 
        # 복구 가능한 수준(기회당 2개)을 넘어서면 즉시 중단합니다.
        if len(breaks) > (3 - depth) * 2:
            return None
        
        # 성공 조건: 모든 숫자가 1씩 차이 나며 정렬된 상태 (0, 1, 2, ..., n+1)
        if not breaks:
            # 3번의 구간을 출력해야 하므로, 이미 정렬됐다면 남은 횟수를 [1, 1]로 채웁니다.
            if depth == 3:
                return path
            return backtrack(curr_arr, depth + 1, path + [[1, 1]])

        # 3번의 기회를 다 썼는데도 연결이 끊긴 곳이 있다면 실패입니다.
        if depth == 3:
            return None

        # [후보군 선정] 
        # 뒤집을 구간 [u, v]의 후보는 반드시 break가 발생한 지점(b)이거나 그 다음(b+1)입니다.
        cand_set = set()
        for b in breaks:
            cand_set.add(b)
            cand_set.add(b + 1)
        
        # 우리가 실제 뒤집을 수 있는 범위는 인덱스 1부터 n까지입니다.
        candidates = sorted([c for c in cand_set if 1 <= c <= n])
        
        num_c = len(candidates)
        for i in range(num_c):
            for j in range(i, num_c):
                u, v = candidates[i], candidates[j]
                
                # 구간 뒤집기 실행 (Slicing 이용)
                # 파이썬의 슬라이싱은 N=1000에서도 충분히 빠릅니다.
                next_arr = curr_arr[:u] + curr_arr[u:v+1][::-1] + curr_arr[v+1:]
                
                res = backtrack(next_arr, depth + 1, path + [[u, v]])
                if res:
                    return res
        return None

    # 탐색 시작!
    answer = backtrack(initial_board, 0, [])
    
    if answer:
        for p in answer:
            print(f"{p[0]} {p[1]}")

if __name__ == "__main__":
    solve()

#######################################################################################

