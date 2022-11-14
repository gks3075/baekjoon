# 과제 안 내신 분
check = [x for x in range(1, 31)]
for _ in range(28):
    a = int(input())
    check.remove(a)
print(check[0])
print(check[1])