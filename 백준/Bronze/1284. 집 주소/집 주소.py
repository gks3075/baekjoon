# 집주소
while True:
    num = input()
    if int(num) == 0:
        break
    ans = 2 + len(num) - 1
    for x in num:
        if x == '1':
            ans += 2
        elif x == '0':
            ans += 4
        else:
            ans += 3
    print(ans)