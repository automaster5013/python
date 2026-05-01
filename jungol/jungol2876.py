import sys
import math

def solve():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽음
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    while ptr < len(input_data):
        try:
            n = int(input_data[ptr])
            q_cnt = int(input_data[ptr+1])
            ptr += 2
        except (ValueError, IndexError):
            break
            
        if n == 0: break # 종료 조건이 있을 경우 (문제에 따라 다름)

        a = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        
        # 1. 그룹화 전처리
        group = [0] * n
        counts = []
        l_bound = []
        r_bound = []
        
        g_id = 0
        start = 0
        for i in range(1, n):
            if a[i] != a[start]:
                counts.append(i - start)
                l_bound.append(start)
                r_bound.append(i - 1)
                start = i
                g_id += 1
            group[i] = g_id
        
        # 마지막 그룹 추가
        counts.append(n - start)
        l_bound.append(start)
        r_bound.append(n - 1)
        
        num_groups = len(counts)
        
        # 2. 희소 테이블(Sparse Table) 전처리
        if num_groups > 0:
            log_n = num_groups.bit_length()
            st = [[0] * num_groups for _ in range(log_n)]
            st[0] = counts
            
            for j in range(1, log_n):
                for i in range(num_groups - (1 << j) + 1):
                    st[j][i] = max(st[j-1][i], st[j-1][i + (1 << (j-1))])

        def query_st(l, r):
            if l > r: return 0
            j = (r - l + 1).bit_length() - 1
            return max(st[j][l], st[j][r - (1 << j) + 1])

        # 3. 질의 처리
        results = []
        for _ in range(q_cnt):
            s = int(input_data[ptr]) - 1 # 0-indexed 변환
            e = int(input_data[ptr+1]) - 1
            ptr += 2
            
            gs = group[s]
            ge = group[e]
            
            if gs == ge:
                # 시작과 끝이 같은 그룹인 경우
                results.append(str(e - s + 1))
            else:
                # 시작 그룹 자투리, 끝 그룹 자투리, 중간 그룹들 중 최댓값
                v_start = r_bound[gs] - s + 1
                v_end = e - l_bound[ge] + 1
                v_mid = query_st(gs + 1, ge - 1)
                results.append(str(max(v_start, v_end, v_mid)))
        
        sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

###########################################################################

