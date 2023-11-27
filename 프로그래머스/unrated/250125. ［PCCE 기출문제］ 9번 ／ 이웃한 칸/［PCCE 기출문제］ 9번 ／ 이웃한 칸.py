def solution(board, h, w):
    answer = 0
    n = len(board)
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dx, dy in d:
        nx = h + dx
        ny = w + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[h][w] == board[nx][ny]:
                answer += 1
    return answer