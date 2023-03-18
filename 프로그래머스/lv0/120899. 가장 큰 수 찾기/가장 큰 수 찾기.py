def solution(array):
    answer = []
    max_id = 0
    for i in range(len(array)):
        if array[i] > array[max_id]:
            max_id = i
    answer.append(array[max_id])
    answer.append(max_id)
    return answer