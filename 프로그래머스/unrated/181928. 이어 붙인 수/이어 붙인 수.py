def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for x in num_list:
        if x % 2 == 0:
            even += str(x)
        else:
            odd += str(x)
    answer = int(odd) + int(even)
    return answer