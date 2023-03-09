def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    string = list(my_string)
    string.sort()
    answer = ''.join(string)
    return answer