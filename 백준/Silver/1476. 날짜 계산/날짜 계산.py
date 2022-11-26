# 날짜 계산
def year(E, S, M):
    E += 1
    S += 1
    M += 1
    if E > 15:
        E = 1
    if S > 28:
        S = 1
    if M > 19:
        M = 1
    return E, S, M

E, S, M = map(int, input().split())
cnt = 1
e, s, m = 1, 1, 1

while E != e or S != s or M != m:
    e, s, m = year(e, s, m)
    cnt += 1
print(cnt)