# 커트라인
N, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)
print(array[k - 1])