# 알파벳
def dfs(i, j, ans):
    global max_ans
    max_ans = max(max_ans, ans)
    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if 0 <= ni < R and 0 <= nj < C and not word_array[ni][nj] in alpha:
            alpha.add(word_array[ni][nj])
            dfs(ni, nj, ans + 1)
            alpha.remove(word_array[ni][nj])


R, C = map(int, input().split())
word_array = [list(map(str, input())) for _ in range(R)]

max_ans = 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
alpha = set()
alpha.add(word_array[0][0])
dfs(0, 0, 1)

print(max_ans)