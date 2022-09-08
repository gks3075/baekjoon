# 숫자 카드 2
N = int(input())
array = [0] * 20000001
n_list = list(map(int, input().split()))
for i in range(N):
    array[n_list[i]] += 1
M = int(input())
m_list = list(map(int, input().split()))
for j in range(M):
    print(array[m_list[j]], end=' ')