def solution(hp):
    general = hp // 5
    hp %= 5
    soldier = hp // 3
    hp %= 3
    worker = hp
    
    return general + soldier + worker

hp1 = 23
hp2 = 24
hp3 = 999

print(solution(hp1))
print(solution(hp2))
print(solution(hp3))

#################################################

def solution(hp):
    general, hp = divmod(hp, 5)
    soldier, worker = divmod(hp, 3)
    
    return general + soldier + worker

hp1 = 23
hp2 = 24
hp3 = 999

print(solution(hp1))
print(solution(hp2))
print(solution(hp3))

#################################################

def solution(hp):
    ant_powers = [5, 3, 1]
    total_ants = 0
    
    for power in ant_powers:
        total_ants += hp // power
        hp %= power
        
    return total_ants


hp1 = 23
hp2 = 24
hp3 = 999

print(solution(hp1))
print(solution(hp2))
print(solution(hp3))

#################################################

def solution(hp):
    # (hp // 5) : 장군개미 수
    # (hp % 5 // 3) : 장군개미가 남긴 체력 중 병정개미 수
    # (hp % 5 % 3) : 최종 남은 체력 = 일개미 수
    return (hp // 5) + (hp % 5 // 3) + (hp % 5 % 3)

hp1 = 23
hp2 = 24
hp3 = 999

print(solution(hp1))
print(solution(hp2))
print(solution(hp3))

#################################################

def solution(hp):
    ants = 0
    while hp > 0:
        if hp >= 5:
            hp -= 5
        elif hp >= 3:
            hp -= 3
        else:
            hp -= 1
        ants += 1
        
    return ants

hp1 = 23
hp2 = 24
hp3 = 999

print(solution(hp1))
print(solution(hp2))
print(solution(hp3))

#################################################































