prev = None
count = 0
while True:
    t = float(input())
    if t == 0:
        break
    if prev is not None and t < prev:
        count += 1
    prev = t
print(count)