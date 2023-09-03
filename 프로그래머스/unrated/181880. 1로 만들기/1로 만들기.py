def solution(num_list):
    answer = 0
    def count(x):
        i = 0
        while x > 1:
            if x % 2 == 0:
                x //= 2
                i += 1
            else:
                x = (x - 1) // 2
                i += 1
        return i
    for x in num_list:
        answer += count(x)
    return answer