# 1, 2, 3 더하기
def sum_count(n, s):
    global cnt
    if s == n:
        cnt += 1
    if s > n:
        return
    for i in range(1, 4):
        sum_count(n, s + i)



T = int(input())
for _ in range(T):
    cnt = 0
    n = int(input())
    sum_count(n, 0)
    print(cnt)