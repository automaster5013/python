import sys

# L이 최대 30이므로 깊이는 30을 넘지 않으나 안전하게 재귀 한도 설정
sys.setrecursionlimit(2000)

def solve():
    # 입력을 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    L = int(input_data[1])
    words = input_data[2:N+2]
    
    # 오른쪽에서 안쪽으로 채워질 단어들은 뒤집힌 상태로 매칭을 확인해야 합니다.
    words_rev = [w[::-1] for w in words]
    
    memo = {}
    
    def dfs(curr_len, overhang, side):
        # 목표 길이에 도달한 경우
        if curr_len == L:
            # 튀어나온 부분(정중앙에 위치) 자체가 팰린드롬이면 완성!
            if overhang == overhang[::-1]:
                return 1
            else:
                return 0
                
        state = (curr_len, overhang, side)
        if state in memo:
            return memo[state]
            
        ans = 0
        
        if side == 2: # 튀어나온 부분이 없는 경우 (양쪽 길이가 같음)
            # 중복 방지를 위해 무조건 왼쪽에 단어를 배치합니다.
            for w in words:
                nlen = curr_len + len(w)
                if nlen <= L:
                    ans += dfs(nlen, w, 0)
                    
        elif side == 0: # 왼쪽에 튀어나온 부분이 있는 경우 -> 오른쪽에 단어를 추가해야 함
            for w_rev in words_rev:
                s_len = len(w_rev)
                nlen = curr_len + s_len
                if nlen <= L:
                    o_len = len(overhang)
                    if s_len < o_len:
                        if w_rev == overhang[:s_len]:
                            ans += dfs(nlen, overhang[s_len:], 0)
                    elif s_len == o_len:
                        if w_rev == overhang:
                            ans += dfs(nlen, "", 2)
                    else:
                        if w_rev[:o_len] == overhang:
                            ans += dfs(nlen, w_rev[o_len:], 1)
                            
        elif side == 1: # 오른쪽에 튀어나온 부분이 있는 경우 -> 왼쪽에 단어를 추가해야 함
            for w in words:
                s_len = len(w)
                nlen = curr_len + s_len
                if nlen <= L:
                    o_len = len(overhang)
                    if s_len < o_len:
                        if w == overhang[:s_len]:
                            ans += dfs(nlen, overhang[s_len:], 1)
                    elif s_len == o_len:
                        if w == overhang:
                            ans += dfs(nlen, "", 2)
                    else:
                        if w[:o_len] == overhang:
                            ans += dfs(nlen, w[o_len:], 0)
                            
        memo[state] = ans
        return ans

    # 총 길이 0, 튀어나온 부분 없음(side=2)으로 탐색 시작
    print(dfs(0, "", 2))

if __name__ == '__main__':
    solve()

############################################################################################

