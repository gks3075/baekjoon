def solution(my_string):
    l = my_string.split(' ')
    answer = int(l[0])
    for i in range(1, len(l) - 1):
        if i % 2 == 1:
            if l[i] == '+':
                answer += int(l[i + 1])
            else:
                answer -= int(l[i + 1])
    return answer