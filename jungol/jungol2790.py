import sys

# 빠른 입력을 위한 설정
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    tires = []
    coords = set()
    
    idx = 1
    for _ in range(n):
        i = int(data[idx])
        o = int(data[idx+1])
        p = int(data[idx+2])
        tires.append((i, o, p))
        coords.add(i)
        coords.add(o)
        idx += 3
    
    # 1. 좌표 압축
    sorted_coords = sorted(list(coords))
    coord_map = {val: i + 1 for i, val in enumerate(sorted_coords)}
    max_idx = len(sorted_coords)
    
    # 2. 바깥지름(O) 기준 정렬
    # I < O 조건이 있으므로 O가 같은 타이어들끼리는 서로 포함될 수 없습니다.
    tires.sort(key=lambda x: x[1])
    
    # 3. Binary Indexed Tree (BIT)를 이용한 DP 최적화
    bit = [0] * (max_idx + 1)
    
    def update(idx, val):
        while idx <= max_idx:
            if val > bit[idx]:
                bit[idx] = val
            else:
                break # 최댓값 갱신이 안 되면 중단 (BIT 속성 활용)
            idx += idx & -idx
            
    # 사실 위 break는 일반적인 BIT update에서는 위험할 수 있으나, 
    # 이 문제처럼 단조 증가하는 최댓값 갱신 상황에선 유효합니다.
    # 안전하게 하려면 아래처럼 작성합니다.
    def safe_update(idx, val):
        while idx <= max_idx:
            bit[idx] = max(bit[idx], val)
            idx += idx & -idx

    def query(idx):
        res = 0
        while idx > 0:
            res = max(res, bit[idx])
            idx -= idx & -idx
        return res
    
    ans = 0
    for i, o, p in tires:
        comp_i = coord_map[i]
        comp_o = coord_map[o]
        
        # 현재 타이어를 바깥쪽에 두었을 때 가능한 최대 가격 합
        max_prev = query(comp_i)
        current_total = max_prev + p
        
        # BIT 업데이트 및 전체 최댓값 갱신
        safe_update(comp_o, current_total)
        if current_total > ans:
            ans = current_total
            
    print(ans)

if __name__ == "__main__":
    solve()

####################################################################

