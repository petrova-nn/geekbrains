# 3. Напишите функцию, которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
#
# old_list = [1, -3, 4]
# result = [1, -3, 2]
# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.


# не смогла заменить цикл for на генератор, не придумала, как обработать else
# появлялась синтаксическая ошибка, если писала выражение типа:
# result = [math.sqrt(i) for i in lst if i >=0 else i]

import math

input_list = [1, 4, 9, -6, 0, -4, -8, 25, 36, 49, -1]

def square_list(lst):
    result = []
    for i in lst:
        i = int(math.sqrt(i)) if i >= 0 else i
        result.append(i)
    return result

result = square_list(input_list)
print('Список на входе: {}'.format(input_list))
print('Результат (квадратный корень от положительных чисел, отрицательные без изменений): {}'.format(result))