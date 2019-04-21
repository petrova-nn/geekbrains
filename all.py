# 1. Получите текст из файла.
# 2. Разбейте текст на предложения.
# 3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
# 4. Отберите все ссылки.
# 5. Ссылки на страницы какого домена встречаются чаще всего?
# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

import re

#1. Получите текст из файла
with open('text.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    print("Задание 1. Получите текст из файла:\n{}".format(txt))
print("\n")

#2. разбейте на предложения
subs = re.split("\.\s",txt)
print("Задание 2. Текст по предложениям: \n{}".format(subs))
print("\n")

#3. найдите самую используемую форму слова из 4 и более букв, на расском языке
freq_words={}
words=re.findall("\w[а-я]{4,}",txt.lower())

for word in words:
    count = freq_words.get(word, 0)
    freq_words[word] = count + 1

max_val = max(freq_words.values())
print("Задание 3. Словарь частности: \n{}".format(freq_words))
print("Максимальная частота слова: {}".format(max_val))

# не работает
max_words = [key for key, val in freq_words.items() if val == max_val ]
#работает
max_words=[]
for key, val in freq_words.items():
    if val == max_val:
        max_words.append(key)

print("Слова c максимальной - {} - частотой употребления:\n{}".format(max_val,max_words))
print("\n")

#4. Отберите все ссылки.
pattern=re.compile("\S+[a-z]\d?")
#в песочнице работало "\b[^M]\S+[a-z]\d?", здесь не сработало. Хотела исключить Mail.ru
link = pattern.findall(txt)
print("Задание 4. Все встречающиеся в тексте ссылки:\n{}".format(link))
print("\n")

# 5. Ссылки на страницы какого домена встречаются чаще всего?
domain_link = re.findall("\w+[a-z]\.ru", txt)
domain_link.remove('Mail.ru')  #ну хоть так
print("Задание 5. Домены:\n{}".format(domain_link))
print("\n")

print("Или вывод через re.finditer - в столбик:")
for m in re.finditer("\w+[a-z]\.ru", txt):
    print(m[0])
print("\n")

#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
txt1 = re.sub("\S+[a-z]\d?","Ссылка отобразится после регистрации", txt)
print("Задание 6. Замена ссылок на текст. Итог:\n{}".format(txt1))

