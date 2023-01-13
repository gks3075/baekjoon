# 대표값2
n = [0] * 5
for i in range(5):
    n[i] = int(input())

n.sort()

print(sum(n) // 5)
print(n[2])