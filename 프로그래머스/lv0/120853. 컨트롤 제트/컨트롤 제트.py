def solution(s):
    answer = 0
    n_list = s.split(' ')
    for i in range(len(n_list)):
        if n_list[i] == 'Z':
            answer -= int(n_list[i - 1])
        else:
            answer += int(n_list[i])
    return answer