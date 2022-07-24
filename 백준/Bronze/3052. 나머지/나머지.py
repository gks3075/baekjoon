# 나머지
array = [0] * 10
for i in range(10):
    array[i] = int(input()) % 42

count = list(set(array))
print(len(count))