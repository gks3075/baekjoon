def solution(num_list, n):
    h = len(num_list) // n
    answer = [[0]*n for _ in range(h)]
    idx = 0
    for i in range(h):
        for j in range(n):
            answer[i][j] = num_list[idx]
            idx += 1
    return answer