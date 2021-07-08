def my_func():
    line = input('Введите числа через пробел\n')
    sum = 0
    while line != '$':
        splitline = line.split()
        for el in splitline:
            sum = sum + int(el)
        print(sum)
        line = input('Введите числа через пробел\n')

my_func()