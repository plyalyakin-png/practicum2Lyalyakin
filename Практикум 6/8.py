number = int(input())
massive = []
for i in range(201):
    if i < 10:
        massive.append(i)
    elif i < 100:
        massive.extend([i // 10, i % 10])
    else:
        massive.extend([i // 100, (i // 10) % 10, i % 10])
print(massive[number - 1])