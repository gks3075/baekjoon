def solution(myString):
    answer = ''
    i = ord("l")
    for x in myString:
        if ord(x) < i:
            answer += "l"
        else:
            answer += x
    return answer