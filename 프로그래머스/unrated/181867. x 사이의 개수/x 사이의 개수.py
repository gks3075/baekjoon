def solution(myString):
    answer = []
    str_list = myString.split('x')
    for x in str_list:
        answer.append(len(x))
    return answer