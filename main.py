# 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

from lesson3.dir_func import make_dir, del_dir, path_dir
import lesson3.list_func

# for i in path_dir:
#     make_dir(i)

# for i in path_dir:
#     del_dir(i)

print(lesson3.list_func.choice_list())

