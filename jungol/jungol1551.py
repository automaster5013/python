import sys

# 트라이 노드의 깊이가 최대 20이므로 기본 설정으로도 충분하지만, 
# 대량의 노드 처리를 위해 재귀 깊이를 넉넉히 설정합니다.
sys.setrecursionlimit(100000)

class TrieNode:
    __slots__ = ['children', 'is_end', 'is_on_longest_path']
    def __init__(self):
        # 자식 노드들을 저장할 딕셔너리
        self.children = {}
        # 해당 노드에서 단어가 끝나는지 여부
        self.is_end = False
        # 전체 단어 중 가장 긴 단어의 경로에 포함되는지 여부
        self.is_on_longest_path = False

def solve():
    # 표준 입력으로부터 데이터를 한 번에 읽어옵니다.
    try:
        data = sys.stdin.read().split()
    except EOFError:
        return
        
    if not data:
        return
    
    n = int(data[0])
    words = data[1:n+1]

    root = TrieNode()
    longest_word = ""
    
    # 1. 트라이 구축 및 가장 긴 단어 찾기
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    # 2. 가장 긴 단어의 경로를 마킹 (마지막에 활자를 남겨두기 위함)
    curr = root
    for char in longest_word:
        curr = curr.children[char]
        curr.is_on_longest_path = True

    output = []

    # 3. 최적의 순서로 트라이 탐색
    def dfs(node):
        # 현재 노드에서 완성되는 단어가 있다면 인쇄(P)
        if node.is_end:
            output.append('P')
        
        # 자식 노드들을 알파벳 순으로 정렬하여 탐색 (결과의 일관성 유지)
        chars = sorted(node.children.keys())
        
        marked_char = None
        # 최장 경로에 포함된 자식을 찾습니다.
        for char in chars:
            if node.children[char].is_on_longest_path:
                marked_char = char
                break
        
        # 최장 경로가 아닌 자식 노드들을 먼저 방문하고 돌아올 때 활자 제거(-)
        for char in chars:
            if char != marked_char:
                output.append(char)
                dfs(node.children[char])
                output.append('-')
        
        # 가장 긴 단어의 경로는 가장 마지막에 방문 (활자 제거를 하지 않음)
        if marked_char:
            output.append(marked_char)
            dfs(node.children[marked_char])

    dfs(root)

    # 4. 결과 출력
    sys.stdout.write(str(len(output)) + '\n')
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()

#############################################################################



