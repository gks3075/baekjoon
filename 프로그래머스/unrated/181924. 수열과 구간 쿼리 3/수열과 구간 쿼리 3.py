def solution(arr, queries):
    answer = []
    for query in queries:
        i = query[0]
        j = query[1]
        arr[i], arr[j] = arr[j], arr[i]
    answer = arr
    return answer