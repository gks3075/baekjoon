N = int(input())

answer = 0

if N < 100:
    answer = N
else:
    answer += 99
    for i in range(100, N + 1):
        r = int(str(i)[0]) - int(str(i)[1])
        flag = 1
        for j in range(1, len(str(i)) - 1):
            if int(str(i)[j]) - int(str(i)[j + 1]) != r:
                flag = 0
                break
        if flag:
            answer += 1

print(answer)

