#1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
# Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os

path_dir = [('dir_' + str(i)) for i in range(1,10)]

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print('Уже существует {}'.format(dir_path))

def del_dir(paths):
    del_path = os.path.join(os.getcwd(), paths)
    try:
        os.rmdir(del_path)
    except:
        print('Не могу удалить {}'.format(del_path))


# for i in path_dir:
#     make_dir(i)
#
# for i in path_dir:
#     del_dir(i)

