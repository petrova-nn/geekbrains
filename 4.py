# 4. Написать функцию, которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError, иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который она вернула.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
#
def number(numb):
    try:
        if numb != 13:
            result = numb ** 2
        else:
            raise ValueError
    except ValueError:
        result = numb
    return result

user_number=int(input('Введите число от 1 до 100: '))
print('Квадрат вашего числа, если оно не равно 13: {}'.format(number(user_number)))