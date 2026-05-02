import sys

def check(limit, m, k, pages):
    """
    한 서기공의 최대 페이지 제한이 limit일 때, 
    k명 이내로 모든 책을 배분할 수 있는지 확인합니다.
    """
    count = 1
    current_sum = 0
    for p in pages:
        if p > limit: return False # 한 권이 제한을 넘으면 불가능
        if current_sum + p > limit:
            count += 1
            current_sum = p
        else:
            current_sum += p
    return count <= k

def solve():
    # 데이터 입력 (대량의 데이터를 빠르게 처리)
    data = sys.stdin.read().split()
    if not data: return
    
    m = int(data[0]) # 책의 권수
    k = int(data[1]) # 서기공의 수
    pages = [int(x) for x in data[2:]]
    
    # 이분 탐색 범위 설정
    low = max(pages)
    high = sum(pages)
    ans_limit = high
    
    # 1. 가장 많이 맡는 페이지 수의 최솟값(X) 찾기
    while low <= high:
        mid = (low + high) // 2
        if check(mid, m, k, pages):
            ans_limit = mid
            high = mid - 1
        else:
            low = mid + 1
            
    # 2. 결과 출력을 위한 역순 그리디 배분
    result_groups = []
    current_group = []
    current_sum = 0
    scribes_rem = k # 남은 서기공 수
    
    for i in range(m - 1, -1, -1):
        # 현재 서기공이 책을 더 맡을 수 있는지 확인
        # 조건: 제한(ans_limit)을 넘지 않아야 하며, 
        # 남은 책의 개수(i+1)가 남은 서기공 수(scribes_rem)보다 커야 함 (최소 1권 보장)
        if current_sum + pages[i] <= ans_limit and i + 1 > scribes_rem - 1:
            current_sum += pages[i]
            current_group.append(pages[i])
        else:
            # 새로운 서기공에게 배정 시작
            result_groups.append(current_group[::-1])
            current_group = [pages[i]]
            current_sum = pages[i]
            scribes_rem -= 1
            
    # 마지막 그룹 추가 및 순서 복원
    result_groups.append(current_group[::-1])
    final_groups = result_groups[::-1]
    
    # 출력 형식에 맞춰 '/' 삽입
    output = []
    for idx, group in enumerate(final_groups):
        output.append(" ".join(map(str, group)))
        if idx < len(final_groups) - 1:
            output.append("/")
            
    print(" ".join(output))

if __name__ == "__main__":
    solve()

####################################################################################


