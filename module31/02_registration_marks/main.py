import re

car_num = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

res = re.findall(r'\b([А-Яа-я]\d{3}[А-Яа-я]{2}\d{3})\b', car_num)
print('Список номеров частных автомобилей: ', res)

res = re.findall(r'\b[А-Яа-я]{2}\d{1,6}', car_num)
print('Список номеров такси: ', res)