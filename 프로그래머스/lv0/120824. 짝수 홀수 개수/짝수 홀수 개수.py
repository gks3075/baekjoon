def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for x in num_list:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    answer = [even, odd]
    return answer