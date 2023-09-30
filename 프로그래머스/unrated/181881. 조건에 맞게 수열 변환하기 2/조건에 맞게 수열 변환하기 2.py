def solution(arr):
    answer = 0
    new = arr[:]
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                new[i] = arr[i] * 2 + 1
        
        if new == arr:
            break
        answer += 1
        arr = new[:]

    return answer