def solution(keyinput, board):
    x, y = 0, 0
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        if key == "left" and x > -max_x:
            x -= 1
        elif key == "right" and x < max_x:
            x += 1
        elif key == "up" and y < max_y:
            y += 1
        elif key == "down" and y > -max_y:
            y -= 1
            
    return [x, y]


a1 = ["left", "right", "up", "right", "right"]
b1 = [11, 11]

a2 = ["down", "down", "down", "down", "down"]
b2 = [7, 9]

print(solution(a1, b1))

print(solution(a2, b2))

#############################################################

def solution(keyinput, board):
    x, y = 0, 0
    max_x, max_y = board[0] // 2, board[1] // 2
    
    move = {
        "left":  (-1, 0),
        "right": (1, 0),
        "up":    (0, 1),
        "down":  (0, -1)
    }
    
    for key in keyinput:
        dx, dy = move[key]
        nx, ny = x + dx, y + dy
        
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            x, y = nx, ny
            
    return [x, y]


a1 = ["left", "right", "up", "right", "right"]
b1 = [11, 11]

a2 = ["down", "down", "down", "down", "down"]
b2 = [7, 9]

print(solution(a1, b1))

print(solution(a2, b2))

#############################################################

def solution(keyinput, board):
    queue = keyinput[:] 
    x, y = 0, 0
    max_x, max_y = board[0] // 2, board[1] // 2
    
    while queue:
        cmd = queue.pop(0) 
        
        if cmd == "left" and x - 1 >= -max_x:  x -= 1
        if cmd == "right" and x + 1 <= max_x:  x += 1
        if cmd == "up" and y + 1 <= max_y:  y += 1
        if cmd == "down" and y - 1 >= -max_y:  y -= 1
        
    return [x, y]



a1 = ["left", "right", "up", "right", "right"]
b1 = [11, 11]

a2 = ["down", "down", "down", "down", "down"]
b2 = [7, 9]

print(solution(a1, b1))

print(solution(a2, b2))




















