array = list(map(int, input().split()))
s = 0
for n in array:
    s += n ** 2
print(s % 10)