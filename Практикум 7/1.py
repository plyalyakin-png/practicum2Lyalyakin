first = 100
while first % 17 != 0:
    first += 1
numbers = []
chislo = first
while chislo <= 999:
    numbers.append(chislo)
    chislo += 17
print(' '.join(map(str, numbers)))
print(len(numbers))