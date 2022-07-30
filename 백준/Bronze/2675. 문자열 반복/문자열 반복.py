# 문자열 반복
T = int(input())
for tc in range(1, T + 1):
    n, s = map(str, input().split())
    n = int(n)
    p = ''
    for x in s:
        p += x * n
    print(p)
