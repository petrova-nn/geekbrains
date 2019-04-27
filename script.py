# 1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
#http://autocomplete.travelpayouts.com/places2?term=Mos&locale=ru&types[]=country&callback=function

import requests
import json
import re

def get_iata(city):
    try:
        link = "http://autocomplete.travelpayouts.com/places2?term="+city+"&locale=ru"
        data = json.loads(requests.get(link).text)
        data = str(data)
        iata_code = re.findall("code\': \'(\w{3})",data)
        iata_code = iata_code[0]
    except IndexError:
        iata_code = "Нет"
    return iata_code

inp_city =  input("Город назначения: ")
print("IATA-код: {}".format(get_iata(inp_city)))
