def solution(my_string):
    answer = []
    for x in my_string:
        if '0' <= x <= '9':
            answer.append(int(x))
    answer.sort()
    return answer