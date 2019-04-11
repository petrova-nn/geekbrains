# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# Получить объект — словарь из предыдущего задания.

import json, pickle

with open('group.json', 'r', encoding='utf-8') as f:
    my_favorite_group = json.load(f)

print('from json')
print(my_favorite_group)
print(type(my_favorite_group))

with open('group.pickle','rb') as f:
    my_favorite_group = pickle.load(f)

print('from pickle')
print(my_favorite_group)
print(type(my_favorite_group))
