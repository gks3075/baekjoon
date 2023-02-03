# 부등호
def search(i, n, p):    # 뽑은 수의 개수, 숫자 합치기, 이전에 뽑은 수
    global min_number, max_number
    if i == k + 1:
        if int(min_number) > int(n):
            min_number = n
        if int(max_number) < int(n):
            max_number = n
        return
    for j in range(10):
        if i == 0:
            used[j] = 1
            search(i + 1, n + str(j), j)
            used[j] = 0
        else:
            if used[j] == 0:
                if sign[i - 1] == '>' and p > j:
                    used[j] = 1
                    search(i + 1, n + str(j), j)
                    used[j] = 0
                elif sign[i - 1] == '<' and p < j:
                    used[j] = 1
                    search(i + 1, n + str(j), j)
                    used[j] = 0

k = int(input())
sign = list(input().split())
numbers = [i for i in range(10)]
used = [0] * 10
min_number = str(1000 ** k)
max_number = str(0)


search(0, '', 0)

print(max_number)
print(min_number)