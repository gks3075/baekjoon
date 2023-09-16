def solution(my_string, is_prefix):
    answer = 0
    check = my_string[:len(is_prefix)]
    if is_prefix == check:
        answer = 1
    return answer