# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

num = [0] * 10
n = a * b * c
for x in str(n):
    x = int(x)
    num[x] += 1
for i in num:
    print(i)