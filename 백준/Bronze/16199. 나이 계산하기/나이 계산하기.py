# 나이 계산하기
by, bm, bd = map(int, input().split())
y, m, d = map(int, input().split())

ans = y - by

if m > bm:
    print(ans)
elif m == bm and d >= bd:
    print(ans)
else:
    print(max(0, ans - 1))

print(ans + 1)
print(ans)