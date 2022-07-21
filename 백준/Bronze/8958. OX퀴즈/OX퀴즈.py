# OX 퀴즈
T = int(input())
for tc in range(1, T + 1):
    ans_list = input()

    score = 0
    ans = 0
    for x in ans_list:
        if x == 'O':
            score += 1
            ans += score
        else:
            score = 0

    print(ans)