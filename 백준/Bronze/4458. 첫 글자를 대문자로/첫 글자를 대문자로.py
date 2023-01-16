# 첫 글자를 대문자로
T = int(input())
for _ in range(T):
    sen = input()
    ans = sen.upper()[:1] + sen[1:]
    print(ans)
