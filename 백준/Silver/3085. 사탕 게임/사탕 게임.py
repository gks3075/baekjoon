# 사탕게임
import sys
input = sys.stdin.readline

def search(array):
    con = 0
    for i in range(N):
        tmpx = 1
        tmpy = 1
        for j in range(1, N):
            if array[i][j - 1] == array[i][j]:
                tmpx += 1
            else:
                tmpx = 1
            if array[j - 1][i] == array[j][i]:
                tmpy += 1
            else:
                tmpy = 1
            con = max(con, tmpx, tmpy)
    return con

def change(board):
    ans = 0
    for i in range(N):
        for j in range(1, N):
            if board[i][j - 1] != board[i][j]:
                board[i][j - 1], board[i][j] = board[i][j], board[i][j - 1]
                ans = max(ans, search(board))
                board[i][j - 1], board[i][j] = board[i][j], board[i][j - 1]
            if board[j - 1][i] != board[j][i]:
                board[j - 1][i], board[j][i] = board[j][i], board[j - 1][i]
                ans = max(ans, search(board))
                board[j - 1][i], board[j][i] = board[j][i], board[j - 1][i]
            if ans == N:
                return ans
    return ans

N = int(input())
board = [list(map(str, input().strip())) for _ in range(N)]

print(change(board))