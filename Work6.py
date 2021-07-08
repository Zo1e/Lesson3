def int_func(words):
    result = ''
    for letter in words:
        letter = letter[0].upper() + letter[1:]
        result += letter + ' '
    return result

string = input('Введите строку со словами, разделенными пробелом(в нижнем регистре) - ')
print(int_func(string.split()))






