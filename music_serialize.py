# 1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# # С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# # Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import json, pickle

my_favourite_group = {
    'name': 'Ночные снайперы',
    'tracks': ['Колыбельная по-снайперски','31-я весна','Катастрофически','Время года зима','Юго','Куба'],
    'albums': [{'name': 'Капля дёгтя в бочке мёда','year': 1998},
               {'name': 'Детский лепет', 'year': 1999},
               {'name': 'Рубеж', 'year': 2001},
               {'name': 'Цунами', 'year': 2002},
               {'name': 'SMS', 'year': 2004}]
}

json_group = json.dumps(my_favourite_group)
print('to json')
print(json_group)
print(type(json_group))

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group,f)

print('group.json done')

pickle_group = pickle.dumps(my_favourite_group)
print('to pickle')
print(pickle_group)
print(type(pickle_group))

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group,f)

print('group.pickle done')