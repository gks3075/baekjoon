def solution(num_list):
    answer = num_list
    if num_list[-1] > num_list[-2]:
        tmp = num_list[-1] - num_list[-2]
        answer += [tmp]
    else:
        tmp = num_list[-1] * 2
        answer += [tmp]
    return answer