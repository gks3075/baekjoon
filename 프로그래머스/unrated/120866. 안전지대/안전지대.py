def solution(board):
    answer = 0
    n = len(board)
    check = [[0] * n for _ in range(n)]
    d = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                check[i][j] = 1
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        check[ni][nj] = 1
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                answer += 1
            
    return answer