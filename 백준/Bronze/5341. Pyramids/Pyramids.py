# pyramids
while True:
    base = int(input())
    if base == 0:
        break
    ans = 0
    for i in range(1, base + 1):
        ans += i
    print(ans)