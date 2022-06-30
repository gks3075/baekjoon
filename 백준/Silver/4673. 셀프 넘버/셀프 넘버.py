#셀프 넘버
def d(n):
    new = n
    while n:
        new += n % 10
        n //= 10
    if new > 10000:
        return
    visited[new] = 1
    d(new)

visited = [0] * 10001
for i in range(1, 10001):
    if visited[i] == 0:
        d(i)

for i in range(1, 10001):
    if visited[i] == 0:
        print(i)