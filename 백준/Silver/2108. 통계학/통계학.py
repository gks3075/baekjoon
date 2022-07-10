# 통계학
N = int(input())
array = [0] * N
count = [0] * (8001)
for i in range(N):
    a = int(input())
    array[i] = a
    count[a + 4000] += 1

def get_mean(l):
    ans = sum(l) / len(l)
    return round(ans)

mean = get_mean(array)
array.sort()
median = array[int(N / 2)]

mode = 0
d = 0
for i in range(8001):
    if count[i] > count[mode]:
        mode = i
        d = 0
    if count[i] == count[mode]:
        if d == 1:
            d += 1
            mode = i
        else:
            d += 1
mode -= 4000

ran = array[-1] - array[0]

print(mean)
print(median)
print(mode)
print(ran)


