def solution(nums):
    answer = 0
    kind = [0] * 200001
    for n in nums:
        kind[n] = 1
    answer = sum(kind) if sum(kind) < len(nums) // 2 else len(nums) // 2
    return answer