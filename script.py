# 1. Получить количество учеников с сайта geekbrains.ru:
# a) при помощи регулярных выражений,
# b) при помощи библиотеки BeautifulSoup.

import re
from bs4 import BeautifulSoup as BS

with open("index.html", encoding='utf-8') as f:
    page = f.read()

print("При помощи регулярных выражений:\n")
tot_users = re.findall("<span class=\"total-users\">([^<]+)", page)
print("Вся строка: {}".format(tot_users))
tu = str(tot_users)
tu = tu.replace(" ","")
tu = re.findall("\d+", tu)
print("Только число: {}".format(int(tu[0])))

print("\n")

print("При помощи BeautifulSoup:\n")
soup = BS(page,"html.parser")

print("Вся строка: {}".format(soup.span.string))

tu1 = soup.span
tu1 = str(tu1.text)
tu1 = re.findall("[0-9]+", tu1.replace(" ",""))
print("Только число: {}".format(int(tu1[0])))

