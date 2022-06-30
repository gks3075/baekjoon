#AC
def AC(p, l):
    flag = 1
    front = 0
    end = len(l)
    for x in p:
        if x == 'R':
            if flag == 1:
                flag = -1
            else:
                flag = 1
        else:
            if flag == 1:
                front += 1
            else:
                end -= 1
        if front > end:
            return 'error'
    return [front, end, flag]




T = int(input())
for tc in range(1, T + 1):
    p = input()
    n = int(input())
    if n:
        l = list(map(int, input().lstrip('[').rstrip(']').split(',')))
    else:
        l = input()
        l = []

    ans = AC(p, l)

    if ans == 'error':
        print('error')
    else:
        if ans[2] == -1:
            print('[', end='')
            for i in range(ans[1] - 1, ans[0] - 1, -1):
                if i == ans[0]:
                    print(l[i], end='')
                else:
                    print(l[i], end=',')
            print(']')
        else:
            print('[', end='')
            for i in range(ans[0], ans[1]):
                if i == ans[1] - 1:
                    print(l[i], end='')
                else:
                    print(l[i], end=',')
            print(']')


