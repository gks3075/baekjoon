def solution(my_str, n):
    answer = []
    while len(my_str) > n:
        tmp = my_str[:n]
        my_str = my_str[n:]
        answer.append(tmp)
    answer.append(my_str)
    return answer