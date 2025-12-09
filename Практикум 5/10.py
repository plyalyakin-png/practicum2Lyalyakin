PIN_code = input()
if len(PIN_code) != 4 or not PIN_code.isdigit():
    print("ERROR")
else:
    if len(set(PIN_code)) != 4:
        print("ERROR")
    else:
        year = int(PIN_code)
        if 1900 <= year <= 2050:
            print("ERROR")
        else:
            print("OK")