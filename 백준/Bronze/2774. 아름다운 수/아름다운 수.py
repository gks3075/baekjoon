# 아름다운 수
T = int(input())
for i in range(T):
    a = input()
    check = [0] * 10
    for x in a:
        check[int(x)] = 1
    print(sum(check))