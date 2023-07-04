str = input()
ans = ''
for x in str:
    if x.isupper():
        ans += x.lower()
    else:
        ans += x.upper()
print(ans)
