# 평균은 넘겠지
T = int(input())
for tc in range(1, T + 1):
    scores = list(map(int, input().split()))
    N = scores.pop(0)
    mean = sum(scores) / N

    cnt = 0
    for i in range(N):
        if scores[i] > mean:
            cnt += 1

    ans = cnt / N * 100
    print(f'{ans:.3f}%')