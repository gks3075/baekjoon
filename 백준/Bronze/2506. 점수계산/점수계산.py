N = int(input())
score = list(map(int, input().split()))
ans = 0
con = 0
for x in score:
    if x == 1:
        con += 1
        ans += con
    else:
        con = 0
print(ans)