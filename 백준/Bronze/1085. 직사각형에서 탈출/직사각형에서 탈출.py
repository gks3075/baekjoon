# 직사각형에서 탈출
x, y, w, h = map(int, input().split())

a = min(x, w-x)
b = min(y, h-y)
print(min(a, b))