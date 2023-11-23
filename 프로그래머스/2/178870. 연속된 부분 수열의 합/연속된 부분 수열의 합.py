def solution(sequence, k):
    # answer = [0, len(sequence)]
    # for i in range(len(sequence)):
    #     for j in range(i + 1, len(sequence) + 1):
    #         if sum(sequence[i:j]) == k:
    #             # print(sum(sequence[i:j]))
    #             if answer[1] - answer[0] > j - 1 - i:
    #                 answer = [i, j-1]
    #             break
    #         elif sum(sequence[i:j]) > k:
    #             break
    # return answer
    start, end, total = 0, 0, sequence[0]
    sequence += [0]
    first, second = 1000000, 2000000

    while end < len(sequence) - 1:
        if total <= k:
            if total == k and end - start < second - first:
                first, second = start, end
            end += 1
            total += sequence[end]
        else:
            start += 1
            total -= sequence[start - 1]

    return [first, second]