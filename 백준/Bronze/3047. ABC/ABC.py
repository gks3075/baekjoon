# ABC
l = list(map(int, input().split()))
l.sort()
abc = input()
for x in abc:
    if x == "A":
        print(l[0], end=' ')
    elif x == "B":
        print(l[1], end=' ')
    else:
        print(l[2], end=' ')