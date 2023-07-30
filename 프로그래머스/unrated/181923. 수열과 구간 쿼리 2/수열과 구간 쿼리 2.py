def solution(arr, queries):
    answer = []
    for q in queries:
        tmp = 10000000
        for x in arr[q[0]: q[1] + 1]:
            if x > q[2]:
                tmp = min(tmp, x)
        if tmp != 10000000:
            answer.append(tmp)
        else:
            answer.append(-1)
    return answer