# 퇴사
def meet(i, s):     # 미팅 가능 시작일, 이익 합
    global ans
    ans = max(ans, s)
    for t in range(i, N):
        if t + meeting[t][0] <= N:
            meet(t + meeting[t][0], s + meeting[t][1])

N = int(input())
meeting = [0] * N
for i in range(N):
    t, p = map(int, input().split())
    meeting[i] = [t, p]
ans = 0
meet(0, 0)
print(ans)