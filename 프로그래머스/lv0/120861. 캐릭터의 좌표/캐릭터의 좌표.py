def solution(keyinput, board):
    command = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    
    n, m = board
    x, y = 0, 0
    width, height = n >> 1, m >> 1
    
    for input in keyinput:
        dx, dy = command.get(input)
        nx, ny = x + dx, y + dy
        if -(width) <= nx <= width and -(height) <= ny <= height:
            x, y = nx, ny

    return [x, y]