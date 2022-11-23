import sys
while True:
    n = sys.stdin.readline()
    n = n.replace('\n', '').strip()
    if len(n) == 0:
        break
    else:
        ans = '1'
        cnt = 1
        while True:
            if int(ans) % int(n) == 0:
                print(cnt)
                break
            else:
                ans += '1'
                cnt += 1
