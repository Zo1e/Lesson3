def my_func():
    a = (input('Введите 3 числа через пробел - '))
    a = a.split()
    a.sort(reverse = True)
    c = int(a[0]) + int(a[1])
    return print(c)
my_func()