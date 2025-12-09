n = int(input())
if n <= 0:
    print("неверно")
else:
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        print("верно")
    else:
        print("неверно")