#10
metres = int(input())
print(metres//1609)
#9
N = int(input())
K = int(input())
print(N-N//K*K)
#8
N = int(input())
M = int(input())
print(M//(N+1))
#7
print(10000*0.01)
#6
h = int(input())
w = int(input())
BMI = round((h*0.43592)/((w*0.0254))**2, 2)
print(BMI)
#5
Q = float(input())
Profit = Q*0.19
print(round(Profit,2))
#4
print(1+7+7**3+7**4)
#3
Cash = input().strip()
S, R = map(float, Cash.split())
print(S+R)
#2
price = input().strip()
First, Second = map(str, price.split())
print(First)
print(Second)
#1
Cash = int(input())
Gold = (Cash - 96*48)/(96/16)
print(int(Gold))
