K = int(input())
i = 0
Identificator = False
while i <= K // 5:
    if (K - 5 * i) % 7 == 0:
        Identificator = True
    i += 1
if Identificator:
    print("да")
else:
    print("нет")