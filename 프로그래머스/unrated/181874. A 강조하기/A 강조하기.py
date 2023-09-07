def solution(myString):
    answer = ''
    for x in myString:
        if x == 'a' or x == 'A':
            answer += 'A'
        elif x.isupper():
            answer += x.lower()
        else:
            answer += x
    return answer