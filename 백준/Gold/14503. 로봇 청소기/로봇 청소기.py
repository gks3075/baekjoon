N, M = map(int, input().split())
r, c, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

ans = 1
array[r][c] = 2
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
rot = 0

while 1:
    d = (d - 1) % 4
    nr, nc = r + dir[d][0], c + dir[d][1]
    if 0 <= nr < N and 0 <= nc < M and array[nr][nc] == 0:
        ans += 1
        array[nr][nc] = 2
        r = nr
        c = nc
        rot = 0
    else:
        rot += 1
    if rot == 4:
        td = (d + 2) % 4
        nr, nc = r + dir[td][0], c + dir[td][1]
        if 0 <= nr < N and 0 <= nc < M:
            if array[nr][nc] == 1:
                break
            else:
                r = nr
                c = nc
                rot = 0
        else:
            break

print(ans)