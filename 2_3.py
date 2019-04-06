#3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#   name — строка, полученная от пользователя,
#   health = 100,
#  damage = 50.
#    Поэкспериментируйте с значениями урона и жизней по желанию.
#    Теперь надо создать функцию attack(person1, person2).
#   Примечание: имена аргументов можете указать свои.
#   Функция в качестве аргумента будет принимать атакующего и атакуемого.
#  В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
#  Функция должна сама работать со словарями и изменять их значения.

# функция вывод здоровья игрока
def player_info(pl):
    return 'Игрок {}: health {}'.format(pl['name'],pl['health'])

# функция атаки
def attack(attacker, defender):
    defender['health'] -= attacker['damage']
    print('{} атаковал {}'.format(attacker['name'], defender['name']))

player = {'name': input('Введите имя игрока: '), 'health': 100, 'damage': 20}
enemy = {'name': input('Введите имя противника: '), 'health': 80, 'damage': 30}

print('До атаки:')
print(player_info(player))
print(player_info(enemy))

#attack(player, enemy)
attack(enemy, player)

print('После атаки:')
print(player_info(player))
print(player_info(enemy))
