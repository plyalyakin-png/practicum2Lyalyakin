n = int(input())
galleons = n // 493  # 17 * 29 = 493
ost = n % 493
sickles = ost // 29
knuts = ost % 29
result = []
if galleons:
    last_one = galleons % 10
    last_two = galleons % 100
    if last_one == 1 and last_two != 11:
        result.append(str(galleons) + " галлеон")
    elif 2 <= last_one <= 4 and (last_two < 10 or last_two >= 20):
        result.append(str(galleons) + " галлеона")
    else:
        result.append(str(galleons) + " галлеонов")
if sickles:
    last_one = sickles % 10
    last_two = sickles % 100
    if last_one == 1 and last_two != 11:
        result.append(str(sickles) + " сикль")
    elif 2 <= last_one <= 4 and (last_two < 10 or last_two >= 20):
        result.append(str(sickles) + " сикля")
    else:
        result.append(str(sickles) + " сиклей")
if knuts:
    last_one = knuts % 10
    last_two = knuts % 100
    if last_one == 1 and last_two != 11:
        result.append(str(knuts) + " кнат")
    elif 2 <= last_one <= 4 and (last_two < 10 or last_two >= 20):
        result.append(str(knuts) + " кната")
    else:
        result.append(str(knuts) + " кнатов")
print(", ".join(result))