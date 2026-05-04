import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    f = int(next(it)) # 테스트케이스 수
    
    for _ in range(f):
        n = int(next(it)) # 영역 수
        m = int(next(it)) # 도로 수
        b = int(next(it)) # 블랙홀 수
        
        edges = []
        
        # 도로 정보 (양방향, 가중치 T)
        for _ in range(m):
            s = int(next(it))
            e = int(next(it))
            t = int(next(it))
            edges.append((s, e, t))
            edges.append((e, s, t))
            
        # 블랙홀 정보 (단방향, 가중치 -T)
        for _ in range(b):
            s = int(next(it))
            e = int(next(it))
            t = int(next(it))
            edges.append((s, e, -t))
            
        # 벨만-포드 알고리즘 수행
        # 특정 출발점이 지정되지 않았으므로 모든 노드에서 음수 사이클을 찾기 위해
        # 거리 배열을 모두 0으로 초기화합니다.
        dist = [0] * (n + 1)
        has_negative_cycle = False
        
        for i in range(n):
            for s, e, t in edges:
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
                    # N번째 반복에서도 갱신이 일어나면 음수 사이클 존재
                    if i == n - 1:
                        has_negative_cycle = True
                        
        if has_negative_cycle:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()

######################################################################################3



