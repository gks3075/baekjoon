# Who is in the middle?
ans = [0] * 3

for i in range(3):
    ans[i] = int(input())

ans.sort()
print(ans[1])