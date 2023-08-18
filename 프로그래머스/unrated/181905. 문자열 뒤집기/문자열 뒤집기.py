def solution(my_string, s, e):
    answer = ''
    b = my_string[s: e + 1]
    b_inv = b[::-1]
    answer = my_string[:s] + b_inv + my_string[e + 1:]
    return answer