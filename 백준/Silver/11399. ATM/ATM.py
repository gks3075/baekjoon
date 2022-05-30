N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
csum = [0] * N
csum[0] = time_list[0]
for i in range(1, N):
    csum[i] = csum[i -1] + time_list[i]
print(sum(csum))