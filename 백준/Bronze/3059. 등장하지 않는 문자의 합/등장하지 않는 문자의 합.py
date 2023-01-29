# 등장하지 않는 문자의 합
T = int(input())
for _ in range(T):
    ascii = [i for i in range(65, 91)]
    S = input()
    for x in S:
        ascii[ord(x) - 65] = 0
    print(sum(ascii))