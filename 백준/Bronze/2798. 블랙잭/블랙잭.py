# 블랙잭
# def comb(i, N, t, s):
#     global ans, M
#     if t == 3:
#         if ans < s <= M:
#             ans = s
#             return
#     if i == N:
#         return
#     if s >= M:
#         return
#     comb(i + 1, N, t + 1, s + array[i])  # 숫자 선택
#     comb(i + 1, N, t, s)    # 숫자 선택 안함

N, M = map(int, input().split())
array = list(map(int, input().split()))

ans = 0
for i in range(N - 2):
    temp = 0
    temp += array[i]
    if temp > M:
        continue
    for j in range(i + 1, N - 1):
        temp += array[j]
        if temp > M:
            temp -= array[j]
            continue
        for k in range(j + 1, N):
            temp += array[k]
            if ans < temp <= M:
                ans = temp
            temp -= array[k]
        temp -= array[j]

print(ans)



