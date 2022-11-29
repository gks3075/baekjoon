answer = 0
def solution(numbers, target):
    global answer
    def dfs(i, s):
        global answer
        if i == len(numbers):
            if s == target:
                answer += 1
            return
        dfs(i + 1, s + numbers[i])
        dfs(i + 1, s - numbers[i])
    dfs(0, 0)
    return answer