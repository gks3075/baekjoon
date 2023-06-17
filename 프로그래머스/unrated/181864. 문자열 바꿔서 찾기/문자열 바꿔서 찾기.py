def solution(myString, pat):
    answer = 0
    new = ''
    for x in pat:
        if x == 'A':
            new += 'B'
        else:
            new += 'A'
    if new in myString:
        answer = 1
    return answer