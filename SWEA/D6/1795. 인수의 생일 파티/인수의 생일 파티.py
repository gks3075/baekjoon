# 인수의 생일 파티
def dijkstra(S, A, D, N):  # 시작 번호, 인접행렬, 거리 리스트
    global inf
    U = [0] * (N + 1)   # 선택된 번호 제외
    U[S] = 1
    for v in range(N + 1):
        D[v] = A[S][v]
    for _ in range(N):
        u = 0
        for w in range(N + 1):  # 다익스트라 리스트에서 최솟값인 번호 찾기
            if D[u] > D[w] and U[w] == 0:   # 선택되지 않았고 최솟값인 번호
                u = w
        U[u] = 1    # 선택 번호 표시
        for v in range(N + 1):
            if 0 < A[u][v] < inf:
                D[v] = min(D[v], D[u] + A[u][v])


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())     # N개의 집(1번부터 N번까지), M 간선의 수, X 생일파티 집
    inf = M * 100
    adjM = [[inf] * (N + 1) for _ in range(N + 1)]    # 인접행렬 0번 인덱스는 사용X
    
    for _ in range(M):
        x, y, c = map(int, input().split())     # 출발번호, 도착번호, 걸리는 시간
        adjM[x][y] = c
    for i in range(N + 1):
        adjM[i][i] = 0
    adjM2 = [[inf] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            adjM2[j][i] = adjM[i][j]

    d1 = [0] * (N + 1)
    d2 = [0] * (N + 1)
    dijkstra(X, adjM, d1, N)
    dijkstra(X, adjM2, d2, N)
    ans = [0] * (N + 1)
    for d in range(1, N + 1):
        ans[d] = d1[d] + d2[d]

    print(f'#{tc} {max(ans)}')
