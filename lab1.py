# импорт модуля
from requests import get
import re

r = get('http://www.tsu.ru/education/faculties/')
text_code=r.text

emails = re.findall(r"[\w.]+@\w+\.\w+", text_code) # возвращает список найденных фрагментов
emails = set(emails) # множество адресов без повторений
print(len(emails))
print(emails) # вывод


'''\w - любая буква,цифра и _
  + - 1 или более вхождений символа в строку
  . - любой символ, кроме новой строки \n'''
