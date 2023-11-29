def solution(keyinput, board):
    answer = []
    x, y = (0 , 0)
    xx = board[0] // 2
    yy = board[1] // 2
    for key in keyinput:
        if key == "up":
            dx = 0
            dy = 1
        elif key == "down":
            dx = 0
            dy = -1
        elif key == "right":
            dx = 1
            dy = 0
        else:
            dx = -1
            dy = 0
        nx = x + dx
        ny = y + dy
        if -xx <= nx <= xx and -yy <= ny <= yy:
            x, y = nx, ny
    answer = [x, y]
    return answer