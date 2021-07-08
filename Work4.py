# def my_func(x, y):
#     if x < 0 or x == 0:
#         print('x должен принимать положительное значение!')
#     if y > 0 or y == 0:
#         print('y должен принимать отрицательное значение!')
#     result = x ** y
#     return print(f'Ответ: {result}')
#
# my_func(25, -1)

# def my_func(x, y):
#     if x > 0:
#         print('x должен принимать положительное значение!')
#     if y < 0:
#         print('y должен принимать отрицательное значение!')
#     while

def my_func(x, y):
    if x < 0:
        print('x должен принимать положительное значение!')
    elif y > 0:
        print('y должен принимать отрицательное значение!')
    else:
        result = 1
        while y != 0:
            result /= 5
            y = y + 1
        return result

print(my_func(5,-3))

        