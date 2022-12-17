# 시그마
import sys
input = sys.stdin.readline

n = list(map(int, input().strip().split()))
n.sort()

a = n[0]
b = n[1]

if n[0] < 0:
    a = abs(n[0]) + 1

print((a + b) * (b - a + 1) // 2)