while True:
    number = int(input())
    i = 0
    identificator = False
    while i * i <= number:
        if i * i == number:
            print('Число - полный квадрат.')
            identificator = True
            break
        i += 1
    if identificator:
        break
    print('Число не является полным квадратом')
    print('Попробуйте еще раз.')
