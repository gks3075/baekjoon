# 나는 요리사다
n = 0
tot = 0
for i in range(1, 6):
    a = sum(list(map(int, input().split())))
    if tot < a:
        tot = a
        n = i

print(n, tot)