import sys
from itertools import combinations

# 6개국(0~5) 중 2팀을 뽑는 모든 경기 조합 (총 15경기)
matches = list(combinations(range(6), 2))

def solve():
    # 모든 데이터를 공백 단위로 읽어옴
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    final_output = []
    
    # 총 4개의 케이스 처리
    for i in range(4):
        # 18개의 숫자를 읽어 6팀의 [승, 무, 패] 리스트로 변환
        row = list(map(int, input_data[i*18 : (i+1)*18]))
        case = [row[j:j+3] for j in range(0, 18, 3)]
        
        is_possible = 0
        
        # 전처리: 각 팀의 승+무+패 합이 5가 아니면 즉시 불가능 판정
        valid_input = True
        for team in case:
            if sum(team) != 5:
                valid_input = False
                break
        
        if valid_input:
            def dfs(match_idx):
                nonlocal is_possible
                # 이미 가능한 결과를 찾았다면 탐색 중단
                if is_possible:
                    return
                
                # 15경기를 모두 시뮬레이션한 경우
                if match_idx == 15:
                    # 모든 팀의 기록이 0(모든 경기 소화)이면 성공
                    for team in case:
                        if any(team): return
                    is_possible = 1
                    return
                
                t1, t2 = matches[match_idx]
                
                # 1. t1 승리, t2 패배
                if case[t1][0] > 0 and case[t2][2] > 0:
                    case[t1][0] -= 1
                    case[t2][2] -= 1
                    dfs(match_idx + 1)
                    case[t1][0] += 1
                    case[t2][2] += 1
                
                # 2. 무승부
                if case[t1][1] > 0 and case[t2][1] > 0:
                    case[t1][1] -= 1
                    case[t2][1] -= 1
                    dfs(match_idx + 1)
                    case[t1][1] += 1
                    case[t2][1] += 1
                
                # 3. t1 패배, t2 승리
                if case[t1][2] > 0 and case[t2][0] > 0:
                    case[t1][2] -= 1
                    case[t2][0] -= 1
                    dfs(match_idx + 1)
                    case[t1][2] += 1
                    case[t2][0] += 1

            dfs(0)
            
        final_output.append(str(is_possible))
    
    # 결과 출력
    print(" ".join(final_output))

if __name__ == "__main__":
    solve()

##################################################################



