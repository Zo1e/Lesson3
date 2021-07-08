def split_func():
    a = int(input('Введите a - '))
    b = int(input('Введите b - '))
    if b == 0:
        print('Деление на ноль невозможно')
        b = int(input('Введите b - '))

    e = a / b
    print((f'Результат - {e}'))
    return e

split_func()