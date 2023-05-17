def solution(num_list):
    answer = 0
    multi = 1
    for x in num_list:
        multi *= x
    s = sum(num_list)
    if multi < s**2:
        answer = 1
    return answer