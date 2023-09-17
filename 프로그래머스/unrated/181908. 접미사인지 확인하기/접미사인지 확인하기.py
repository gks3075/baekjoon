def solution(my_string, is_suffix):
    answer = 0
    idx = len(is_suffix)
    if my_string[-idx:] == is_suffix:
        answer = 1
    return answer