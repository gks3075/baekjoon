# 하노이 탐 이동 순서
def hanoi(n, a, b):
    global cnt
    if n == 0:
        return
    position = [1, 2, 3]
    position.remove(a)
    position.remove(b)
    c = position[0]
    # n - 1 이동
    hanoi(n - 1, a, c)
    # n 이동
    move.append([a, b])
    cnt += 1
    # n - 1 이동
    hanoi(n - 1, c, b)

k = int(input())
cnt = 0
move = []
hanoi(k, 1, 3)
print(cnt)
for x in move:
    print(*x)