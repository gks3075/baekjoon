# 대소문자 바꾸기
word = input()
ans = ''
for x in word:
    if x.isupper():
        ans += x.lower()
    else:
        ans += x.upper()
print(ans)