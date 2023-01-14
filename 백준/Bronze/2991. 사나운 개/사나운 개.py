#사나운 개
a, b, c, d = map(int, input().split())
p = list(map(int, input().split()))

for x in p:
    ans = 0
    t = x % (a + b)
    if 0 < t <= a:
        ans += 1
    t = x % (c + d)
    if 0 < t <= c:
        ans += 1
    print(ans)
