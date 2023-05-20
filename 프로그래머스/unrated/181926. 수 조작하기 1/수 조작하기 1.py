def solution(n, control):
    answer = 0
    for x in control:
        if x == 'w':
            n += 1
        elif x == 's':
            n -= 1
        elif x == 'd':
            n += 10
        else:
            n -= 10
    answer = n
    return answer