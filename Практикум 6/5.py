s = input().strip()
start, end = s.split('-')
x = abs(ord(start[0]) - ord(end[0]))
y = abs(int(start[1]) - int(end[1]))
if (x, y) == (1, 2) or (x, y) == (2, 1):
    print("верно")
else:
    print("ошибка")