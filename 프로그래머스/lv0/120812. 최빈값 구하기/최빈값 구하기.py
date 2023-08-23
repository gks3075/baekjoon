def solution(array):
    answer = 0
    count = [0] * 1001
    for x in array:
        count[x] += 1
    mx = max(count)
    c = 0
    mx_idx = 0
    for i in range(1001):
        if count[i] == mx: 
            c +=1
            mx_idx = i
    if c == 1:
        answer = mx_idx
    else:
        answer = -1
    return answer