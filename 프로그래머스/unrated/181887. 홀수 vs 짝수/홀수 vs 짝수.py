def solution(num_list):
    answer = 0
    odd = sum(num_list[::2])
    even = sum(num_list[1::2])
    answer = max(odd, even)
    return answer