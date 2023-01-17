# 추론
N = int(input())
numbers = [0] * N
for i in range(N):
    numbers[i] = int(input())

if numbers[1] - numbers[0] == numbers[2] - numbers[1]:
    print(numbers[N - 1] + numbers[1] - numbers[0])
else:
    print(numbers[N - 1] * (numbers[1] // numbers[0]))