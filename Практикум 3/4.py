X, Y, N = map(int, input().split())
TRrub = X*N + (Y*N)//100
TRcop = (Y*N)%100
print(TRrub, 'руб.', TRcop, 'коп.')
