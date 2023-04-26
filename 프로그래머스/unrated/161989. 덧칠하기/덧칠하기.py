def solution(n, m, section):
    answer = 0
    flag = [0] * (n + 1)
    for x in section:
        flag[x] = 1
    for x in section:
        if flag[x] == 1:
            answer += 1
            for i in range(x, min(n + 1, x + m)):
                flag[i] = 0
    return answer