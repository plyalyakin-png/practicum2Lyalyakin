s = input().strip()
letter_num = ord(s[0]) - 96
number = int(s[1])
if (letter_num + number) % 2 == 0:
    print("черный")
else:
    print("белый")