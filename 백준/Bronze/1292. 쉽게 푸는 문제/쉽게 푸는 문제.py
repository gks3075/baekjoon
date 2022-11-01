# 쉽게 푸는 문제
from collections import deque
array = deque()
for i in range(100):
    for j in range(i):
        array.append(i)
a, b = map(int, input().split())
ans = 0
for k in range(a - 1, b):
    ans += array[k]
print(ans)