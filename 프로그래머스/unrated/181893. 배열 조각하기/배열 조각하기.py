def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i % 2 == 1:
            arr = arr[query[i]:]

        else:
            arr = arr[:query[i] + 1]

    return arr