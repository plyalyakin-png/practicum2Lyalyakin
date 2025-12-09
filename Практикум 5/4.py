n = int(input())
last = n % 10
two_last = n % 100
if 11 <= two_last <= 14:
    print(n, "попугаев")
elif last == 1:
    print(n, "попугай")
elif 2 <= last <= 4:
    print(n, "попугая")
else:
    print(n,"попугаев")