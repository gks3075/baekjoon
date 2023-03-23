# Intercepting Information
li = list(map(int, input().split()))
ans = "S"
for x in li:
    if x == 9:
        ans = "F"
        break
print(ans)
