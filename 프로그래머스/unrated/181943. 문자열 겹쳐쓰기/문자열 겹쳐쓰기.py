def solution(my_string, overwrite_string, s):
    answer = ''
    n = len(overwrite_string)
    if n + s >= len(my_string):
        answer = my_string[:s] + overwrite_string
    else:
        answer = my_string[:s] + overwrite_string + my_string[n + s:]
    return answer