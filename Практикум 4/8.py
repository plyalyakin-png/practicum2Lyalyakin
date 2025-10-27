MARK1 = 1944
Now = 2025
MARK1 = Now - MARK1
print("Здравствуйте! Как Вас зовут?", end = " ")
name = input().strip()
print(f"Очень приятно,{name}! Меня зовут Марк.")
print("Сколько Вам лет?", end = " ")
age = int(input().strip())
if age < MARK1:
    diff = MARK1 - age
    print(f"Да, {name}, я старше Вас на {diff} лет.")
elif age > MARK1:
    diff = age - MARK1
    print(f"Да, {name}, Вы старше меня на {diff} лет.")
else:
    print(f"Да, {name}, мы с Вами ровесники!")
print("Вам нравится программировать?", end = " ")
answer = input().strip().lower()
if answer in ("да"):
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")