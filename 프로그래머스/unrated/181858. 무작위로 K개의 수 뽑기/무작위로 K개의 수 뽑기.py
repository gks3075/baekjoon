def solution(arr, k):
    answer = []
    check = [0] * 100001
    for x in arr:
        if check[x] == 0:
            answer.append(x)
            check[x] = 1
    if len(answer) > k:
        answer = answer[:k]
    else:
        answer = answer + [-1] * (k - len(answer))
    return answer