# Football Team
while True:
    try:
        name = input()
        if len(name) == '0':
            break
        ans = ''
        for x in name:
            if x == 'e':
                ans += 'i'
            elif x == 'i':
                ans += 'e'
            elif x == 'E':
                ans += 'I'
            elif x == 'I':
                ans += 'E'
            else:
                ans += x
        print(ans)
    except:
        break