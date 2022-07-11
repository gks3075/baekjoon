#소트인사이드
num = list(map(int, input()))
num.sort(reverse=True)
for x in num:
    print(x, end='')