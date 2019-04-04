#3. Создайте программу «Медицинская анкета», где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
#Выведите результат согласно которому:
#1. Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#2. Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг,
#3. Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
#Все остальные варианты можете обработать на ваш вкус и полет фантазии.

name=input('Ваше имя: ')
surname=input('Ваша фамилия: ')
age=int(input('Сколько вам лет? '))
weight=int(input('Ваш вес, пожалуйста: '))

if age < 30 and (weight >=50 and weight <= 120):
    result = '{} {}, {} лет, {} кг. Вы здоровы!'.format(name, surname, age, weight)
    print(result)
elif age < 30 and (weight < 50 or weight > 120):
    result = '{} {}, {} лет, {} кг. У вас проблемы!'.format(name, surname, age, weight)
    print(result)
elif age >= 30 and age <= 39 and (weight <= 50 or weight >= 120):
    result = '{} {}, {} лет, {} кг. Займитесь собой!'.format(name, surname, age, weight)
    print(result)
elif age >= 40 and (weight <= 50 or weight >= 120):
    result = '{} {}, {} лет, {} кг. Обратитесь ко врачу!'.format(name, surname, age, weight)
    print(result)
elif age >= 30 and (weight > 50 and weight < 120):
    result = '{} {}, {} лет, {} кг. Вы в прекрасной форме!'.format(name, surname, age, weight)
    print(result)
else:
    result = '{} {}, {} лет, {} кг. Нет рекомендаций.'.format(name, surname, age, weight)
    print(result)
