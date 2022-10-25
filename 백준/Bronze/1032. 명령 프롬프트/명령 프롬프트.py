# 명령 프롬프트
N = int(input())
ans = input()
for _ in range(N - 1):
    temp = ''
    word = input()
    for i in range(len(ans)):
        if ans[i] != word[i]:
            temp += '?'
        else:
            temp += ans[i]
    ans = temp
print(ans)
