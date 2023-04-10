def solution(order):
    answer = 0
    o = str(order)
    for x in o:
        if x == '3' or x == '6' or x =='9':
            answer += 1
    return answer