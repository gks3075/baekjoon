# 영화감독 숌
def count(N):
    num = str(N)
    cnt = 0
    for x in num:
        if x == '6':
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False

N = int(input())

i = 0
j = 666
while i < N:
    if count(j):
        i += 1
        j += 1
    else:
        j += 1
print(j - 1)