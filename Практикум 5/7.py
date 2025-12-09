n, k, m = map(int, input().split())
if k == m:
    print(0)
else:
    if k <= m:
        stations1 = m - k - 1
    else:
        stations1 = (n - k) + (m - 1)
    if k >= m:
        stations2 = k - m - 1
    else:
        stations2 = (k - 1) + (n - m)
    print(min(stations1, stations2))