input_str = input().strip()
N, M = map(int, input_str.split('x'))
K = int(input().strip())
if (K % N == 0 and K // N < M) or (K % M == 0 and K // M < N):
    print("успешно")
else:
    print("неосуществимо")