# 윷놀이
for _ in range(3):
    array = list(map(int, input().split()))
    ans = sum(array)
    if ans == 0:
        print('D')
    elif ans == 1:
        print('C')
    elif ans == 2:
        print('B')
    elif ans == 3:
        print('A')
    else:
        print('E')