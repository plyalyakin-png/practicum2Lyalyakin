N, K, R = map(float, input().split())
day = 1
length = N
while length < R:
    length = length * (K / 100) + length
    day += 1
print(day)