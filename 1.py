# 1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#
#     Примечание: Списки фруктов создайте вручную в начале файла.


first_list = ['apple', 'pear', 'banana', 'melon', 'peach', 'orange']
second_list = ['pear', 'lemon', 'banana', 'cherry', 'apple', 'grapefruit']

mutual_list = [fruit for fruit in first_list if fruit in second_list]
print('Первый список {}'.format(first_list))
print('Второй список {}'.format(second_list))
print('Элементы есть в обоих списках {}'.format(mutual_list))

