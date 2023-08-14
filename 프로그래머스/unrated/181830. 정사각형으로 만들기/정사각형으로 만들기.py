def solution(arr):
    answer = [[]]
    r = len(arr)
    c = len(arr[1])
    if r > c:
        for i in range(len(arr)):
            arr[i] = arr[i] + [0] * (r - c)
    elif r < c:
        for i in range(c - r):
            arr.append([0] * c)
    return arr