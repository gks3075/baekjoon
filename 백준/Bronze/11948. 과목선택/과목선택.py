#과목선택
science = [0] * 4
social = [0] * 2
for i in range(4):
    science[i] = int(input())
for i in range(2):
    social[i] = int(input())
science.sort(reverse=True)
social.sort(reverse=True)

ans = sum(science[:3], social[0])
print(ans)
