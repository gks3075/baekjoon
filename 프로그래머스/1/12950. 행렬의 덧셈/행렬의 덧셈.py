def solution(arr1, arr2):
    answer = [[0] * len(arr1[1]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[1])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    return answer