import math
N, K, M = map(int, input().split())
print((math.ceil((N * 2) // K)) * M)