def solution(s):
    answer = True
    s = s.lower()
    p = 0
    y = 0
    for x in s:
        if x == 'p':
            p += 1
        if x == 'y':
            y += 1
    if p != y:
        answer = False

    return answer