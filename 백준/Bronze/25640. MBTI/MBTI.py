#MBTI
jin = input()
N = int(input())
ans = 0
for i in range(N):
    friend = input()
    if jin == friend:
        ans += 1
print(ans)