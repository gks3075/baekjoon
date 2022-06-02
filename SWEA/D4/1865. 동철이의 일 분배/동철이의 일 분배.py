# 동철이의 일 분배
def perm(i, N, p):      # 인덱스, 배열의 크기, 확률
    global maxP
    if i == N:
        if maxP < p:
            maxP = p
    elif maxP >= p:
        return
    else:
        for j in range(N):
            if not used[j]:
                used[j] = 1
                perm(i + 1, N, (p/100) * (arr[i][j]/100) * 100)
                used[j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxP = 0
    used = [0] * N
    perm(0, N, 100)

    print(f'#{tc} {maxP:.6f}')