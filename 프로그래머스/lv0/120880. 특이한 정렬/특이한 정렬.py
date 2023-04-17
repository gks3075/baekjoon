def solution(numlist, n):
    answer = []
    for i in range(len(numlist)):
        numlist[i] = [numlist[i], abs(n - numlist[i])]
    numlist.sort(key = lambda x : (x[1], -x[0]))
    for num in numlist:
        answer.append(num[0])
    return answer