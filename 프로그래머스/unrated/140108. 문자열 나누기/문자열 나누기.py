def solution(s):
    answer = 0
    x = s[0]
    y = 0
    n = 0
    for i in range(len(s)):
        if x == s[i]:
            y += 1
        else:
            n += 1
        if y == n:
            answer += 1
            y = 0
            n = 0
            if i == len(s) - 1:
                break
            elif i < len(s) - 1:
                x = s[i + 1]
        elif i == len(s) - 1:
            answer += 1
            break
    return answer