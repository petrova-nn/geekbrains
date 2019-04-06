#4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#1. Наносит урон. Это улучшенная версия функции из задачи 3.
#2. Вычисляет урон по отношению к броне.

#Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа

# функция вывод здоровья игрока
def player_info(pl):
    return 'Игрок {}: Здоровье {} Урон {}'.format(pl['name'],pl['health'],pl['damage'])

# функция по броне
def armour(attacker, defender):
    armour_attack = round(attacker['damage'] / defender['armour'], 2)
    print('Бронь {} уменьшает атаку до {}'.format(defender['armour'],armour_attack))
    return armour_attack

# функция атаки
def attack2(attacker, defender):
    defender['health'] = round(defender['health'] - armour(attacker, defender),2)
    print('{} атаковал {}'.format(attacker['name'], defender['name']))

player = {'name': input('Введите имя игрока: '), 'health': 100, 'damage': 20, 'armour': 1.2}
enemy = {'name': input('Введите имя противника: '), 'health': 80, 'damage': 30, 'armour': 1.1}

print('До атаки:')
print(player_info(player))
print(player_info(enemy))

#attack2(player, enemy)
attack2(enemy, player)

print('После атаки:')
print(player_info(player))
print(player_info(enemy))

