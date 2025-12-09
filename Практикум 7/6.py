N = int(input())
start = 1
followers = 1
while followers <= N:
    print(start)
    followers = followers + start
    start = start * 2