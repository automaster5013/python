import sys
from collections import deque

def solve_v1():
    # 입력 받기
    try:
        line = sys.stdin.readline()
        if not line: return
        n = int(line.strip())
        
        # 1부터 N까지 카드를 담은 큐 생성
        deck = deque(range(1, n + 1))
        player_cards = []
        
        while deck:
            # 1. 가장 윗장을 플레이어에게 주기
            player_cards.append(deck.popleft())
            
            # 2. 다음 장이 있다면 가장 아래로 보내기
            if deck:
                deck.append(deck.popleft())
                
        # 결과 출력
        print(*(player_cards))
    except EOFError:
        pass

solve_v1()

#############################################################

def solve_v2():
    import sys
    n = int(sys.stdin.readline())
    # 덱을 넉넉한 크기의 리스트로 구현
    deck = list(range(1, n + 1))
    front = 0
    result = []
    
    while front < len(deck):
        # 플레이어에게 주기
        result.append(deck[front])
        front += 1
        
        # 다음 카드를 뒤로 보내기
        if front < len(deck):
            deck.append(deck[front])
            front += 1
            
    print(" ".join(map(str, result)))

solve_v2()

#############################################################

def shuffle(deck, result):
    if not deck:
        return result
    
    # 첫 번째 카드를 결과에 추가
    result.append(deck[0])
    next_deck = deck[1:]
    
    # 남은 카드가 있다면 두 번째 카드를 뒤로 보냄
    if next_deck:
        moved_card = next_deck[0]
        final_deck = next_deck[1:] + [moved_card]
        return shuffle(final_deck, result)
    else:
        return shuffle([], result)

def solve_v3():
    import sys
    sys.setrecursionlimit(2000) # 안전을 위해 재귀 한도 설정
    n = int(sys.stdin.readline())
    res = shuffle(list(range(1, n + 1)), [])
    print(*(res))

solve_v3()

#############################################################

class CardDeck:
    def __init__(self, n):
        from collections import deque
        self.cards = deque(range(1, n + 1))

    def shuffle_and_give(self):
        player_hand = []
        while self.cards:
            # 1단계: 지급
            player_hand.append(self.cards.popleft())
            # 2단계: 이동
            if self.cards:
                self.cards.rotate(-1) # 왼쪽으로 한 칸 회전 (가장 앞을 뒤로)
        return player_hand

def solve_v4():
    import sys
    n = int(sys.stdin.readline())
    my_deck = CardDeck(n)
    print(*(my_deck.shuffle_and_give()))

solve_v4()

#############################################################

def solve_v5():
    import sys
    n = int(sys.stdin.readline())
    cards = list(range(1, n + 1))
    res = []
    
    idx = 0
    while cards:
        # 현재 위치의 카드를 플레이어에게 지급
        res.append(cards.pop(idx))
        
        # 다음 위치 계산 (만약 카드가 남았다면 1칸 건너뜀)
        if not cards: break
        idx = (idx + 1) % len(cards)
        
    print(*(res))

solve_v5()

#############################################################



