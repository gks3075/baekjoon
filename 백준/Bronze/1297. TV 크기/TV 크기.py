# TV 크기
import math
D, H, W = map(int, input().split())
p = math.sqrt((D ** 2) / (H ** 2 + W ** 2))
print(int(H * p), int(W * p))